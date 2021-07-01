# Taks 04. Odd and Even Sum

def odd_even_sum(digit_as_str):
    odd_nums = [int(x) for x in digit_as_str if not int(x) % 2 == 0]
    even_nums = [int(x) for x in digit_as_str if int(x) % 2 == 0]
    return sum(odd_nums), sum(even_nums)


number_string = input()
odd_sum, even_sum = odd_even_sum(number_string)
print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')