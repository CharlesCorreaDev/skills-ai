import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, '..');

const pySrc = path.join(root, 'temp_python', 'python-3.15-docs-text');
const pyDest = path.join(root, 'python-docs');

const djangoSrc = path.join(root, 'temp_django_git', 'docs');
const djangoDest = path.join(root, 'django-docs');

function copyAndConvert(srcDir, destDir, extFrom, extTo) {
  if (!fs.existsSync(destDir)) fs.mkdirSync(destDir, { recursive: true });

  const entries = fs.readdirSync(srcDir, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(srcDir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name.startsWith('.') || entry.name.startsWith('_')) continue;
      const subDest = path.join(destDir, entry.name);
      copyAndConvert(srcPath, subDest, extFrom, extTo);
    } else if (entry.isFile()) {
      if (entry.name.endsWith(extFrom)) {
        const base = path.basename(entry.name, extFrom);
        const destFile = path.join(destDir, `${base}${extTo}`);
        const content = fs.readFileSync(srcPath, 'utf8');
        fs.writeFileSync(destFile, content, 'utf8');
      }
    }
  }
}

console.log('Copiando e organizando documentação do Python (pt-br 3.15)...');
copyAndConvert(pySrc, pyDest, '.txt', '.md');

console.log('Copiando e organizando documentação do Django (6.1 / main)...');
copyAndConvert(djangoSrc, djangoDest, '.txt', '.md');

console.log('Processo de cópia concluído com sucesso!');

