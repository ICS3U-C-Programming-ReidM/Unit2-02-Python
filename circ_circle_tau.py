# main.py

# Import the constant value of TAU from the constants.py file
from constants import TAU


# Function to calculate the circumference of a circle
def calculate_circumference(radius):
    return TAU * radius


# Main program to get user input and calculate the circumference
def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        circumference = calculate_circumference(radius)
        print(f"The circumference of the circle is: {circumference}")
    except ValueError:
        print("Please enter a valid number for the radius.")


if __name__ == "__main__":
    main()
