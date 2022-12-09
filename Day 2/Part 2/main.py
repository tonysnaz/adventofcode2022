def return_points(input):
    with open(input) as f:
        contents = f.read().splitlines()
        result_list = []
        final_points = 0
        current_line = 0
        for line in contents:
            current_line += 1
            result_list.append(return_result(line))
            final_points += result_list[-1]['Result'] + result_list[-1]['Points']
    return final_points
def return_result(current_match):
    point_allotment = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    result = {
        'Result': 0,
        'Points': 0
    }
    for item in point_allotment:
        if item in current_match:
            result['Points'] = point_allotment.get(item)
            if item == 'X':  # Lose
                if 'A' in current_match:
                    result['Result'] = 3
                elif 'B' in current_match:
                    result['Result'] = 1
                elif 'C' in current_match:
                    result['Result'] = 2
            if item == 'Y':  # Draw
                if 'A' in current_match:
                    result['Result'] = 1
                elif 'B' in current_match:
                    result['Result'] = 2
                elif 'C' in current_match:
                    result['Result'] = 3
            if item == 'Z':  # Win
                if 'A' in current_match:
                    result['Result'] = 2
                elif 'B' in current_match:
                    result['Result'] = 3
                elif 'C' in current_match:
                    result['Result'] = 1
    return result

if __name__ == '__main__':
    print(return_points('input.txt'))
