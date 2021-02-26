from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title('Convert Miles to Km')
window.minsize(width=200, height=120)
window.config(padx=50, pady=50)


def miles_to_km():
    miles = float(miles_entry.get())
    km = round(miles * 1.609)
    result_label.config(text=f'{km}')


# Labels
miles_label = Label(text='Mile(s)')
miles_label.grid(row=1, column=3)

equal_label = Label(text='is equal to')
equal_label.grid(row=2, column=1)

km_label = Label(text='Km')
km_label.grid(row=2, column=3)

result_label = Label(text='0')
result_label.grid(row=2, column=2)

# Entry
miles_entry = Entry(width=10, text='0')
miles_entry.grid(row=1, column=2)

# Button
button = Button(text='Calculate', command=miles_to_km)
button.grid(row=3, column=2)

window.mainloop()
