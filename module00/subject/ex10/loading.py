"""
A script to demonstrate a custom progress bar function using tqdm.

This module provides a generator function, ft_progress, which wraps any
iterable to display a progress bar during iteration. It also includes a main
function to show an example of its usage.
"""

import time
import tqdm


def ft_progress(lst):
    """
    Function-generator, that cover iteratible object in tqdm and returns
    their elements.
    
    Args:
        lst: (Iterable): The iterable object (e.g., a list, range, etc.)
        to iterate over.

    Yields:
        Any: The next element from the input iterable.
    """
    for item in tqdm.tqdm(lst):
        yield item


def main():
    """
    Simply initialize a range of numbers and iterates through them using the
    ft_progress() func. During the loop it provides a simple calculation on
    each element to simulate work and finaly prints the final result.
    """
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(f"Result: {ret}")


if __name__ == "__main__":
    main()
