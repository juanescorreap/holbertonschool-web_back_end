export default function updateUniqueItems(myMap) {
  if (!(myMap instanceof Map)) {
    throw Error('Cannot process');
  }
  for (const item of myMap.values()) {
    if (item === 1) {
      myMap.set(item, 100);
    }
  }
  return myMap;
}
