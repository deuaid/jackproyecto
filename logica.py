from tkinter import *

def convert(unit1, unit2, value):
 

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


  window = Tk()
  window.title("CONVERTIDOR DE UNIDADES ELECTRICAS")

  label = Label(window, text="Current Unit:")
  entry_box = Entry(window)
  button = Button(window, text="Convert", command=convert)

  label.pack()
  entry_box.pack()
  button.pack()

  window.mainloop()

if __name__ == "__main__":
  main()