export default function getStudentsByLocation(studentlist, city) {
  return studentlist.filter((student) => student.location === city);
}
