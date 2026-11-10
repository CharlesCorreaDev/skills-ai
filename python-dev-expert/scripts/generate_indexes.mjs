import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, '..');

function generateIndex(dir, title, outFile, relPrefix) {
  let lines = [
    `# ${title} 📚⚡`,
    '',
    `> **Índice Mestre de Navegação Offline**`,
    `> *Consulte este índice para localizar capítulos e tópicos diretamente sem gastar tokens ou buscar na internet.*`,
    '',
    '---',
    ''
  ];

  function walk(currentDir, currentRel) {
    const entries = fs.readdirSync(currentDir, { withFileTypes: true });
    entries.sort((a, b) => a.name.localeCompare(b.name));

    const subDirs = entries.filter(e => e.isDirectory());
    const files = entries.filter(e => e.isFile() && e.name.endsWith('.md') && e.name !== '_INDEX.md');

    if (files.length > 0) {
      const sectionName = currentRel ? `### 📁 ${currentRel}` : `### 📁 Raiz`;
      lines.push(sectionName);
      lines.push('');
      for (const file of files) {
        const filePath = path.join(currentRel, file.name).replace(/\\/g, '/');
        const fileBase = path.basename(file.name, '.md');
        lines.push(`- [${fileBase}](${filePath})`);
      }
      lines.push('');
    }

    for (const sub of subDirs) {
      walk(path.join(currentDir, sub.name), path.join(currentRel, sub.name));
    }
  }

  walk(dir, '');
  fs.writeFileSync(outFile, lines.join('\n'), 'utf8');
  console.log(`Gerado índice em: ${outFile}`);
}

generateIndex(path.join(root, 'python-docs'), 'Documentação Oficial do Python (pt_BR 3.15)', path.join(root, 'python-docs', '_INDEX.md'), 'python-docs');
generateIndex(path.join(root, 'django-docs'), 'Documentação Oficial do Django (6.1)', path.join(root, 'django-docs', '_INDEX.md'), 'django-docs');
