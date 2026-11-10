import https from 'node:https';

function check(url) {
  https.get(url, (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
      const regex = /href=["']([^"']+\.(?:zip|tar\.bz2|epub|pdf))["']/gi;
      const links = [];
      let m;
      while ((m = regex.exec(data)) !== null) {
        links.push(m[1]);
      }
      console.log(`URL: ${url}`);
      console.log('Links:', links);
    });
  }).on('error', console.error);
}

check('https://docs.python.org/pt-br/3.15/download.html');
check('https://docs.python.org/3/download.html');
