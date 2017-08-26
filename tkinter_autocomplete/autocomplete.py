try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    # Python 2
    import Tkinter as tk
    import ttk

__all__ = ["Autocomplete"]

NO_RESULTS_MESSAGE = "No results found for '{}'"


def _longest_common_substring(s1, s2):
    """Get the longest common substring for two strings.
    Source: https://goo.gl/k64S4f
    """
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


class Autocomplete(tk.Frame, object):
    """An autocomplete object is a container for tk.Entry and tk.Listbox
    widgets. Together, these widgets can provide end users with relevant
    results (autocomplete entries). 

    Methods defined here:
    __init__(): The init method initializes a new tk.Frame object, as
                well as the tk.Entry and tk.Listbox widgets. These can
                be modified by accessing respectively
                `Autocomplete.entry_widget` and
                `Autocomplete.listbox_widget`.
    
    build(): The build method sets up the autocompletion settings for
             the tk.Entry widget. It is mandatory to call build()
             to be able to display the frame.
    
    _update_autocomplete(): The _update_autocomplete method evaluates
                            whatever the tk.Entry widget contains and
                            updates the tk.Listbox widget to display
                            relevant matches. It is called on
                            <KeyRelease> and should never be called
                            explicitly.

    _select_entry(): The _select_entry method replaces the textvariable
                     connected to the tk.Entry widget with the current
                     listbox selection. It is called on
                     <<ListboxSelect>> and should never be called
                     explicitly.
    
    Constants defined here:

    DEFAULT_LISTBOX_HEIGHT: The default 'height' attribute for the
                            tk.Listbox widget. This value directly
                            corresponds to the maximum amount of results
                            shown in the tk.Listbox widget at once.
                            Note that the user may view more results
                            by scrolling vertically.
                            --- DEFAULT = 5 ---
    
    DEFAULT_LISTBOX_WIDTH: The default 'width' attribute for the
                           tk.Listbox widget. This value directly
                           corresponds to the maximum amount of
                           characters shown per result at once.
                           Note that the user may view more characters
                           by scrolling horizontally.
                           --- DEFAULT = 25 ---
    
    DEFAULT_ENTRY_WIDTH: The default 'width' attribute for the tk.Entry
                         widget.
                         --- DEFAULT = 25 ---
    """

    DEFAULT_LISTBOX_HEIGHT = 5
    DEFAULT_LISTBOX_WIDTH = 25
    DEFAULT_ENTRY_WIDTH = 25

    def __init__(self, *args, **kwargs):
        """Constructor.
        Initialize a new tk.Frame object and create a tk.Entry and
        tk.Listbox widget for later configuration.

        ---

        Arguments:
        All arguments passed here will be directly passed to a new
        tk.Frame instance. For further help:

            >>> help(tk.Frame)

        ---

        Example:
            >>> autocomplete = Autocomplete(tk.Root())
            >>> autocomplete["width"] = 50
            >>> # Corresponds to tk.Frame["width"]

        ---

        Returns:
        None
        """

        super(Autocomplete, self).__init__(*args, **kwargs)
        self.text = tk.StringVar()
        self.entry_widget = tk.Entry(
            self,
            textvariable=self.text,
            width=self.DEFAULT_ENTRY_WIDTH
        )
        self.listbox_widget = tk.Listbox(
            self,
            height=self.DEFAULT_LISTBOX_HEIGHT,
            width=self.DEFAULT_LISTBOX_WIDTH
        )

    def build(self, entries, match_exact=False, case_sensitive=False,
              no_results_message=NO_RESULTS_MESSAGE):
        """Set up the tk.Entry and tk.Listbox widgets.

        ---

        Arguments:
        * entries: [iterable] Autocompletion entries.

        * match_exact: [bool] Treat only entries that start with
                              the current entry as matches.
                              If False, select the most relevant results
                              based on the length of the longest common
                              substring (LCS).
                              Defaults to False.

        * case_senstive: [bool] Treat only entries with the exact same
                                characters as matches. If False, allow
                                capitalization to be mixed.
                                Defaults to False.

        * no_results_message: The message to display if no matches
                              could be found for the current entry.
                              May include a formatting key to display
                              the current entry. If None, the tk.Listbox
                              widget will be hidden until the next
                              <KeyRelease> event.

        ---

        Example:

            >>> autocomplete = Autocomplete(tk.Root())
            >>> autocomplete.build(
            ...     entries=["Foo", "Bar"],
            ...     case_sensitive=True,
            ...     no_results_message="<No results for '{}'>"
            ... )

        ---

        Returns:
        None
        """
        if not case_sensitive:
            entries = list(map(
                lambda entry: entry.lower(), entries
            ))

        self._case_sensitive = case_sensitive
        self._entries = entries
        self._match_exact = match_exact
        self._no_results_message = no_results_message

        self.entry_widget.bind("<KeyRelease>", self._update_autocomplete)
        self.entry_widget.focus_set()
        self.entry_widget.grid(column=0, row=0)

        self.listbox_widget.bind("<<ListboxSelect>>", self._select_entry)
        self.listbox_widget.grid(column=0, row=1)
        self.listbox_widget.grid_forget()

    def _update_autocomplete(self, event):
        """Update the tk.Listbox widget to display new matches.

        Do not call explicitly.
        """
        self.listbox_widget.delete(0, tk.END)
        self.listbox_widget["height"] = self.DEFAULT_LISTBOX_HEIGHT

        text = self.text.get()
        if not self._case_sensitive:
            text = text.lower()
        if not text:
            self.listbox_widget.grid_forget()
        elif not self._match_exact:
            matches = {}
            for entry in self._entries:
                lcs = len(_longest_common_substring(text, entry))
                # if lcs >= 2:
                if lcs:
                    matches[entry] = lcs
            sorted_items = sorted(list(matches.items()),
                                  key=lambda match: match[1])
            for item in sorted_items[::-1]:
                self.listbox_widget.insert(tk.END, item[0])
        else:
            for entry in self._entries:
                if entry.strip().startswith(text):
                    self.listbox_widget.insert(tk.END, entry)

        listbox_size = self.listbox_widget.size()
        if not listbox_size:
            if self._no_results_message is None:
                self.listbox_widget.grid_forget()
            else:
                try:
                    self.listbox_widget.insert(
                        tk.END,
                        self._no_results_message.format(text)
                    )
                except UnicodeEncodeError:
                    self.listbox_widget.insert(
                        tk.END,
                        self._no_results_message.format(
                            text.encode("utf-8")
                        )
                    )
                if listbox_size <= self.listbox_widget["height"]:
                    # In case there's less entries than the maximum
                    # amount of entries allowed, resize the listbox.
                    self.listbox_widget["height"] = listbox_size
                self.listbox_widget.grid()
        else:
            if listbox_size <= self.listbox_widget["height"]:
                self.listbox_widget["height"] = listbox_size
            self.listbox_widget.grid()

    def _select_entry(self, event):
        """Set the textvariable corresponding to self.entry_widget
        to the value currently selected.

        Do not call explicitly.
        """
        widget = event.widget
        value = widget.get(int(widget.curselection()[0]))
        self.text.set(value)
