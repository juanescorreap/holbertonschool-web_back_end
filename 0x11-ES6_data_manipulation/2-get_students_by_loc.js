export default function getStudentsByLocation(arrayOfstudents, city) {
  return arrayOfstudents.filter((object) => object.city === city);
}
