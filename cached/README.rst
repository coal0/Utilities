Cached
======

A little utility library for caching class data.

This tiny library consists of the two functions ``cached()`` and ``auto_cached()``.
The functions are used as wrappers around class methods returning some form of data
that may be cached. Take a look:

.. code:: python

  from cached import cached
  
  
  class String:
    def __init__(self, s):
      self._s = s
    
    @cached("_stripped_string")
    def stripped(self):
      return self._s.strip()

What the ``cached()`` decorator does is:

1. Check if the name '_stripped_string' is already an existing attribute of the class;
2. If it is not, assign the return value of ``String.stripped()`` to ``String._stripped_string``;
3. Return ``String._stripped_string`` (which is now guaranteed to exist).

That's the crux of it.

If you prefer anonymous caching (i.e. without providing a name yourself), use
``auto_cached()``:

.. code:: python

  from cached import auto_cached
  
  
  class String:
    def __init__(self, s):
      self._s = s
    
    @auto_cached
    def capitalized(self):
      return self._s.capitalize()

Should you feel uncomfortable using ordinary methods for data access, don't worry, as
``property`` will work great too.
