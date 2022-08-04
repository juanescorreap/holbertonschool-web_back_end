import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const array = [];
  const classRoom1 = new ClassRoom(19);
  array.push(classRoom1);
  const classRoom2 = new ClassRoom(20);
  array.push(classRoom2);
  const classRoom3 = new ClassRoom(34);
  array.push(classRoom3);
  return array;
}
