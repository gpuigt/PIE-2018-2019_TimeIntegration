import numpy as np
import scipy.optimize
from rk import rk_4


def Gear_2(y0, t, f):
    """
    Gear method 2nd order
    y' = f(y, t)
    y(t[0]) = y0
    :param y0: initial value, may be multi-dimensional of size d
    :param t: array of time steps, of size n
    :param f: a function with well shaped input and output
    :return: the solution, of shape (n, d)
    """
    try:
        n, d = len(t), len(y0)
        y = np.zeros((n, d))
    except TypeError:
        n = len(t)
        y = np.zeros((n,))

    y[0] = y0
    y[1] = y0 + (t[1] - t[0]) * f(y0, t[0])

    for i in range(1, n - 1):
        def g(y):
            return y - 4. / 3. * y[i] - 1. / 3. * y[i - 1] + 2. / 3. * (t[i + 1] - t[i]) * f(y, t[i + 1])

        y[i + 1] = scipy.optimize.newton(g, y[i])

    return y


def bdf_6(y0, t, f):
    """
    Backward Differentiation Formula - 6 method
    y' = f(y, t)
    y(t[0]) = y0

    :param y0: initial value, may be multi-dimensional of size d
    :param t: array of time steps, of size n
    :param f: a function with well shaped input and output
    :return: the solution, of shape (n, d)
    """
    try:
        n, d = len(t), len(y0)
        y = np.zeros((n, d))
    except TypeError:
        n = len(t)
        y = np.zeros((n,))
    y[:6] = rk_4(y0, t[:6], f)
    for i in range(n - 6):
        h = t[i + 1] - t[i]
        l = lambda u: 147. * u - 360. * y[i + 5] + 450. * y[i + 4] - 400. * y[i + 3] + 225. * y[i + 2] - 72. * y[
            i + 1] + 10. * y[i] - 60. * h * f(u, t[i + 1])
        y[i + 6] = scipy.optimize.newton(l, y[i + 5])
    return y


if __name__ == '__main__':
    pass
