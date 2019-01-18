# convertfv2.py
# A program to convert Fahrenheit temps to Celsius
# by: Macauley Tosi

def main():
    print("Hello and welcome to the Fahrenheit Calculator")
    Fahrenheit = eval(input("What is the Fahrenheit temp? "))
    Celsius = (Fahrenheit - 32) * .5556
    print("The temperature is", Celsius, "degrees Celsius.")
    input("Press the <Enter> key to quit.")
main()
