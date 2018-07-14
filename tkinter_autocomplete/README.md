## Tkinter Autocomplete

Text autocompletion provides relevant real-time results to users.
Because tkinter does not provide a widget for adding autocompletion to GUIs out of the box,
I decided to make one myself. This utility is compatible with and has been tested on Python 2.7.1 and Python 3.6.0.<br />

References:
* Read the **license** [here](https://github.com/Coal0/Utilities/blob/master/LICENSE)<br />
* Play around with the **demo** [here](https://github.com/Coal0/Utilities/blob/master/tkinter_autocomplete/demo.py)

### Structure

###### NOTE: The `Tkinter` library for Python 2 and `tkinter` library for Python 3 will from now on be referred to as `tk`.

The `AutocompleteEntry` class (which can be found [here](https://github.com/Coal0/Utilities/blob/master/tkinter_autocomplete/main.py))
derives from `tk.Frame` and is a container used to group a `tk.Entry` and `tk.Listbox` widget. Should you need to modify the widgets,
they can be accessed as (respectively) `AutocompleteEntry` s `entry` and `listbox` attributes.<br />

The entry widget acts like a normal textbox. When activated, it binds `<KeyRelease>` to a private method which will update
the list of suggestions. The listbox widget contains the suggestions themselves. When activated, it binds `<<ListboxSelect>>` to a
private method which sets the entry widget to whatever value was selected.<br />

Since an instance of `AutocompleteEntry` is a `tk.Frame` instance too, you can place it by calling its `pack` or `grid` methods with
their respective arguments.

### Quickstart

###### NOTE: These examples will only run under Python 3. To make them Python 2-compatible, replace `tkinter` with `Tkinter`.

To add a new autocompletion frame to our interface, first initialize one:

```python
import tkinter as tk

from main import AutocompleteEntry

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

entry = AutocompleteEntry(frame)
# You can pass additional parameters to further customize the window;
# all parameters that you can pass to tk.Frame, are valid here too.
```

Now you need to configure the instance by passing it an iterable containing all autocompletion entries.<br />
Do this by calling its `build` method:

```python
ENTRIES = (
    "Foo",
    "Bar"
)

entry.build(ENTRIES)
```

You can pass additional arguments to `build`:

* `max_entries` (integer):<br />
  The maximum number of entries to display at once. This value directly corresponds to the listbox widget's `height` attribute. Defaults to `5`.

* `case_sensitive` (boolean):<br />
  If `True`, only autocomplete entries that enforce the same capitalization as the current entry will be displayed.<br />
  If `False`, all autocomplete entries that match with the current entry will be displayed.<br />
  Defaults to `False`.

* `no_results_message` (string or `None`):<br />
  The message to display if no suggestions could be found for the current entry.<br />
  This argument may include a formatting identifier (`{}`) which, at runtime, gets formatted as the current entry. If `None` is specified, the listbox will instead be hidden until the next `<KeyRelease>` event.
  
Let's play around with these arguments:

```python
entry.build(
    entries=ENTRIES,
    no_results_message="< No results found for '{}' >"
    # Note that this is formatted at runtime
)
```

###### NOTE: You may call the `build` method multiple times on an instance of `AutocompleteEntry`, to dynamically change the available suggestions.

With that out of the way, you can display `entry`:

```python
entry.pack()
```

Now, each time a user presses a key while the entry widget has focus, a list of suggestions will display below it.

---

### Additional options

By default, the `tk.Listbox` widget has a width of `25` pixels and a height of `5` (items). The `tk.Entry` widget also has a default width of `25` pixels. These settings can be modified through the following class attributes:

* `AutocompleteEntry.LISTBOX_HEIGHT`: The height to specify when creating the `tk.Listbox` widget. There's no need to modify this, since the maximum number of entries to be displayed can be passed as an argument to `build`.

* `AutocompleteEntry.LISTBOX_WIDTH`: The width to specify when creating the `tk.Listbox` widget. Any positive integer is valid.

* `AutocompleteEntry.ENTRY_WIDTH`: The width to specify when creating the `tk.Entry` widget. Any positive integer is valid.

###### NOTE: You almost always want to keep the 1:1 `LISTBOX_WIDTH`:`ENTRY_WIDTH` ratio.

You can retrieve the current entry by accessing the instance's `text` attribute (which is a `tk.StringVar` instance):

```python
text = entry.text.get()
```

To further customize the entry widget, you may set its font options, for example:

```python
entry.entry["font"] = (<FONT NAME>, <FONT SIZE>, <FONT WEIGHT>)
```

Or to change the background color for the listbox widget:

```python
entry.listbox["background"] = "#cfeff9"
# Light blue
```

For a demonstration of this utility, check out [the demo](#tkinter-autocomplete).
