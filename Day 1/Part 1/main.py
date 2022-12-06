#tonysnaz - Day 1 Part 1 Advent of Code
def return_max_calories(input):
    max_calories = 0
    temp_calories = 0
    with open(input) as f:
        contents = f.read().splitlines()
        for line in contents:
            if line != '':
                temp_calories += int(line)
            else:
                if temp_calories > max_calories:
                    max_calories = temp_calories
                temp_calories = 0
    return max_calories



if __name__ == '__main__':
    print(return_max_calories('input.txt'))
