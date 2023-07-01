"""
Collection of the core mathematical operators used throughout the code base.
"""


import math
from typing import Callable, Iterable

# ## Task 0.1

# Implementation of a prelude of elementary functions.


def mul(x: float, y: float) -> float:
    ":math:`f(x, y) = x * y`"
    # TODO: Implement for Task 0.1.
    return x * y


def id(x: float) -> float:
    ":math:`f(x) = x`"
    # TODO: Implement for Task 0.1.
    return x


def add(x: float, y: float) -> float:
    ":math:`f(x, y) = x + y`"
    # TODO: Implement for Task 0.1.
    return x + y


def neg(x: float) -> float:
    ":math:`f(x) = -x`"
    # TODO: Implement for Task 0.1.
    return -x


def lt(x: float, y: float) -> float:
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    # TODO: Implement for Task 0.1.
    return 1.0 if x < y else 0.0


def eq(x: float, y: float) -> float:
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    # TODO: Implement for Task 0.1.
    return 1.0 if x == y else 0.0


def max(x: float, y: float) -> float:
    ":math:`f(x) =` x if x is greater than y else y"
    # TODO: Implement for Task 0.1.
    return x if x > y else y


def is_close(x: float, y: float) -> float:
    ":math:`f(x) = |x - y| < 1e-2`"
    # TODO: Implement for Task 0.1.
    return abs(x - y) < 1e-2


def sigmoid(x: float) -> float:
    r"""
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}`
    (See `<https://en.wikipedia.org/wiki/Sigmoid_function>`_ .)

    Calculate as
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}` if x >=0 else :math:`\frac{e^x}{(1.0 + e^{x})}`
    for stability.

    Args:
        x (float): input

    Returns:
        float : sigmoid value
    """
    # TODO: Implement for Task 0.1.

    if x >= 0:
        z = math.exp(-x)
        sig = 1.0 / (1.0 + z)
        return sig
    else:
        z = math.exp(x)
        sig = z / (1.0 + z)
        return sig


def relu(x: float) -> float:
    """
    :math:`f(x) =` x if x is greater than 0, else 0
    (See `<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>`_ .)

    Args:
        x (float): input

    Returns:
        float : relu value
    """
    # TODO: Implement for Task 0.1.
    return x if x > 0.0 else 0.0


EPS = 1e-6


def log(x: float) -> float:
    ":math:`f(x) = log(x)`"
    return math.log(x + EPS)


def exp(x: float) -> float:
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def log_back(x: float, d: float) -> float:
    r"If :math:`f = log` as above, compute :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.

    return d * (1.0 / x)


def inv(x: float) -> float:
    ":math:`f(x) = 1/x`"
    # TODO: Implement for Task 0.1.

    return 1.0 / x


def inv_back(x: float, d: float) -> float:
    r"If :math:`f(x) = 1/x` compute :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.

    return d * (-1 / x**2)


def relu_back(x: float, d: float) -> float:
    r"If :math:`f = relu` compute :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.

    return 0.0 if x < 0.0 else d


# ## Task 0.3

# Small library of elementary higher-order functions for practice.


def map(
    fn: Callable[[float], float]
) -> Callable[[Iterable[float]], Iterable[float]]:
    """
    Higher-order map.

    .. image:: figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): Function from one value to one value.

    Returns:
        function : A function that takes a list, applies `fn` to each element, and returns a
        new list
    """
    # TODO: Implement for Task 0.3.
    def actual_map(lst):
        mapped_lst = [fn(x) if x != 0.0 else 0.0 for x in lst]

        return mapped_lst

    return actual_map


def negList(ls: Iterable[float]) -> Iterable[float]:
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    # TODO: Implement for Task 0.3.
    if ls == []:
        return ls
    neg_func = map(neg)
    return neg_func(ls)


def zipWith(
    fn: Callable[[float, float], float]
) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """
    Higher-order zipwith (or map2).

    .. image:: figs/Ops/ziplist.png

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (two-arg function): combine two values

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
        applying fn(x, y) on each pair of elements.

    """
    # TODO: Implement for Task 0.3.
    def map2(ls1, ls2):
        assert len(ls1) == len(ls2)
        new_list = []
        for i in range(len(ls1)):
            new_list.append(fn(ls1[i], ls2[i]))

        return new_list

    return map2


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    # TODO: Implement for Task 0.3.
    assert len(ls1) == len(ls2)
    zip_add = zipWith(add)
    return zip_add(ls1, ls2)


def reduce(
    fn: Callable[[float, float], float], start: float
) -> Callable[[Iterable[float]], float]:
    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        :math:`x_1 \ldots x_n` and computes the reduction :math:`fn(x_3, fn(x_2,
        fn(x_1, x_0)))`
    """
    # TODO: Implement for Task 0.3.
    def apply(input_list):
        my_list = list(input_list).copy()

        if len(my_list) == 0:
            return start
        current_value = my_list.pop()
        return fn(current_value, apply(my_list))

    return apply


def sum(ls: Iterable[float]) -> float:
    "Sum up a list using :func:`reduce` and :func:`add`."
    # TODO: Implement for Task 0.3.
    reduce_add = reduce(add, 0)
    return reduce_add(ls)


def prod(ls: Iterable[float]) -> float:
    "Product of a list using :func:`reduce` and :func:`mul`."
    # TODO: Implement for Task 0.3.
    reduce_mul = reduce(mul, 1)
    return reduce_mul(ls)
