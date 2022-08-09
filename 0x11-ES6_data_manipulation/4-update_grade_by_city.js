export default function updateStudentGradeByCity(arrayOfstudents, city, newGgrades) {
  const studentsByLocation = arrayOfstudents.filter((student) => student.location === city);
  return studentsByLocation.map((student) => {
    const studentTmp = student;
    const gradesByStudentID = newGgrades.filter((grade) => grade.studentId === student.id);
    if (gradesByStudentID.length !== 0) {
      studentTmp.grade = gradesByStudentID[0].grade;
    } else {
      studentTmp.grade = 'N/A';
    }
    return studentTmp;
  });
}
