export default function cleanSet(set, startString) {
  let newString = '';
  if (!startString || !startString.length) {
    return newString;
  }
  for (const item of set) {
    if (item && item.startsWith(startString)) {
      newString += `${item.slice(startString.length)}-`;
    }
  }
  return newString.slice(0, -1);
}
