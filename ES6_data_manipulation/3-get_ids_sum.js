export default function getStudentIdsSum(Students) {
  return Students.reduce((sum, Students) => sum + Students.id,0); 
}
