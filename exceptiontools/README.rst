Exception tools
===============

This module aims to serve as a handy toolkit for working with exceptions.

Functions
---------
* ``raises(callable, args=(), kwargs={})``: Check if calling ``callable(*args, **kwargs)`` raises an exception.
  Returns ``True`` if an exception is caught, else ``False``. The return value of the call will be lost.
 
  .. code-block:: python
  
     >>> def raise_runtime_error():
     ...    raise RuntimeError("Yikes!")
     ...    
     >>> def dont_raise():
     ...    return
     ...
     >>> raises(raise_runtime_error)
     True
     >>> raises(dont_raise)
     False
     
          
* ``suppress(*exceptions)``: Function decorator. Suppress all exceptions listed in ``*exceptions``. All other
  exceptions are propagated back to the caller. If no exceptions are caught, return the return value of the call.
  
  .. code-block:: python
  
     >>> @suppress(TypeError)
     ... def raise_type_error():
     ...    raise TypeError("Ouch!")
     ...
     >>> @suppress(TypeError)
     ... def raise_value_error():
     ...    raise ValueError("Eek!")
     ...
     >>> raise_type_error()
     >>> raise_value_error()
     Traceback (most recent call last):
     ...
     ValueError: Eek!
           
* ``raise_from_context(exception, context=None)``: Raise ``exception`` from ``context``. ``raise_from_context`` is backwards
  compatible with Python 2.
  
  .. code-block:: python

     >>> context = IndexError("Out of bounds!")
     >>> exception = RuntimeError("Something went wrong...")
     >>>
     >>> raise_from_context(exception)
     Traceback (most recent call last):
     ...
      
     >>> raise_from_context(exception, context)
     IndexError: Out of bounds!

     During handling of the above exception, another exception occurred:

     Traceback (most recent call last):
     ...
     RuntimeError: Something went wrong...






