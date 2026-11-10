import fs from 'node:fs';
import path from 'node:path';
import https from 'node:https';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, '..');

function download(url, dest) {
  return new Promise((resolve, reject) => {
    console.log(`Iniciando download de: ${url}`);
    const file = fs.createWriteStream(dest);
    https.get(url, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        return download(res.headers.location, dest).then(resolve).catch(reject);
      }
      if (res.statusCode !== 200) {
        return reject(new Error(`Status ${res.statusCode} para ${url}`));
      }
      res.pipe(file);
      file.on('finish', () => {
        file.close();
        console.log(`Download concluído: ${dest} (${fs.statSync(dest).size} bytes)`);
        resolve();
      });
    }).on('error', (err) => {
      fs.unlink(dest, () => {});
      reject(err);
    });
  });
}

async function run() {
  const pythonZip = path.join(root, 'python-docs.zip');
  const djangoZip = path.join(root, 'django-docs.zip');

  await download('https://docs.python.org/pt-br/3.15/archives/python-3.15-docs-text.zip', pythonZip);
  await download('https://media.readthedocs.org/htmlzip/django/latest/django.zip', djangoZip);
}

run().catch(console.error);

