import tkinter as tk

def evaluate():
    x = int(entry1.get())
    y = int(entry2.get())
    result = f"""
x < y : {x < y}
x > y : {x > y}
x <= y : {x <= y}
x >= y : {x >= y}
x == y : {x == y}
x != y : {x != y}
"""
    label_result.config(text=result)

root = tk.Tk()
root.title("Relational Expression Evaluator")

tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Evaluate", command=evaluate).pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()