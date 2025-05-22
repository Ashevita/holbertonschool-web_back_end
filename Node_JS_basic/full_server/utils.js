import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
      if (err) {
        reject(err);
        return;
      }
      const lines = data.trim().split('\n');
      const fields = {};
      const headers = lines[0].split(',');
      const fieldIdx = headers.indexOf('field');
      const fnameIdx = headers.indexOf('firstname');
      if (fieldIdx === -1 || fnameIdx === -1) {
        resolve(fields);
        return;
      }
      for (let i = 1; i < lines.length; i += 1) {
        const row = lines[i].split(',');
        const field = row[fieldIdx];
        const fname = row[fnameIdx];
        if (!fields[field]) fields[field] = [];
        fields[field].push(fname);
      }
      resolve(fields);
    });
  });
}
