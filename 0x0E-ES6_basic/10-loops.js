export default function appendToEachArrayValue(array, appendString) {
  let idx;
  const array2 = [];
  for (const value of array) {
    idx = array.indexOf(value);
    array2[idx] = appendString + value;
  }

  return array2;
}
