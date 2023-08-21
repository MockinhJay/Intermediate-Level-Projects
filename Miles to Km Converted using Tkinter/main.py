from tkinter import *

is_miles_to_km = True


def miles_to_km():
    value = number_input.get()
    if is_miles_to_km:
        converted_value = round(float(value) * 1.609)
    else:
        converted_value = round(float(value) / 1.609)
    results_label.config(text=f"{converted_value}")
    number_input.delete(0, END)


def reverse_calculation():
    global is_miles_to_km
    is_miles_to_km = not is_miles_to_km
    if is_miles_to_km:
        miles_label.config(text="Miles")
        kilometer_label.config(text="Km")
        calculate_button["command"] = miles_to_km
    else:
        miles_label.config(text="Km")
        kilometer_label.config(text="Miles")
        calculate_button["command"] = miles_to_km
    results_label.config(text="0")
    number_input.delete(0, END)


window = Tk()
window.title("Converter")
window.config(padx=30, pady=30)

number_input = Entry(width=7)
number_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

results_label = Label(text="0")
results_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

reverse_calculation_button = Button(text="Reverse", command=reverse_calculation)
reverse_calculation_button.grid(column=1, row=3)

window.mainloop()

