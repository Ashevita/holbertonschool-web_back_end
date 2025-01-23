const fs = require('fs'); // Importation du module fs pour lire les fichiers

function countStudents(path) {
  try {
    // Lecture du fichier de manière synchrone
    const data = fs.readFileSync(path, 'utf8');

    // Découpage du contenu en lignes
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Suppression de l'en-tête
    const header = lines.shift();

    if (!header || lines.length === 0) {
      throw new Error('Cannot load the database');
    }

    const fields = {};
    let totalStudents = 0;

    for (const line of lines) {
      const studentData = line.split(',');
      if (studentData.length >= 4) { // Ignore les lignes mal formatées
        const firstName = studentData[0].trim();
        const field = studentData[3].trim();

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstName);
        totalStudents = +1;
      }
    }

    // Affiche le nombre total d'étudiants
    console.log(`Number of students: ${totalStudents}`);

    // Affiche le nombre d'étudiants par domaine
    for (const [field, students] of Object.entries(fields)) {
      console.log(
        `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`,
      );
    }
  } catch (error) {
    // Gérer les erreurs et afficher le message demandé
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
