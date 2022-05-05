def selection_sort_descend_trace(integers):
    for i in range(len(integers) - 1):
        pos = i
        for j in range(i + 1, len(integers)):
            if integers[pos] < integers[j]:
                pos = j
        integers[i], integers[pos] = integers[pos], integers[i]
        for value in integers:
            print(value, end=" ")
        print()
    return integers


if __name__ == "__main__":
    integers = []

    integers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(integers)
