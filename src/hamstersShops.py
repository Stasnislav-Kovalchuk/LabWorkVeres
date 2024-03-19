def max_hamsters_count(first, last, counted_hamsters, supply, hamsters):
    mid_elem = ((first + last) // 2)
    hamsters_count = mid_elem + 1

    temp_arr = sorted([hamster[0] + hamster[1] * mid_elem for hamster in hamsters])
    need_of_food = sum(temp_arr[:mid_elem + 1])
    counted_hamsters[mid_elem] = need_of_food
    if need_of_food == supply:
        return hamsters_count
    if need_of_food > supply:
        last = mid_elem - 1
        return max_hamsters_count(first, last, counted_hamsters, supply, hamsters)
    else:
        next_pos = mid_elem + 1
        if counted_hamsters[next_pos] > supply:
            return hamsters_count
        first = mid_elem + 1
        return max_hamsters_count(first, last, counted_hamsters, supply, hamsters)


def max_hamsters(supply, hamsters):
    first = 0
    last = len(hamsters) - 1
    counted_hamsters = [0] * len(hamsters)

    max_count = max_hamsters_count(first, last, counted_hamsters, supply, hamsters)

    return max_count


s = 18
hamsters = [[5, 1], [3, 1], [5, 2]]
result = max_hamsters(s, hamsters)

print(result)
