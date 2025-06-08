def partition(box, gift, low, high, g):
    i = (low - 1)  # index of smaller element
    pivot = gift[g]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if box[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            box[i], box[j] = box[j], box[i]

    box[i + 1], box[high] = box[high], box[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# box[] --> array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(box, gift, low, high):
    g = 0
    if len(box) == 1:
        return box
    if low < high:
        # pi is partitioning index, box[p] is now
        # at right place
        pi = partition(box, gift, low, high, g)
        ++g

        # Separately sort elements before
        # partition and after partition
        quickSort(box, gift, low, pi - 1)
        quickSort(box, gift, pi + 1, high)


box = [4, 2, 0, 3, 1]
gift = [2, 0, 1, 4, 3]

quickSort(box, gift, 0, len(box) - 1)

for i in range(0, len(box)):
    print(box[i])
    print(gift[i])  # if the same numbers are printed back to back, the algorithm is working
