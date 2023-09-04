def float_from_unsigned16(n):
    assert 0 <= n < 2 ** 16
    sign = n >> 15
    exp = (n >> 10) & 0b011111
    fraction = n & (2 ** 10 - 1)
    if exp == 0:
        if fraction == 0:
            return -0.0 if sign else 0.0
        else:
            return (-1) ** sign * fraction / 2 ** 10 * 2 ** (-14)  # subnormal
    elif exp == 0b11111:
        if fraction == 0:
            return float('-inf') if sign else float('inf')
        else:
            return float('nan')
    return (-1) ** sign * (1 + fraction / 2 ** 10) * 2 ** (exp - 15)


float_from_unsigned16(int("0101011101010000", 2))

import numpy as np
import struct
a=struct.pack("H",int("0101011101010000",2))
np.frombuffer(a, dtype =np.float16)[0]