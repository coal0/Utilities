## Tkinter Autocomplete

Text autocompletion provides relevant real-time results to users.
Because tkinter does not provide an easy 'set it and forget it' widget for adding autocompletion to GUI's,
I decided to make one myself. This utility is compatible with and has been tested on Python 2.7.1 and Python 3.6.0.<br />

References:
* Read the **license** [here](https://github.com/Coal0/Utilities/blob/master/LICENSE)<br />
* Play around with the **demo** [here](https://github.com/Coal0/Utilities/blob/master/tkinter_autocomplete/demo.py)

### Structure

###### NOTE: The `Tkinter` library for Python 2 and `tkinter` library for Python 3 will henceforth be referred to as `tk`.

The `Autocomplete` class (which can be found [here](https://github.com/Coal0/Utilities/blob/master/tkinter_autocomplete/autocomplete.py))
derives from `tk.Frame` and is a container used to group a `tk.Entry` and `tk.Listbox` widget. Should we need to modify the widgets,
they can be accessed as (respectively) `Autocomplete` s `entry_widget` and `listbox_widget` attributes.<br />

The entry widget acts like a normal textbox. When activated, it binds `<KeyRelease>` to a private method which will update
the list of suggestions. The listbox widget contains the suggestions themselves. When activated, it binds `<<ListboxSelect>>` to a
private method which `set` s the entry widget to whatever value was selected.<br />

Since an instance of `Autocomplete` is a `tk.Frame` instance too, we can place it by calling its `pack()` or `grid()` methods with
their respective arguments.

### Quickstart

###### NOTE: These examples will only run under Python 3. To make them Python 2-compatible, replace `tkinter` with `Tkinter`.


To add a new Autocomplete frame to our interface, first initialize one:

```python
import tkinter as tk

from autocomplete import Autocomplete

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

autocomplete_frame = Autocomplete(frame)
```

Now we need to configure the instance by passing it an iterable containing all autocomplete-entries.<br />
We do this by calling its `build()` method:

```python
ENTRIES = (
    "Foo",
    "Bar"
)

autocomplete_frame.build(ENTRIES)
```

We can pass additional arguments to `build()`:

* `match_exact` (boolean):<br />
  If `True`, only autocomplete entries that start with the current entry will be displayed.<br />
  If `False`, the most relevant results will be shown depending on the length of the
  [longest common substring](https://en.wikipedia.org/wiki/Longest_common_substring_problem).<br />
  Defaults to `False`.

* `case_sensitive` (boolean):<br />
  If `True`, only autocomplete entries that enforce the same capitalization as the current entry will be displayed.<br />
  If `False`, all autocomplete entries that match according to the rules defined in correspondence with the `match_exact` argument.<br />
  Defaults to `False`.

* `no_results_message` (string or None):<br />
  The message to display if no suggestions could be found for the current entry.<br />
  This argument may include a 'formatting key' (`{}`) which, during runtime, gets formatted as the current entry.<br />
  If `None` is specified, the listbox will instead be hidden until the next `<KeyRelease>` event.
  
Let's play around with these arguments:

```python
autocomplete_frame.build(
    entries=ENTRIES,
    no_results_message="< No results found for '{}' >"
    # Note that this is formatted at runtime
)
```

###### NOTE: We may call the `build()` method multiple times on an instance of `Autocomplete`.

Now that we have that out of the way, we can simply display the `autocomplete_frame` frame by calling its `pack()` method:

```python
autocomplete_frame.pack()
```

Now, each time a user presses a key while the entry widget has focus, a list of suggestions will display below it.

---

We can retrieve the current entry by accessing the instance's `text` attribute (which is a `tk.StringVar()` instance):

```python
text = autocomplete_frame.text.get()
```

To further customize the entry widget, we may set its font options, for example:

```python
autocomplete_frame.entry_widget["font"] = (<FONT NAME>, <FONT SIZE>, <FONT WEIGHT>)
```

Or to change the background color for the listbox widget:

```python
autocomplete_frame.listbox_widget["background"] = "#cfeff9"
# Light blue
```

For a demonstration of this utility, check out [the demo](#tkinter-autocomplete).
