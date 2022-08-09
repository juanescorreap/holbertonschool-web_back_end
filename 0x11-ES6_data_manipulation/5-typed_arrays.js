export default function createInt8TypedArray(length, position, value) {
  if (position > length - 1) {
    throw Error('Position outside range');
  }
  const arrayBuffer = new ArrayBuffer(length);
  const dataView = new DataView(arrayBuffer, 0);
  dataView.setInt8(position, value);
  return dataView;
}
