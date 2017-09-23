try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    # Python 2
    import Tkinter as tk
    import ttk

from main import AutocompleteEntry
from main import NO_RESULTS_MESSAGE

COUNTRIES = open("countries.txt").read().split("\n")


class Application(tk.Frame, object):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        label = tk.Label(self, text="Select a country: ")
        label.pack()

        self.entry = AutocompleteEntry(self)
        self.build(case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
        self.entry.pack(after=label)

        self.nr = tk.StringVar()
        tk.Label(
            self,
            text="\n\nAlternative message (<Return> to set): "
        ).pack()
        nr = tk.Entry(self, textvariable=self.nr)
        nr.pack()
        nr.bind("<Return>", self._update)

        self.cs = tk.StringVar()
        cb = tk.Checkbutton(
            self,
            text="Case sensitive",
            variable=self.cs,
            state="normal",
            command=self._update
        )
        cb.deselect()
        cb.pack()

    def _update(self, *args):
        case_sensitive = False
        if self.cs.get() == "1":
            case_sensitive = True
        no_results_message = self.nr.get()
        self.build(
            case_sensitive=case_sensitive,
            no_results_message=no_results_message
        )

    def build(self, *args, **kwargs):
        self.entry.build(
            COUNTRIES,
            kwargs["case_sensitive"],
            kwargs["no_results_message"]
        )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("DEMO")
    root.resizable(False, False)
    root.tk_setPalette("white")

    application = Application(root)
    application.pack()

    root.mainloop()
