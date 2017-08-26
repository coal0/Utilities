try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    # Python 2
    import Tkinter as tk
    import ttk

from autocomplete import Autocomplete
from autocomplete import NO_RESULTS_MESSAGE

COUNTRIES = open("countries.txt").read().split("\n")


class Application:
    def __init__(self, master):
        self.frame = ttk.Frame(master)
        self.frame.grid(column=0, row=0)

        label = ttk.Label(
            self.frame,
            text="Select a country: "
        )
        label.pack()

        self.autocomplete = Autocomplete(self.frame)
        self.build_autocomplete(
            case_sensitive=False,
            match_exact=False,
            no_results_message=NO_RESULTS_MESSAGE
        )

        self.case_sensitive = tk.StringVar()
        ttk.Checkbutton(
            self.frame,
            text="Case sensitive",
            variable=self.case_sensitive,
            command=self._update,
        ).pack(anchor="w")

        self.match_exact = tk.StringVar()
        ttk.Checkbutton(
            self.frame,
            text="Match exact entries",
            variable=self.match_exact,
            command=self._update,
        ).pack(anchor="w")

        subframe = ttk.Frame(self.frame)
        subframe.pack()

        self.no_results = tk.StringVar()
        ttk.Label(
            subframe,
            text="Alternative message (<Return> to set)"
        ).grid(column=0, row=0)

        no_results = ttk.Entry(
            subframe,
            textvariable=self.no_results
        )
        no_results.grid(column=1, row=0)
        no_results.bind("<Return>", self._update)

    def _update(self, *args):
        case_sensitive = False
        if self.case_sensitive.get() == "1":
            case_sensitive = True
        match_exact = False
        if self.match_exact.get() == "1":
            match_exact = True
        no_results_message = self.no_results.get()
        self.build_autocomplete(
            case_sensitive=case_sensitive,
            match_exact=match_exact,
            no_results_message=no_results_message
        )

    def build_autocomplete(self, *args, **kwargs):
        self.autocomplete.build(
            COUNTRIES,
            kwargs["match_exact"],
            kwargs["case_sensitive"],
            kwargs["no_results_message"]
        )
        self.autocomplete.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("DEMO")
    root.resizable(False, False)

    application = Application(root)

    root.mainloop()
