def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("DNA sequences must have equal length")

    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    return differences / len(list1)


def get_p_distance_matrix(list_of_lists):
    n = len(list_of_lists)
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            distance = get_p_distance(list_of_lists[i], list_of_lists[j])
            row.append(round(distance, 5))   # <-- this line was broken before
        matrix.append(row)

    return matrix