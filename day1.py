"""The captcha requires you to review a sequence of digits (your puzzle input)
and find the sum of all digits that match the next digit in the list. The list is circular,
so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit
and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
"""


def solve_captcha(file_name):
    results = []
    with open(file_name) as fp:
        input_ = fp.read()
        for i, digit in enumerate(input_):
            try:
                if digit == input_[i+1]:
                    results.append(int(digit))
            except IndexError:
                if digit == input_[0]:
                    results.append(int(digit))
    return sum(results)

print(solve_captcha('day1_input'))
