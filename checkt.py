import tkinter as tk
from tkinter.simpledialog import Dialog

class BuySellDialog(Dialog):
    def body(self, master):
        self.title("Question")
        tk.Button(master, text="Buy", command=self.buy).pack()
        tk.Button(master, text="Sell", command=self.sell).pack()
        return None

    def buy(self):
        self.result = "Buy"
        self.destroy()

    def sell(self):
        self.result = "Sell"
        self.destroy()

root = tk.Tk()
root.withdraw()  # Hide the main window

dialog = BuySellDialog(root)
print(f"You selected {dialog.result}.")

root.mainloop()