from finding_bits import *


def test_calc_integral():
    time_axis1 = np.arange(10000)
    amp_axis1 = np.ones(10000)
    def func(x):
        if x % 2 == 0:
            return -1
        else:
            return 1
    assert calc_integral(time_axis1, amp_axis1, func) == 0

