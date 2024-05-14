def read_file(file_path):
    file = open(file_path, 'r')
    try:
        columns, lines = map(int, file.readline().split(' '))
    except ValueError:
        file.close()
        return 0

    matrix = []
    dict_of_letters = dict()
    cur_line = 0
    for line in file:
        line = line.replace('\n', '')
        cur_column = 0
        temp_line = []
        for char in line:
            temp_line.append(char)
            if char in dict_of_letters:
                dict_of_letters[char].append((cur_line, cur_column))
            else:
                dict_of_letters[char] = [(cur_line, cur_column)]

            cur_column += 1

        matrix.append(temp_line)
        cur_line += 1
    file.close()
    return matrix, dict_of_letters, lines, columns


def get_result(matrix, dict_of_letters, rows, columns):
    result = 0
    for j in range(rows):
        queue = [(j, 0)]
        while queue:
            x, y = queue.pop(0)
            if y == columns - 1:
                if x == 0 or x == rows - 1:
                    result += 1
                continue

            for neighbor in dict_of_letters[matrix[x][y]]:
                if neighbor[1] > y:
                    queue.append(neighbor)

            if (x, y + 1) not in queue:
                queue.append((x, y + 1))

    return result


def write_result(output_file, result):
    file = open(output_file, 'w')
    file.write(str(result))
    file.close()
    print(result)


def indiana_jones(input_file, output_file):
    input_data = read_file(input_file)
    if input_data == 0:
        write_result(output_file, 0)
        return

    indiana_jones_matrix, letters_dict, rows, columns = input_data
    result = get_result(indiana_jones_matrix, letters_dict, rows, columns)
    write_result(output_file, result)

# IF YOU WANT TO SEE RESULT IN TERMINAL
# def indiana_jones(input_file):
#     input_data = read_file(input_file)
#     if input_data == 0:
#         print(0)
#         return
#
#     indiana_jones_matrix, letters_dict, rows, columns = input_data
#     result = get_result(indiana_jones_matrix, letters_dict, rows, columns)
#     print(result)
#
#
# indiana_jones("input_file_for_IG1.txt")
