import tkinter as tk

window = tk.Tk()
window.title("Multiplication Factory")
window.rowconfigure([0, 1], minsize = 50, weight = 1)
window.columnconfigure([0,1,2,3,4], minsize = 50, weight = 1)

def set():
    number = int(numberEntry.get())
    timesLabel["text"] = number
    valueLabel["text"] = number
    countLabel["text"] = "1"
    numberEntry.delete(0, tk.END)


def decrease():
    times = int(timesLabel["text"])
    count = int(countLabel["text"])
    if count == 0:
        countLabel['text']= f"{count}"
    else:
        countLabel['text']= f"{count - 1}"
    value = int(valueLabel["text"])
    if value == 0:
        valueLabel["text"] = f"{value}"
    else:
        valueLabel["text"] = f"{value - times}"

def increase():
    times = int(timesLabel["text"])
    count = int(countLabel["text"])
    countLabel["text"] =f"{count + 1}"
    value = int(valueLabel["text"])
    valueLabel["text"] = f"{value + times}"



numberLabel = tk.Label(master=window, text="Number")
numberLabel.grid(row=0, column=0, sticky="nsew")

numberEntry = tk.Entry()
numberEntry.grid(row=0, column=1, columnspan=3, sticky="nsew")

setButton =tk.Button(master=window, text="set", command = set)
setButton.grid(row=0, column=4, sticky= 'nsew')

decreaseButtton = tk.Button(master = window, text = "-", bg="#ff3333", command = decrease)
decreaseButtton.grid(row=1, column=0, sticky= 'nsew')

increaseButton = tk.Button(master = window, text = "+", bg="#33ff33", command = increase)
increaseButton.grid(row=1, column=4, sticky="nsew")

valueLabel = tk.Label(master = window, text = "0")
valueLabel.grid(row=1, column=3, sticky="nsew")

countLabel = tk.Label(master = window, text = "0")
countLabel.grid(row=1, column=2, sticky="nsew")

timesLabel = tk.Label(master = window, text = "0")
timesLabel.grid(row=1, column=1, sticky="nsew")

window.mainloop()
