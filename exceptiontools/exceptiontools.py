"""Various functions to help deal with exceptions.
Released under the MIT license (https://opensource.org/licenses/MIT).
"""


def raises(callable, args=(), kwargs={}):
    """Check if `callable(*args, **kwargs)` raises an exception.
    Returns `True` if an exception is raised, else `False`.

    Arguments:
    - callable: A callable object.

    - args: A list or tuple containing positional arguments to `callable`.
      Defaults to an empty tuple.

    - kwargs: A dictionary containing keyword arguments to `callable`.
      Defaults to an empty dictionary.
    """
    try:
        callable(*args, **kwargs)
    except Exception as exc:
        return True
    return False


def suppress(*exceptions):
    """Suppress `exceptions` when calling a function.
    If an exception is raised and it is not contained in `exceptions`,
    it is propagated back to the caller without context. If no exceptions
    are raised, return `callable(*args, **kwargs)`.

    Arguments:
    - *exceptions: The exceptions to suppress.
      All exceptions must derive from `BaseException`.

    - callable: A callable object.

    - *args: Positional arguments to `callable`.

    - **kwargs: Keyword arguments to `callable`.
    """
    def wrap(callable):
        def call(*args, **kwargs):
            try:
                return callable(*args, **kwargs)
            except exceptions:
                pass
            except Exception as exc:
                raise_from_context(exc)
        return call
    return wrap


def raise_from_context(exception, context=None):
    """Raise `exception` from `context`.
    This function is compatible with Python 2 as it sets `__context__`.

    Arguments:
    - exception: An exception (derived from `BaseException`).

    - context: The context from which to raise `exception`.
      Defaults to `None`.
    """
    exception.__context__ = context
    raise exception
