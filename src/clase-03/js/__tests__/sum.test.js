// Test minimalista. Si usás Node >=18, también podés usar node:test en vez de Jest.
import { sum } from '../src/sum.js';

test('sum adds two numbers', () => {
  expect(sum(2, 3)).toBe(5);
});