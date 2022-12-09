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
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    result = {
        'Result': 0,
        'Points': 0
    }
    for item in point_allotment:
        if item in current_match:
            result['Points'] = point_allotment.get(item)
            if item == 'X':
                if 'A' in current_match:
                    result['Result'] = 3
                elif 'B' in current_match:
                    result['Result'] = 0
                elif 'C' in current_match:
                    result['Result'] = 6
            if item == 'Y':
                if 'A' in current_match:
                    result['Result'] = 6
                elif 'B' in current_match:
                    result['Result'] = 3
                elif 'C' in current_match:
                    result['Result'] = 0
            if item == 'Z':
                if 'A' in current_match:
                    result['Result'] = 0
                elif 'B' in current_match:
                    result['Result'] = 6
                elif 'C' in current_match:
                    result['Result'] = 3
    return result

if __name__ == '__main__':
    print(return_points('input.txt'))
