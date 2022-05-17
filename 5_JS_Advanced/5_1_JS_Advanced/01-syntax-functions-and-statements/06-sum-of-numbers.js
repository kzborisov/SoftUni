function sumOfNumber(n, m) {
  let result = 0;
  for (i = Number(n); i <= Number(m); i++) {
    result += i;
  }
  return result;
}

sumOfNumber("1", "5");
