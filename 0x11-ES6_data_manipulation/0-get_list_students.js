export default function getListStudents() {
  const student1 = {
    firstName: 'Guillaume',
    id: 1,
    location: 'San Francisco',
  };
  const student2 = {
    firstName: 'James',
    id: 2,
    location: 'Columbia',
  };
  const student3 = {
    firstName: 'Serena',
    id: 5,
    location: 'San Francisco',
  };
  const array = [];
  array.push(student1);
  array.push(student2);
  array.push(student3);
  return array;
}
