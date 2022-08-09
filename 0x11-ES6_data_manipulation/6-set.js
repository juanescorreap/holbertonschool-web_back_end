export default function setFromArray(array) {
  const mySet = new Set();
  for (const item of array) {
    mySet.add(item);
  }
  return mySet;
}
