import { readDatabase } from '../utils.js';

class StudentsController {
  static getAllStudents(req, res) {
    const dbFile = process.argv[2];
    readDatabase(dbFile)
      .then((fields) => {
        let response = 'This is the list of our students\n';
        const sortedFields = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
        sortedFields.forEach((field, idx) => {
          response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
          if (idx !== sortedFields.length - 1) response += '\n';
        });
        res.status(200).send(response);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const dbFile = process.argv[2];
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    readDatabase(dbFile)
      .then((fields) => {
        const list = fields[major] || [];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
