function calculateMoney(fruit, grams, pricePerKG) {
  let weight = grams / 1000;
  let money = weight * pricePerKG;
  console.log(
    `I need $${money.toFixed(2)} to buy ${weight.toFixed(
      2
    )} kilograms ${fruit}.`
  );
}

calculateMoney("orange", 2500, 1.8); // I need $4.50 to buy 2.50 kilograms orange.
calculateMoney("apple", 1563, 2.35);
