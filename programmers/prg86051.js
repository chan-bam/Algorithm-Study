function solution(numbers) {
  let sum = numbers.reduce((acc, v) => acc += v, 0)
  return 45 - sum;
}