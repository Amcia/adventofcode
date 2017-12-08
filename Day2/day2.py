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

# Sum of all line results, generator used
print(sum(line_result for line_result in checksum_of_each_line('day2_input')))

