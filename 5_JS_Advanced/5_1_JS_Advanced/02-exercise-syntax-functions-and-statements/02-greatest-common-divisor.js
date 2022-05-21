function gcd(x, y) {
  if (!y) {
    return x;
  }
  return gcd(y, x % y);
}

gcd(15, 5);
gcd(2154, 458);
