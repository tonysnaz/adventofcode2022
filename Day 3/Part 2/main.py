def return_item_list(file_input):
    supply_list = []
    with open(file_input) as f:
        contents = f.read().splitlines()
        elf_count = 0
        elf_list = []
        badge_list = []
        for line in contents:
            elf_count += 1
            elf_list.append(line)
            badge_found = False
            if elf_count % 3 == 0:
                elf_1 = elf_list[elf_count-3]
                elf_2 = elf_list[elf_count-2]
                elf_3 = elf_list[elf_count-1]
                for i in elf_1:
                    for j in elf_2:
                        if i == j:
                            for k in elf_3:
                                if i == k and badge_found is False:
                                    badge_found = True
                                    badge_list.append(i)
    return badge_list


def return_sum(badge_list):
    print(len(badge_list))
    priority_sum = 0
    for item in badge_list:
        if item.isupper():
            item_value = ord(item) - 38
        else:
            item_value = ord(item) - 96
        priority_sum += item_value
    return priority_sum


if __name__ == '__main__':
    print(return_sum(return_item_list('input.txt')))
