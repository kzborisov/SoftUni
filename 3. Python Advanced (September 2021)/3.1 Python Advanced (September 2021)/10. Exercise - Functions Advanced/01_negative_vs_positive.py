def is_negative(number):
    return number <= 0


numbers = [int(x) for x in input().split()]
negatives = [x for x in numbers if is_negative(x)]
positives = [x for x in numbers if not is_negative(x)]
sum_negatives, sum_positives = sum(negatives), sum(positives)

print(sum_negatives)
print(sum_positives)

if abs(sum_negatives) > sum_positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
