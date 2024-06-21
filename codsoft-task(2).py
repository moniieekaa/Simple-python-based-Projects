import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry frame
        entry_frame = tk.Frame(self.root, bg="#333333")
        entry_frame.pack(expand=True, fill="both")

        entry = tk.Entry(entry_frame, textvariable=self.result_var, font=("Helvetica", 24), bg="#333333", fg="#FFFFFF", bd=0, justify="right")
        entry.pack(expand=True, fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # Button frame
        button_frame = tk.Frame(self.root, bg="#333333")
        button_frame.pack(expand=True, fill="both")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0, 2), (".", 4, 2), ("+", 4, 3),
            ("C", 5, 0, 2), ("=", 5, 2, 2)
        ]

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) == 4 else 1

            btn = tk.Button(button_frame, text=text, font=("Helvetica", 18), bg="#444444", fg="#FFFFFF",
                            activebackground="#666666", activeforeground="#FFFFFF", bd=0, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.result_var.set("")
        elif char == "=":
            try:
                result = eval(self.expression)
                self.result_var.set(result)
                self.expression = str(result)
            except Exception:
                self.result_var.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()