def calculate_next_step(pattern, len_of_needle, state, x):
    if state < len_of_needle and x == pattern[state]:
        return state + 1
    i = 0
    for next_state in range(state, 0, -1):
        if pattern[next_state - 1] == x:
            while i < next_state - 1:
                if pattern[i] != pattern[state - next_state + 1 + i]:
                    break
                i += 1
            if i == next_state - 1:
                return next_state
    return 0

def create_table(pattern, len_of_needle):
    table = [{} for _ in range(len_of_needle + 1)]
    for state in range(len_of_needle + 1):
        for x in pattern:
            table[state][x] = calculate_next_step(pattern, len_of_needle, state, x)
    return table

def search_num_of_in(needle, haystack):
    len_of_needle = len(needle)
    len_of_haystack = len(haystack)
    table = create_table(needle, len_of_needle)
    state = 0
    occurrences = []
    for i in range(len_of_haystack):
        state = table[state].get(haystack[i], 0)
        if state == len_of_needle:
            occurrences.append(i - len_of_needle + 1)
    return occurrences

haystack = "ababaababbaa"
needle = "aaba"
print(search_num_of_in(needle, haystack))
