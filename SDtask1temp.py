import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, OptionMenu

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        # Set background color
        self.root.configure(bg="white")

        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the x and y coordinates for the Tk root window
        x_coordinate = int((screen_width/2) - (650/2))  # 400 is the width of the window
        y_coordinate = int((screen_height/2) - (400/5))  # 400 is the height of the window

        # Set the window size and position
        self.root.geometry(f"650x400+{x_coordinate}+{y_coordinate}")

        self.title_label = Label(root, text="Temperature Converter", font=("Helvetica", 16, "bold"), bg="#F0F0F0")
        self.title_label.pack(pady=10)

        self.temperature_label = Label(root, text="Temperature:", font=("Helvetica", 12), bg="#F0F0F0")
        self.temperature_label.pack(pady=10)

        self.temperature_entry = Entry(root, font=("Helvetica", 12))
        self.temperature_entry.pack(pady=10)

        self.unit_label = Label(root, text="Unit:", font=("Helvetica", 12), bg="#F0F0F0")
        self.unit_label.pack(pady=10)

        self.unit_var = StringVar()
        self.unit_var.set("Celsius")  # Default value
        self.unit_menu = OptionMenu(root, self.unit_var, "Celsius", "Fahrenheit", "Kelvin")
        self.unit_menu.pack(pady=10)

        self.result_var = StringVar()
        self.result_label = Label(root, textvariable=self.result_var, font=("Helvetica", 12), bg="#F0F0F0")
        self.result_label.pack(pady=10)

        self.convert_button = Button(root, text="Convert", command=self.convert_temperature, font=("Helvetica", 12, "bold"), bg="blue", fg="white")
        self.convert_button.pack(pady=20)

    def convert_temperature(self):
        try:
            temperature = float(self.temperature_entry.get())
            unit = self.unit_var.get().lower()

            if unit == 'celsius':
                fahrenheit = celsius_to_fahrenheit(temperature)
                kelvin = celsius_to_kelvin(temperature)
                result = f"{temperature} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin."
            elif unit == 'fahrenheit':
                celsius = fahrenheit_to_celsius(temperature)
                kelvin = fahrenheit_to_kelvin(temperature)
                result = f"{temperature} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius and {kelvin:.2f} Kelvin."
            elif unit == 'kelvin':
                celsius = kelvin_to_celsius(temperature)
                fahrenheit = kelvin_to_fahrenheit(temperature)
                result = f"{temperature} Kelvin is equal to {celsius:.2f} degrees Celsius and {fahrenheit:.2f} degrees Fahrenheit."
            else:
                result = "Invalid unit of measurement. Please select Celsius, Fahrenheit, or Kelvin."

            self.result_var.set(result)
        except ValueError:
            self.result_var.set("Invalid input. Please enter a valid number for temperature.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
