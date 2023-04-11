import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = tk.Label(self.master, textvariable=self.result_var, font=("Arial", 20), width=20, height=2, bd=5, bg="#EEE")
        self.result_label.grid(row=0, column=0, columnspan=4)

        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        self.buttons = []
        for i, text in enumerate(button_texts):
            button = tk.Button(self.master, text=text, font=("Arial", 20), width=4, height=2, bd=5, bg="#DDD")
            button.grid(row=(i//4)+1, column=i%4)
            self.buttons.append(button)
            button.config(command=lambda button=button: self.handle_button_click(button))

        self.master.bind("<Return>", lambda event: self.handle_button_click(self.buttons[-2]))

    def handle_button_click(self, button):
        button_text = button.cget("text")
        result_text = self.result_var.get()
        if button_text == "=":
            try:
                result_text = str(eval(result_text))
            except ZeroDivisionError:
                result_text = "Error: Division by zero"
            except:
                result_text = "Error: Invalid input"
        elif button_text == "C":
            result_text = "0"
        elif button_text == "CE":
            result_text = result_text[:-1] if len(result_text) > 1 else "0"
        elif button_text == "±":
            result_text = str(float(result_text) * -1)
        elif button_text == ".":
            if "." not in result_text:
                result_text += "."
        else:
            if result_text == "0":
                result_text = ""
            result_text += button_text
        self.result_var.set(result_text)

root = tk.Tk()
app = Calculator(master=root)
app.mainloop()
