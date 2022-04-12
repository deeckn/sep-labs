
class BinError(Exception):
    pass


class InvalidArgument(Exception):
    pass


def binsearch(dataList, key):
    if not isinstance(dataList, list):
        raise InvalidArgument("Datalist should be list only")

    first = 0
    count = len(dataList)
    while 0 < count:
        step = int(count / 2)
        mid = first + step

        if dataList[mid] > key:
            mid += 1
            first = mid
            count -= step + 1
        else:
            count = step

        if first < len(dataList) and dataList[first] == key:
            return first

    return None
