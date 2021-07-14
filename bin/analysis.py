"""
This is the module docstring.

Here is where you should put any overarching documentation about your script,
particularly for folks that will be looking at the code.

This module provides an inefficient means to calculate a total when provided
a collection of integers.
"""
import sys # So we can write to stdout
import time # Record start and end times.
import logging  # Use the logging module for logging messages.
from argparse import ArgumentParser # The standard library for building CLIs.


def add(x, y=None):
    """Add two integers.

    This is the function docstring. It should contain details about what the
    function does, its parameters (inputs), and what it returns (if anything).
    There are several standard formats, but this one follows the numpy
    docstring style.

    These docstrings can be turned into a webpage using Sphinx and can
    incorporate ReStructured Text (ReST) directives. For example, here are the
    links to the `numpy docstring documentation
    <https://numpydoc.readthedocs.io/en/latest/format.html>`_ and the `Sphinx
    documentation <https://www.sphinx-doc.org/en/master/>`_

    Parameters
    ----------
    x : int
        The first integer to add.
    y : int, optional
        The second integer to add. If ``None``, ``x`` is added to itself.

    Returns
    -------
    int
        The sum of ``x`` and ``y``.
    """
    if y is None:
        y = x

    return int(x) + int(y)


def total(integers):
    """Calculate the sum of a collection of integers.

    Parameters
    ----------
    integers : iterable of int
        The integers we want to sum.

    Returns
    -------
    int
        The sum of all the values in ``integers``.
    """
    running_total = 0
    for num in integers:
        running_total = add(running_total, num)

    return running_total


def main():
    """Calculate the sum of integers from the commmand line.

    This function parses our command line arguments.
    """
    # Record the start time:
    start = time.time()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    # Build our command line interface:
    parser = ArgumentParser(description="Sum a collection of integers.")
    parser.add_argument(
        "integers",
        type=int,
        nargs="+",
        help="The integers we want to sum."
    )

    # Parse the arguments:
    args = parser.parse_args()

    # Log a message:
    logging.info("Calculating sum of %s", str(args.integers))

    # Calculate the sum:
    result = total(args.integers)

    # Log the run time:
    logging.info("Finished in %fs.", time.time()-start)

    # Write the total to stdout
    print(result, file=sys.stdout)


# Define the behaviour when running from the commmand line:
if __name__ == "__main__":
    main()


# Add some tests to the end.
# Pytest will automatically detect functions that start with `test``
# Note that these could be expanded to be better!
def test_add():
    """Test that the ``add()`` function works as expected"""
    assert add(2, 1) == 3
    assert add(2.1, 1.2) == 3
    assert add("2", "1") == 3
    assert add(1) == 2


def test_total():
    """Test that the ``total()`` function works as expected"""
    assert total([1, 2, 3]) == 6
    assert total((1, 2, 3)) == 6
    assert total("123") == 6
