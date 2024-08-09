def find_min_pledge(pledge_list):
    pledge_set = set(pledge_list)
    pledge = 1
    while pledge in pledge_set:
        pledge += 1
    return pledge

# Ստուգման օրինակներ
assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1