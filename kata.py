def chop(value, sorted_list, start_index=0):
    if sorted_list == []:
        return -1

    cutoff_index = int(len(sorted_list) / 2)
    if cutoff_index == 0:
        if sorted_list[cutoff_index] == value:
            return start_index + cutoff_index
        else:
            return -1

    if sorted_list[cutoff_index] > value:
        return chop(
            value,
            sorted_list[:cutoff_index],
            start_index,
        )
    else:
        start_index += cutoff_index
        return chop(
            value,
            sorted_list[cutoff_index:],
            start_index,
        )

