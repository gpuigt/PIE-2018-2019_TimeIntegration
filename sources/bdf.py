import numpy as np
import scipy.optimize
import warnings
from rk import rk_4


def _bdf_i(i, y0, t, f, func_to_minimise, jac):
    try:
        n, d = len(t), len(y0)
        y = np.zeros((n, d))
    except TypeError:
        n = len(t)
        y = np.zeros((n,))
    y[:i] = rk_4(y0, t[:i], f)
    for k in range(n - i):
        result = scipy.optimize.root(func_to_minimise, y[k + i - 1],
                                     args=(t[k + i - 1], t[k + i], *y[k:k + i]), jac=jac)
        if not result.success:
            warnings.warn(result.message)
        y[k + i] = result.x
    return y


def bdf_1(y0, t, f, jac=None):
    """
    BDF1 or Implicit Euler method
    y' = f(y, t)
    y(t[0]) = y0

    :param array_like y0: Initial value, may be multi-dimensional of size d
    :param 1D_array t: Array of time steps, of size n
    :param func f: Function with well shaped input and output
    :param jac: If given, the Jacobian of f
    :type jac: func or None, optional
    :return: numpy.ndarray - The solution, of shape (n, d)
    """

    def func_to_minimise(u, t0, t1, u0):
        return u - u0 - (t1 - t0) * f(u, t1)

    if jac is None:
        jacobian = None
    else:
        def jacobian(u, t0, t1, *args):
            foo = jac(u, t1)
            return np.eye(*foo.shape) - (t1 - t0) * foo

    return _bdf_i(1, y0, t, f, func_to_minimise, jacobian)


def bdf_2(y0, t, f, jac=None):
    """
    BDF2 method
    y' = f(y, t)
    y(t[0]) = y0

    :param array_like y0: Initial value, may be multi-dimensional of size d
    :param 1D_array t: Array of time steps, of size n
    :param func f: Function with well shaped input and output
    :param jac: If given, the Jacobian of f
    :type jac: func or None, optional
    :return: numpy.ndarray - The solution, of shape (n, d)
    """

    def func_to_minimise(u, t1, t2, u0, u1):
        return u - 4. * u1 / 3. + u0 / 3. - 2. * (t2 - t1) * f(u, t2) / 3.

    if jac is None:
        jacobian = None
    else:
        def jacobian(u, t1, t2, *args):
            foo = jac(u, t2)
            return np.eye(*foo.shape) - 2 * (t2 - t1) * foo / 3

    return _bdf_i(2, y0, t, f, func_to_minimise, jacobian)


def bdf_3(y0, t, f, jac=None):
    """
    BDF3 method
    y' = f(y, t)
    y(t[0]) = y0

    :param array_like y0: Initial value, may be multi-dimensional of size d
    :param 1D_array t: Array of time steps, of size n
    :param func f: Function with well shaped input and output
    :param jac: If given, the Jacobian of f
    :type jac: func or None, optional
    :return: numpy.ndarray - The solution, of shape (n, d)
    """

    def func_to_minimise(u, t2, t3, u0, u1, u2):
        return u - 18. * u2 / 11. + 9. * u1 / 11. - 2. * u0 / 11. - 6 * (t3 - t2) * f(u, t3) / 11.

    if jac is None:
        jacobian = None
    else:
        def jacobian(u, t2, t3, *args):
            foo = jac(u, t3)
            return np.eye(*foo.shape) - 6 * (t3 - t2) * foo / 11

    return _bdf_i(3, y0, t, f, func_to_minimise, jacobian)


def bdf_4(y0, t, f, jac=None):
    """
    BDF4 method
    y' = f(y, t)
    y(t[0]) = y0

    :param array_like y0: Initial value, may be multi-dimensional of size d
    :param 1D_array t: Array of time steps, of size n
    :param func f: Function with well shaped input and output
    :param jac: If given, the Jacobian of f
    :type jac: func or None, optional
    :return: numpy.ndarray - The solution, of shape (n, d)
    """

    def func_to_minimise(u, t3, t4, u0, u1, u2, u3):
        return u - 48. * u3 / 25. + 36. * u2 / 25. - 16. * u1 / 25. + 3. * u0 / 25. - 12 * (t4 - t3) * f(u, t4) / 25.

    if jac is None:
        jacobian = None
    else:
        def jacobian(u, t3, t4, *args):
            foo = jac(u, t4)
            return np.eye(*foo.shape) - 12 * (t4 - t3) * foo / 25

    return _bdf_i(4, y0, t, f, func_to_minimise, jacobian)


def bdf_5(y0, t, f, jac=None):
    """
    BDF5 method
    y' = f(y, t)
    y(t[0]) = y0

    :param array_like y0: Initial value, may be multi-dimensional of size d
    :param 1D_array t: Array of time steps, of size n
    :param func f: Function with well shaped input and output
    :param jac: If given, the Jacobian of f
    :type jac: func or None, optional
    :return: numpy.ndarray - The solution, of shape (n, d)
    """

    def func_to_minimise(u, t4, t5, u0, u1, u2, u3, u4):
        return u - 300. * u4 / 137. + 300. * u3 / 137. - 200. * u2 / 137. + 75. * u1 / 137. - 12. * u0 / 137. \
               - 60 * (t5 - t4) * f(u, t5) / 137.

    if jac is None:
        jacobian = None
    else:
        def jacobian(u, t4, t5, *args):
            foo = jac(u, t5)
            return np.eye(*foo.shape) - 60 * (t5 - t4) * foo / 137

    return _bdf_i(5, y0, t, f, func_to_minimise, jacobian)


def bdf_6(y0, t, f, jac=None):
    """
    BDF6 method
    y' = f(y, t)
    y(t[0]) = y0

    :param array_like y0: Initial value, may be multi-dimensional of size d
    :param 1D_array t: Array of time steps, of size n
    :param func f: Function with well shaped input and output
    :param jac: If given, the Jacobian of f
    :type jac: func or None, optional
    :return: numpy.ndarray - The solution, of shape (n, d)
    """

    def func_to_minimise(u, t5, t6, u0, u1, u2, u3, u4, u5):
        return u - 360. * u5 / 147. + 450. * u4 / 147. - 400. * u3 / 147. + 225. * u2 / 147. - 72. * u1 / 147. + 10. * u0 / 147. \
               - 60 * (t6 - t5) * f(u, t6) / 147.

    if jac is None:
        jacobian = None
    else:
        def jacobian(u, t5, t6, *args):
            foo = jac(u, t6)
            return np.eye(*foo.shape) - 60 * (t6 - t5) * foo / 147

    return _bdf_i(6, y0, t, f, func_to_minimise, jacobian)


if __name__ == '__main__':
    pass
