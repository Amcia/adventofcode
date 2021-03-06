"""
SEach square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?o, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?

Your puzzle input is still 265149.
"""

def manhatan_dist(input):
    # Allocation of first 3 variables for each line 45 degrees in the main square
    right_up = {'a_ru': 1, 'b_ru': 3, 'c_ru': 13}
    left_down = {'a_ld': 1, 'b_ld': 7, 'c_ld': 21}
    right_down = {'a_rd': 1, 'b_rd': 9, 'c_rd': 25}
    left_up = {'a_lu': 1, 'b_lu': 5, 'c_lu': 17}
    counter = 2
    while True:
        counter += 1
        LD = 3 * (left_down['c_ld'] - left_down['b_ld']) + left_down['a_ld']
        left_down['a_ld'] = left_down['b_ld']
        left_down['b_ld'] = left_down['c_ld']
        left_down['c_ld'] = LD
        RU = 3 * (right_up['c_ru'] - right_up['b_ru']) + right_up['a_ru']
        right_up['a_ru'] = right_up['b_ru']
        right_up['b_ru'] = right_up['c_ru']
        right_up['c_ru'] = RU
        RD = 3 * (right_down['c_rd'] - right_down['b_rd']) + right_down['a_rd']
        right_down['a_rd'] = right_down['b_rd']
        right_down['b_rd'] = right_down['c_rd']
        right_down['c_rd'] = RD
        LU = 3 * (left_up['c_lu'] - left_up['b_lu']) + left_up['a_lu']
        left_up['a_lu'] = left_up['b_lu']
        left_up['b_lu'] = left_up['c_lu']
        left_up['c_lu'] = LU
        # Point numbers (x,y) are the length of the path to the central point
        print('LU:{:10} <-> RU:{:10}'.format(LU, RU))
        print('|| {:10}     || {:10}'.format('', ''))
        print('LD:{:10} <-> RD:{:10}'.format(LD, RD))
        print('Counter: {}'.format(counter))

        if input > RD:
            continue
        elif LU <= input >= LD:
            distance_to_central = abs(RD - (RD - LD) / 2 - input)
            return distance_to_central + counter
        elif LU <= input:
            distance_to_central = abs(LD - (RD - LD) / 2 - input)
            return distance_to_central + counter
        elif RU <= input:
            distance_to_central = abs(LU - (RD - LD) / 2 - input)
            return distance_to_central + counter
        else:
            distance_to_central = abs(RU - (RD - LD) / 2 - input)
            return distance_to_central + counter


"""
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?

Your puzzle input is still 265149.
"""


class Array:
    row_0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_14 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_17 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_18 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_19 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_20 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    array = []
    position = []

    def __init__(self):
        self.row_10[10] = 1
        self.array = [self.row_0, self.row_1, self.row_2, self.row_3, self.row_4, self.row_5, self.row_6, self.row_7,
                      self.row_8, self.row_9, self.row_10, self.row_11, self.row_12, self.row_13, self.row_14,
                      self.row_15, self.row_16, self.row_17, self.row_18, self.row_19, self.row_20]
        self.position = [0, 0]

    def sum_fields(self):
        self.array[self.position[1]][self.position[0]] = sum(self.array[self.position[1] - 1][self.position[0]],
                                                             self.array[self.position[1] + 1][self.position[0]],
                                                             self.array[self.position[1]][self.position[0] - 1],
                                                             self.array[self.position[1]][self.position[0] + 1],
                                                             self.array[self.position[1] - 1][self.position[0] - 1],
                                                             self.array[self.position[1] + 1][self.position[0] + 1],
                                                             self.array[self.position[1] - 1][self.position[0] + 1],
                                                             self.array[self.position[1] + 1][self.position[0] - 1])

    def move_right(self):
        self.position[0] += 1
        self.sum_fields()

    def move_up(self):
        self.position[1] += 1
        self.sum_fields()

    def move_left(self):
        self.position[0] -= 1
        self.sum_fields()

    def move_down(self):
        self.position[1] -= 1
        self.sum_fields()


def moving_array(arr_obj, input_number):
    count = 0
    y = 0
    x = 1
    while True:
        count += 1
        print(arr_obj.array[arr_obj.position[y]][arr_obj.position[x]])
        if arr_obj.array[arr_obj.position[y]][arr_obj.position[x]] > input_number:
            return arr_obj.array[arr_obj.position[y]][arr_obj.position[x]]
        if arr_obj.array[arr_obj.position[y]+1][arr_obj.position[x]] != 0 or arr_obj.array[arr_obj.position[y]+1][arr_obj.position[x]+1] != 0:
            arr_obj.move_right()
        elif arr_obj.array[arr_obj.position[y]][arr_obj.position[x]-1] != 0 or arr_obj.array[arr_obj.position[y]+1][arr_obj.position[x]-1] != 0:
            arr_obj.move_up()
        elif arr_obj.array[arr_obj.position[y]-1][arr_obj.position[x]] != 0 or arr_obj.array[arr_obj.position[y]-1][arr_obj.position[x]-1] != 0:
            arr_obj.move_left()
        elif arr_obj.array[arr_obj.position[y]][arr_obj.position[x]+1] != 0 or arr_obj.array[arr_obj.position[y]-1][arr_obj.position[x]+1] != 0:
            arr_obj.move_down()


if __name__ == '__main__':
    #print(manhatan_dist(265149))
    arr_1 = Array()
    print(moving_array(arr_1, 265149))



