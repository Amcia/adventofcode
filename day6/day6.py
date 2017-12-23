
def check_memory_loop(memory, current_memory):
    if memory == current_memory:
        return True
    else:
        return False


def memory_distribution(file_name):
    with open(file_name) as fp:
        line = [int(x) for x in fp.read().strip().split()]
        tmp = line  #??????????????????????? zmienia sie
        print(line)
        maximum = max(line)
        print(maximum)
        index = line.index(maximum)
        print(index)

        length = len(line)
        i = index + 1
        count = 0
        while i <= length:
            count += 1
            if i == length:
                i = 0
            if line[index] != 0:
                if i != index:
                    line[index] -= 1
                    line[i] += 1
                    if check_memory_loop(tmp, line):
                        break
                    i += 1
                else:
                    maximum = max(line)
                    index = line.index(maximum)
                    i = index + 1
            else:
                maximum = max(line)
                index = line.index(maximum)
                i = index + 1
        print(count)


if __name__ == '__main__':
    memory_distribution('input')