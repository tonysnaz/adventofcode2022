def return_item_list(file_input):
    supply_list = []
    with open(file_input) as f:
        contents = f.read().splitlines()
        for line in contents:
            container_1 = []
            container_2 = []
            found_match = False
            for i in range(0, int(len(line) / 2)):
                container_1.append(line[i])
            for i in range(int(len(line) / 2), int(len(line))):
                container_2.append(line[i])
            for i in container_1:
                for j in container_2:
                    if (i in j) and (found_match is False):
                        found_match = True
                        supply_list.append(i)
    return supply_list


def return_sum(supply_list):
    print(supply_list)
    priority_sum = 0
    for item in supply_list:
        if item.isupper():
            item_value = ord(item) - 38
        else:
            item_value = ord(item) - 96
        priority_sum += item_value
    return priority_sum


if __name__ == '__main__':
    print(return_sum(return_item_list('input.txt')))
