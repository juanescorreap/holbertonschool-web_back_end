export default function getStudentIdsSum(arrayOfstudents) {
  return arrayOfstudents.reduce((sum, object) => sum + object.id, 0);
}
