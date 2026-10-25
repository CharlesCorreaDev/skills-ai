#!/usr/bin/env node
/**
 * Foundry VTT Media Optimizer & Converter (Images to .webp, Videos to .webm)
 * Author: GM Charles Corrêa (Master of Foundry VTT)
 * 
 * Inspects directories and converts raster images (PNG, JPG, JPEG, GIF, BMP) to .webp
 * and videos (MP4, MOV, MKV, AVI) to .webm (VP9 / Opus) using sharp, ffmpeg, or cwebp.
 * 
 * SVG files are preserved as vector primitives without rasterization.
 */

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'];
const VIDEO_EXTENSIONS = ['.mp4', '.mov', '.mkv', '.avi', '.wmv', '.m4v'];
const AUDIO_EXTENSIONS = ['.mp3', '.wav', '.m4a', '.flac', '.aac', '.wma'];

function hasBinary(binName) {
  try {
    const cmd = process.platform === 'win32' ? `where ${binName}` : `which ${binName}`;
    execSync(cmd, { stdio: 'ignore' });
    return true;
  } catch {
    return false;
  }
}

async function convertImageToWebP(srcPath, destPath, quality = 95) {
  // 1. Try sharp (if available in node_modules)
  try {
    const sharp = (await import('sharp')).default;
    await sharp(srcPath).webp({ quality, effort: 5 }).toFile(destPath);
    return { success: true, method: 'sharp' };
  } catch {}

  // 2. Try cwebp CLI
  if (hasBinary('cwebp')) {
    try {
      execSync(`cwebp -q ${quality} "${srcPath}" -o "${destPath}"`, { stdio: 'pipe' });
      return { success: true, method: 'cwebp' };
    } catch {}
  }

  // 3. Try ffmpeg CLI
  if (hasBinary('ffmpeg')) {
    try {
      execSync(`ffmpeg -y -i "${srcPath}" -quality ${quality} "${destPath}"`, { stdio: 'pipe' });
      return { success: true, method: 'ffmpeg' };
    } catch {}
  }

  return { success: false, reason: 'Nenhum conversor de imagem disponível (instale sharp, cwebp ou ffmpeg).' };
}

function convertVideoToWebM(srcPath, destPath, crf = 16) {
  if (hasBinary('ffmpeg')) {
    try {
      // VP9 + Opus encoding, crf 16 (~95% perceptual quality), optimized for web canvas looping
      const cmd = `ffmpeg -y -i "${srcPath}" -c:v libvpx-vp9 -b:v 0 -crf ${crf} -c:a libopus -b:a 192k -f webm "${destPath}"`;
      execSync(cmd, { stdio: 'pipe' });
      return { success: true, method: 'ffmpeg' };
    } catch (e) {
      return { success: false, reason: e.message };
    }
  }
  return { success: false, reason: 'ffmpeg não encontrado no sistema para conversão de vídeo.' };
}

function convertAudioToOgg(srcPath, destPath, bitrate = '192k') {
  if (hasBinary('ffmpeg')) {
    try {
      // Ogg Vorbis at 192k (quality ~95%), seamless loopable
      const cmd = `ffmpeg -y -i "${srcPath}" -c:a libvorbis -b:a ${bitrate} "${destPath}"`;
      execSync(cmd, { stdio: 'pipe' });
      return { success: true, method: 'ffmpeg' };
    } catch (e) {
      return { success: false, reason: e.message };
    }
  }
  return { success: false, reason: 'ffmpeg não encontrado no sistema para conversão de áudio.' };
}

async function processDirectory(dirPath, options = {}) {
  const { dryRun = false, quality = 95, crf = 16, deleteOriginal = false } = options;

  if (!fs.existsSync(dirPath)) {
    console.error(`[!] Caminho '${dirPath}' não encontrado.`);
    process.exit(1);
  }

  const stat = fs.statSync(dirPath);
  const targets = [];

  if (stat.isFile()) {
    targets.push(dirPath);
  } else {
    function walk(dir) {
      for (const item of fs.readdirSync(dir)) {
        if (item === 'node_modules' || item === '.git') continue;
        const full = path.join(dir, item);
        const s = fs.statSync(full);
        if (s.isDirectory()) {
          walk(full);
        } else {
          targets.push(full);
        }
      }
    }
    walk(dirPath);
  }

  let convertedCount = 0;

  for (const filePath of targets) {
    const ext = path.extname(filePath).toLowerCase();

    // SVG preservation notice
    if (ext === '.svg') {
      console.log(`[PRESERVADO] ${filePath} (SVG nativo vetorial mantido intacto)`);
      continue;
    }

    if (IMAGE_EXTENSIONS.includes(ext)) {
      const destPath = filePath.slice(0, -ext.length) + '.webp';
      if (dryRun) {
        console.log(`[SIMULAÇÃO] Imagem: ${filePath} -> ${destPath}`);
      } else {
        process.stdout.write(`[*] Convertendo imagem: ${path.basename(filePath)} -> .webp ... `);
        const res = await convertImageToWebP(filePath, destPath, quality);
        if (res.success) {
          convertedCount++;
          console.log(`OK (${res.method})`);
          if (deleteOriginal && fs.existsSync(destPath) && destPath !== filePath) {
            fs.unlinkSync(filePath);
          }
        } else {
          console.log(`FALHA: ${res.reason}`);
        }
      }
    } else if (VIDEO_EXTENSIONS.includes(ext)) {
      const destPath = filePath.slice(0, -ext.length) + '.webm';
      if (dryRun) {
        console.log(`[SIMULAÇÃO] Vídeo: ${filePath} -> ${destPath}`);
      } else {
        process.stdout.write(`[*] Convertendo vídeo: ${path.basename(filePath)} -> .webm ... `);
        const res = convertVideoToWebM(filePath, destPath, crf);
        if (res.success) {
          convertedCount++;
          console.log(`OK (${res.method})`);
          if (deleteOriginal && fs.existsSync(destPath) && destPath !== filePath) {
            fs.unlinkSync(filePath);
          }
        } else {
          console.log(`FALHA: ${res.reason}`);
        }
      }
    } else if (AUDIO_EXTENSIONS.includes(ext)) {
      const destPath = filePath.slice(0, -ext.length) + '.ogg';
      if (dryRun) {
        console.log(`[SIMULAÇÃO] Áudio/Música: ${filePath} -> ${destPath}`);
      } else {
        process.stdout.write(`[*] Convertendo áudio: ${path.basename(filePath)} -> .ogg ... `);
        const res = convertAudioToOgg(filePath, destPath);
        if (res.success) {
          convertedCount++;
          console.log(`OK (${res.method})`);
          if (deleteOriginal && fs.existsSync(destPath) && destPath !== filePath) {
            fs.unlinkSync(filePath);
          }
        } else {
          console.log(`FALHA: ${res.reason}`);
        }
      }
    }
  }

  console.log(`\nConcluído. Itens processados: ${targets.length}. Convertidos: ${convertedCount}.`);
}

const args = process.argv.slice(2);
const dryRun = args.includes('--dry-run');
const deleteOriginal = args.includes('--delete-original');
const target = args.find(a => !a.startsWith('--'));

if (!target) {
  console.log('Uso: node scripts/convert_media.js <arquivo-ou-pasta> [--dry-run] [--delete-original]');
  process.exit(0);
}

processDirectory(target, { dryRun, deleteOriginal }).catch(err => {
  console.error('[!] Erro:', err);
  process.exit(1);
});
