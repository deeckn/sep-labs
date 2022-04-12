
class HexError(Exception):
    pass


class InvalidArgument(Exception):
    pass


class NotUpper(Exception):
    pass


def toHex(n):
    if not isinstance(n, int) or n < 0:
        raise InvalidArgument("n must be a positive integer")

    hex_val = str()
    while n != 0:
        temp = n % 16
        if temp < 10:
            hex_val = chr(temp + 48) + hex_val
        else:
            hex_val = chr(temp + 55) + hex_val
        n = int(n // 16)

    return hex_val
