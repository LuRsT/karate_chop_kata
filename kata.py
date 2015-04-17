
def chop(value, list_):
    if len(list_) == 0:
        return -1

    current_list = list_
    x = 0
    while True:
        cutoff_point = int(len(current_list) / 2)
        if cutoff_point == 0:
            if current_list[cutoff_point] == value:
                return cutoff_point + x
            else:
                return -1
        else:
            if current_list[cutoff_point] > value:
                half = current_list[:cutoff_point]
            else:
                half = current_list[cutoff_point:]
                x += cutoff_point

        current_list = half
