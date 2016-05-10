__author__ = 'eric'

def selection_sort(data):
    """
    Reorder the items in the list datafrom smallest to largest.
    @:param data: [] - a list of comparable objects
    @:return: None - data is sorted in place

    """

    unsorted_front = 0
    while unsorted_front < len(data):

        # Find the index of the smallest item in data[i:].
        smallest_location = unsorted_front
        for unsorted_next in range(unsorted_front + 1, len(data)):
            if data[unsorted_next] < data[smallest_location]:
                smallest_location = unsorted_next

        # Swap smallest item in the unsorted list with the item at the front of unsorted list
        data[unsorted_front], data[smallest_location] = data[smallest_location], data[unsorted_front]

        #advance the unsorted_front indicator to the next item
        unsorted_front += 1