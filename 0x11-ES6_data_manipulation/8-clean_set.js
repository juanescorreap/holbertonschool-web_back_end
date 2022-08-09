export default function cleanSet(set, startString) {
  const { length } = startString;
  const newString = '';
  for (const item of set) {
    if (item === startString.substr(0, length)) {
      newString.append(item, '-');
    }
  }
  return newString;
}
