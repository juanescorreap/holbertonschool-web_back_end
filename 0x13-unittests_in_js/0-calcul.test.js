const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
  it('result should be a positive integer', () => {
    assert.strictEqual(calculateNumber(8, 8), 16);
    assert.strictEqual(calculateNumber(8, 7.9), 16);
    assert.strictEqual(calculateNumber(1.1, 9), 10);
    assert.strictEqual(calculateNumber(4.5, 4.5), 10);
    assert.strictEqual(calculateNumber(2.7, 1), 4);
    assert.strictEqual(calculateNumber(5.8, 2.2), 8);
  });
  it('result should be a negative integer', () => {
    assert.strictEqual(calculateNumber(-3, 3), 0);
    assert.strictEqual(calculateNumber(-1.2, -1.9), -3);
    assert.strictEqual(calculateNumber(11, -1), 10);
    assert.strictEqual(calculateNumber(-4.5, -4.5), -10);
  });
  it('result should be TypeError', () => {
    assert.throws(() => calculateNumber(NaN, 1.1), { name: 'TypeError' });
    assert.throws(() => calculateNumber(1.1, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber(NaN, NaN), { name: 'TypeError' });
  });
});
