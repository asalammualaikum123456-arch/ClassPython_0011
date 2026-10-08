class Rectangle:
    
    def __init__(self, length, width):
        if length == 0 or width == 0:
            raise ValueError("The input value cannot be 0.")
        self.length = length
        self.width = width

    def calculate_circumference(self):
        return 2 * (self.length + self.width)

    
    def calculate_area(self):
        return self.length * self.width

    def __str__(self):
         return f"rectangle, {self.length} cm long, and {self.width} cm wide"

    def main():
        print("=== Rectangle Calculator ===")
        try:

            length = float(input("Enter the length (cm): "))
            width = float(input("Enter the width (cm): "))

            if length == 0 or width == 0:
                        print("Error: The input value cannot be 0.")
                        return

            my_rectangle = Rectangle(length, width)

            print("\n--- Output ---")
            print(my_rectangle)

            print(f"Area: {my_rectangle.calculate_area()} cm²")
            print(f"Circumference: {my_rectangle.calculate_circumference()} cm")
            
        except ValueError as e:
            print(f"Invalid input! {e}")
            
            if __name__ == "__main__":
                main()

        