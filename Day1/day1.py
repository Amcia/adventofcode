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


"""
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

    1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
    1221 produces 0, because every comparison is between a 1 and a 2.
    123425 produces 4, because both 2s match each other, but no other digit has a match.
    123123 produces 12.
    12131415 produces 4.
"""


def solve_captcha_second(file_name):
    results = []
    with open(file_name) as fp:
        input_ = fp.read()
        for i, digit in enumerate(input_):
            try:
                # Try to go from the beginning of the list and look up to half away number
                # when you reached half of the list, go further but look up behind
                if i < len(input_)/2 and digit == input_[i+len(input_)/2]:
                    results.append(int(digit))
                elif i >= len(input_)/2 and digit == input_[i-len(input_)/2]:
                    results.append(int(digit))
            except IndexError:
                pass
    return sum(results)

if __name__ == '__main__':
    print(solve_captcha('day1_input'))
    print(solve_captcha_second('day1_input'))

