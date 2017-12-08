"""For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

    The first row's largest and smallest values are 9 and 1, and their difference is 8.
    The second row's largest and smallest values are 7 and 3, and their difference is 4.
    The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.
"""
import re


def checksum_of_each_line(file_name):
    with open(file_name) as fp:
        input_ = fp.read().splitlines()
        for line in input_:
            list_of_the_numbers_in_line = re.findall('(?P<number>\d+)', line)       # try to find only numbers
            # find difference for each line (max - min)
            output = max(int(number) for number in list_of_the_numbers_in_line) - \
                  min(int(number) for number in list_of_the_numbers_in_line)
            yield output



"""Second part
It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, 
where the result of the division operation is a whole number. They would like you to find those numbers on each line, 
divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5

    In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
    In the second row, the two numbers are 9 and 3; the result is 3.
    In the third row, the result is 2.

In this example, the sum of the results would be 4 + 3 + 2 = 9.
"""

def checksum_of_each_line_second(file_name):
    with open(file_name) as fp:
        input_ = fp.read().splitlines()
        for line in input_:
            list_of_the_numbers_in_line = re.findall('(?P<number>\d+)', line)       # try to find only numbers
            # Sort list in reverse order, from biggest to smallest numbers
            numbers = sorted([int(number) for number in list_of_the_numbers_in_line], key=int, reverse=True)
            # print('\n{}\n'.format(numbers))
            # Check if next number evenly divides the current one
            for i, value in enumerate(numbers):
                for count in range(i+1, len(numbers) + 1):
                    try:
                        if value % numbers[count] == 0:
                            # print('iter: {}:num {} -->> {} / {} = {} '
                                  # '<- forward'.format(i, value, value, numbers[count], value / numbers[count]))
                            yield value / numbers[count]
                            break
                        else:
                            continue
                    except IndexError:
                        pass

if __name__ == '__main__':
    # Sum of all line results, generator used
    print(sum(line_result for line_result in checksum_of_each_line('day2_input')))
    # Result from the second exercise
    print(sum(line_result for line_result in checksum_of_each_line_second('day2_input')))
