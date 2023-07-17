from tkinter import *

def convert(unit1, unit2, value):
  """Converts a value from one unit to another.

  Args:
    unit1: The original unit.
    unit2: The target unit.
    value: The value to convert.

  Returns:
    The converted value.
  """

  conversion_rates = {
    "volts": 1,
    "amperes": 1,
    "watts": 1,
    "ohms": 1,
    "farads": 1,
    "henries": 1,
    "siemens": 1,
    "webers": 1,
    "joules": 1,
    "watts": 1,
  }

  return value * conversion_rates[unit1] / conversion_rates[unit2]

def main():
  """The main function of the program.

  Creates a Tkinter window and adds a label, an entry box, and a button.
  The label displays the current unit, the entry box allows the user to enter a value,
  and the button converts the value to the target unit.
  """

  window = Tk()
  window.title("Electricity Unit Converter")

  label = Label(window, text="Current Unit:")
  entry_box = Entry(window)
  button = Button(window, text="Convert", command=convert)

  label.pack()
  entry_box.pack()
  button.pack()

  window.mainloop()

if __name__ == "__main__":
  main()