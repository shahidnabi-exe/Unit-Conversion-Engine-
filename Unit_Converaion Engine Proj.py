print("    ")
print(" ===============  Welcome to Universal Unit Conversion Engine (Project):- ==========================  ")
print("   ")

def convert_units():
    """
    Converts between different units of measurement.
    """

    while True:
        print("   Available conversions: ")
        print(" 1. Temperature")
        print(" 2. Distance")
        print(" 3. Weight")
        print(" 4. Currency")
        print(" 5. Length")
        print("6.Gpa")       
        print(" 7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "7":
            break

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue

        if choice not in range(1, 7):
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            convert_temperature()
        elif choice == 2:
            convert_distance()
        elif choice == 3:
            convert_weight()
        elif choice == 4:
            convert_currency()
        elif choice== 5:
            convert_length()
        elif choice== 6:
            convert_gpa()
        
def convert_temperature():
    """
    Converts between Celsius and Fahrenheit.
    """

    unit_from = input("Enter the unit you're converting from (Celsius or Fahrenheit): ").lower()
    value = float(input("Enter the value to convert: "))

    if unit_from == "celsius" or unit_from =="c":
        result = value * 9/5 + 32
        print(f"{value} Celsius is equal to {result:.2f} Fahrenheit")
    elif unit_from == "fahrenheit" or unit_from =="f":
        result = (value - 32) * 5/9
        print(f"{value} Fahrenheit is equal to {result:.2f} Celsius")
    else:
        print("Invalid unit. Please try again.")

def convert_distance():
    """
    Converts between kilometers, miles, centimeters and meters .
    """

    unit_from = input("Enter the unit you're converting from (kilometers or miles): ").lower()
    value = float(input("Enter the value to convert: "))

    if unit_from == "kilometers" or unit_from =="km":
        result = value * 0.621371
        print(f"{value} kilometers is equal to {result:.2f} miles")
    elif unit_from == "miles" or unit_from== 'm':
        result = value * 1.60934
        print(f"{value} miles is equal to {result:.2f} kilometers")
    else:
        print("Invalid unit. Please try again.")

    unit_from = input("Enter the unit you're converting from (centimeter or meter): ").lower()
    value = float(input("Enter the value to convert: "))

    if unit_from =="centimeter" or unit_from =="cm":
        result=value*0.01
        print(f"{value} centimeters is equal to {result:.2f} meters")
    elif unit_from =="meter" or unit_from =="m":
        result=value*100
        print(f"{value} meters is equal to {result:.2f} centimeters")
    else:
        print("Invalid unit. Please try again.")
def convert_weight():
    """
    Converts between kilograms and pounds.
    """

    unit_from = input("Enter the unit you're converting from (kilograms or pounds): ").lower()
    value = float(input("Enter the value to convert: "))

    if unit_from == "kilograms" or unit_from =="kg":
        result = value * 2.20462
        print(f"{value} kilograms is equal to {result:.2f} pounds")
    elif unit_from == "pounds"or unit_from=="p":
        result = value * 0.453592
        print(f"{value} pounds is equal to {result:.2f} kilograms")
    else:
        print("Invalid unit. Please try again.")

def convert_currency():
    """
    Converts between US dollars, euros and  Pakistani Rupees
    """

    unit_from = input("Enter the unit you're converting from (US dollars or euros): ").lower()
    value = float(input("Enter the value to convert: "))

    exchange_rate = 1.18

    if unit_from == "us dollars" or unit_from =="$":
        result = value * exchange_rate
        print(f"{value} US dollars is equal to {result:.2f} euros")
    elif unit_from == "euros" or unit_from =="e":
        result = value / exchange_rate
        print(f"{value} euros is equal to {result:.2f} dollars")
    else:
        print("Invalid unit. Please try again.")

    unit_from = input("Enter the unit you're converting from (US dollars or rupees): ").lower()
    value = float(input("Enter the value to convert: "))

    exchange_rate = 279.49
    if unit_from == "us dollar" or unit_from=="$":
        result=value*exchange_rate
        print(f"{value} US dollars is equal to {result:.2f} rupees")
    elif unit_from == "rupees" or unit_from == "r":
        result=value/exchange_rate
        print(f"{value} rupees is equal to {result:.2f} US dollars")   
    else:
        print("Invalid unit. Please try again.")
        

def convert_length():
    """
    Converts between length in centimeters, meters, inches,  and yard.
    """

    unit_from = input("Enter the unit you are converting from( centimeter or inches): ").lower()
    value = float(input("Enter the value to convert: "))

    if unit_from == "centimeter" or  unit_from == "cm":
        result= value*0.393701
        print(f"{value} centimeter is equal to {result:.2f} inches ")
    elif unit_from == "inches" or unit_from=="in":
        result=value*2.54
        print(f"{value} inches is equal to {result:.2f} centimeter ")
    else:
        print("Invalid unit. Please try again.")


    unit_from = input("Enter the unit you are converting from( meter or yards): ").lower()
    value = float(input("Enter the value to convert: "))
    if unit_from =="meter" or unit_from=="m":
        result=value*1.09361
        print(f"{value} meters is equal to {result:.2f} yards ")
    elif unit_from=="yards" or unit_from=="y":
        result=value*0.9144
        print(f"{value} yards is equal to {result:.2f} meters ")
    else:
        print("Invalid unit. Please try again.")

def convert_gpa():
    marks = input("Enter your Marks:")
    if marks>=85:
        print("Your Gpa is A")
     
    
       




# Start the program
convert_units()
