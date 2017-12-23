
def file_handler_1_star(file_name):
    with open(file_name) as fp:
        whole_list = fp.read()
        operation_list = whole_list.split('\n')
        for c, value in enumerate(operation_list):
            operation_list[c] = int(value)
        #print(operation_list)
        count = 0
        i = 0
        tmp = 0
        while True:
            try:
                tmp = operation_list[i]
                operation_list[i] = tmp + 1
                i += tmp
                count += 1
            except IndexError:
                break
        print(count)


def file_handler_2_star(file_name):
    with open(file_name) as fp:
        whole_list = fp.read()
        operation_list = whole_list.split('\n')
        for c, value in enumerate(operation_list):
            operation_list[c] = int(value)
        #print(operation_list)
        count = 0
        i = 0
        tmp = 0
        while True:
            try:
                tmp = operation_list[i]
                if tmp >= 3:
                    operation_list[i] = tmp - 1
                else:
                    operation_list[i] = tmp + 1
                i += tmp
                count += 1
            except IndexError:
                break
        print(count)


if __name__ == '__main__':
    file_handler_1_star('input')
    file_handler_2_star('input')
