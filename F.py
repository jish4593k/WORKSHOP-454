import tkinter as tk
import torch
from tkinter import ttk
from scipy.special import factorial

class CustomToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_visible = False
        self.create_tooltip()

    def create_tooltip(self):
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry("+1000+1000")  # Place it initially out of the screen

        label = tk.Label(self.tooltip, text=self.text, justify='left',
                         background="#FFFFCC", fg='black', relief='solid', borderwidth=1,
                         padx=5, pady=5)
        label.pack()

        tensor_button = ttk.Button(self.tooltip, text="PyTorch Tensor Op", command=self.tensor_operation)
        tensor_button.pack(pady=5)

        scipy_button = ttk.Button(self.tooltip, text="Scipy Factorial", command=self.scipy_operation)
        scipy_button.pack(pady=5)

        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if not self.tooltip_visible:
            x, y, _, _ = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 20
            self.tooltip.geometry("+%d+%d" % (x, y))
            self.tooltip.deiconify()
            self.tooltip_visible = True

    def hide_tooltip(self, event=None):
        if self.tooltip_visible:
            self.tooltip.withdraw()
            self.tooltip_visible = False

    def tensor_operation(self):
       
        a = torch.tensor([1, 2, 3])
        b = torch.tensor([4, 5, 6])
        result = a + b
        tk.messagebox.showinfo("PyTorch Tensor Op", f"Tensor Operation Result: {result}")

    def scipy_operation(self):
       
        value = 5
        result = factorial(value)
        tk.messagebox.showinfo("Scipy Factorial", f"Factorial of {value}: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    button = tk.Button(root, text="Hover me")
    button.pack(padx=50, pady=50)

    tooltip = CustomToolTip(button, "Thy.")

    root.mainloop()
