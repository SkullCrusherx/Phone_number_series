from tkinter import Tk, Label, Button, StringVar, Entry
import random
import threading

root = Tk()
root.title("Series Generator")
root.geometry('270x330')
root.resizable(False, False)
root.config(background='#35c9d4')

def generate_series():
    prefix = entry_series.get()
    quantity = entry_quantity.get()
    filename = entry_savefile.get()

    # Input validation
    try:
        quantity = int(quantity)
        if quantity <= 0:
            label.config(text="Quantity must be positive.")
            return
    except ValueError:
        label.config(text="Enter a valid number for quantity.")
        return

    if not prefix.isdigit() or len(prefix) < 3:
        label.config(text="Prefix must be numeric and at least 3 digits.")
        return

    if not filename:
        label.config(text="Filename cannot be empty.")
        return

    try:
        with open(filename + ".txt", "a") as file:
            for _ in range(quantity):
                random_number = f"{random.randint(0, 999999):06d}"
                phone_number = prefix + random_number
                file.write(phone_number + "\n")
        label.config(text=f"Saved {quantity} numbers to '{filename}.txt'")
    except Exception as e:
        label.config(text=f"Error: {e}")

def start_thread():
    threading.Thread(target=generate_series).start()

# UI elements
Label(root, text='Series Generator', background='#35c9d4', font=("Helvetica", 16), fg='#001314').pack(pady=5)

Label(root, text='Prefix (e.g., 987)', background='#35c9d4', font=("Helvetica", 10)).pack()
entry_series = Entry(root, width=20, font=("Helvetica", 14), background='#03919c', fg='#d5f3f5')
entry_series.pack(pady=5)

Label(root, text='Quantity', background='#35c9d4', font=("Helvetica", 10)).pack()
entry_quantity = Entry(root, width=20, font=("Helvetica", 14), background='#03919c', fg='#d5f3f5')
entry_quantity.pack(pady=5)

Label(root, text='Filename', background='#35c9d4', font=("Helvetica", 10)).pack()
entry_savefile = Entry(root, width=20, font=("Helvetica", 14), background='#03919c', fg='#d5f3f5')
entry_savefile.pack(pady=5)

Button(root, text='Generate', command=start_thread, width=14, font=("Helvetica", 14), background='#031ca6', fg='#d5f3f5').pack(pady=10)

label = Label(root, text="Status will appear here.", background='#35c9d4', font=("Helvetica", 10))
label.pack(pady=5)

root.mainloop()
