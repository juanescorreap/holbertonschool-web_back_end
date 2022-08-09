export default function updateUniqueItems(myMap) {
  if (!(myMap instanceof Map)) {
    throw Error('Cannot process');
  }
  for (const item of myMap) {
    if (item[1] === 1) {
      myMap.set(item[0], 100);
    }
  }
  return myMap;
}
