# Task 1: Start 
# Begin by asking the user to enter the temperature in Fahrenheit.

def weather_input():
    print("What is the weather temperature today?")
    try:
        user_input = int(input("Enter a Fahrenheit number: ")) 
        print("Thank You For That......")
        return user_input
    except ValueError:
        print("Thats Not A Valid Number")
       


# Task 2: Temperature Conversion
#  Write a function that converts the Fahrenheit temperature to Celsius.
#  Remember that the formula is (Fahrenheit - 32) * 5/9.
# Use a try block to catch any potential errors during the conversion process. 
# What happens if they type out "thirty" instead of doing 30?
# Task 3: 
# User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."
# Task 4: 
# Finally Add a finally block that thanks the user for using the weather forecast application, 
# ensuring that this message is displayed regardless of whether an exception was caught or not.

def temperature_converter(user_input):
    try:
        celsius = (user_input - 32) * 5/9
    except TypeError:
        print("Wake up!!!")
    else:
        print(f'This is the temperature you gave in fahrenheit: {user_input} now in celsius: {celsius}')
    finally:
        print("Thank you for using this weather application and i hope it was helpful!!")

fahrenheit = weather_input()
temperature_converter(fahrenheit)