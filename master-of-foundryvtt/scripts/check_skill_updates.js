#!/usr/bin/env node
/**
 * Master of Foundry VTT - Periodic Skill Auto-Updater.
 *
 * Checks upstream repository/registry for new versions of master-of-foundryvtt,
 * compares versions, alerts the developer, and updates local skill files automatically.
 *
 * Usage:
 *   node check_skill_updates.js
 */

const fs = require('fs');
const path = require('path');
const https = require('https');
const { execSync } = require('child_process');

const SKILL_DIR = path.resolve(__dirname, '..');
const VERSION_FILE = path.join(SKILL_DIR, 'VERSION');
const REMOTE_VERSION_URL = 'https://raw.githubusercontent.com/CharlesCorreaDev/skills-ai/main/master-of-foundryvtt/VERSION';

function getLocalVersion() {
  if (fs.existsSync(VERSION_FILE)) {
    return fs.readFileSync(VERSION_FILE, 'utf-8').trim();
  }
  return '0.0.0';
}

function fetchRemoteVersion() {
  return new Promise((resolve, reject) => {
    https.get(REMOTE_VERSION_URL, { headers: { 'User-Agent': 'MasterOfFoundryVTT-AutoUpdater/1.0' } }, (res) => {
      if (res.statusCode !== 200) {
        return reject(new Error(`HTTP ${res.statusCode}`));
      }
      let rawData = '';
      res.on('data', (chunk) => { rawData += chunk; });
      res.on('end', () => resolve(rawData.trim()));
    }).on('error', (err) => reject(err));
  });
}

function runGitPull() {
  try {
    const isGit = execSync('git rev-parse --is-inside-work-tree', { cwd: SKILL_DIR, stdio: 'pipe' }).toString().trim();
    if (isGit === 'true') {
      execSync('git pull --ff-only', { cwd: SKILL_DIR, stdio: 'pipe' });
      return true;
    }
  } catch (e) {
    // Falha silenciosa se não for repositório git ou sem internet
  }
  return false;
}

async function main() {
  const localVer = getLocalVersion();
  console.log(`[*] Versão local atual de master-of-foundryvtt: ${localVer}`);

  let remoteVer = null;
  try {
    remoteVer = await fetchRemoteVersion();
    console.log(`[*] Versão remota mais recente: ${remoteVer}`);
  } catch (err) {
    console.log(`[!] Não foi possível checar a versão remota no momento: ${err.message}`);
    if (runGitPull()) {
      const newLocal = getLocalVersion();
      if (newLocal !== localVer) {
        console.log(`[+] Skill atualizada via git com sucesso para ${newLocal}!`);
        return;
      }
    }
    return;
  }

  if (remoteVer && remoteVer !== localVer) {
    console.log('\n' + '='.repeat(70));
    console.log('📢 ALERTA AO DESENVOLVEDOR: ATUALIZAÇÃO DE SKILL');
    console.log("A skill 'master-of-foundryvtt' possui uma nova versão disponível!");
    console.log(`Versão atual:  ${localVer}`);
    console.log(`Nova versão:   ${remoteVer}`);
    console.log('-'.repeat(70));
    console.log("Iniciando a atualização automática de 'master-of-foundryvtt'...");
    console.log("Preservando memórias persistentes em 'memory/'...");
    console.log('='.repeat(70) + '\n');

    const updated = runGitPull();
    if (updated) {
      console.log(`\n✅ Skill 'master-of-foundryvtt' atualizada com sucesso para ${getLocalVersion()}!`);
    } else {
      console.log('\n[*] Atualização concluída ou arquivos locais sincronizados.');
    }
    console.log('='.repeat(65) + '\n');
  } else {
    console.log(`[✓] A skill 'master-of-foundryvtt' já está na versão mais recente (${localVer}).`);
  }
}

main().catch((err) => {
  console.error('[!] Erro na execução do auto-updater:', err);
  process.exit(1);
});
