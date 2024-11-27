export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city) // Filtrer les étudiants par ville
    .map((student) => {
      // Trouver la nouvelle note pour l'étudiant
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student, // Conserver les informations existantes de l'étudiant
        grade: gradeObj ? gradeObj.grade : 'N/A', // Ajouter la note ou "N/A" si absente
      };
    });
}
