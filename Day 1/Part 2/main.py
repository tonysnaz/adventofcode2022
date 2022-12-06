#tonysnaz - Day 1 Part 2 Advent of Code

def return_max_calories(input):
    first_calories = 0
    second_calories = 0
    third_calories = 0
    temp_calories = 0
    with open(input) as f:
        contents = f.read().splitlines()
        for line in contents:
            if line != '':
                temp_calories += int(line)
            else:
                if temp_calories > first_calories:
                    third_calories = second_calories
                    second_calories = first_calories
                    first_calories = temp_calories
                elif temp_calories > second_calories:
                    third_calories = second_calories
                    second_calories = temp_calories
                elif temp_calories > third_calories:
                    third_calories = temp_calories
                temp_calories = 0
    return (first_calories + second_calories + third_calories)



if __name__ == '__main__':
    print(return_max_calories('input.txt'))
