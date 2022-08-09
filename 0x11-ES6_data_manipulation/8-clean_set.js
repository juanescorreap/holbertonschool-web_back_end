export default function cleanSet(set, startString) {
  const newString = '';
  if (!startString || startString.length) {
    return newString;
  }
  for (const item of set) {
    if (item === item.startsWith(startString)) {
      newString.append(item.slice(startString.length));
      newString.append('-');
    }
  }
  return newString.slice(0, -1);
}
