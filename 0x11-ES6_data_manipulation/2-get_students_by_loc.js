export default function getStudentsByLocation(arrayOfstudents, city) {
  return arrayOfstudents.filter((object) => object.location === city);
}
