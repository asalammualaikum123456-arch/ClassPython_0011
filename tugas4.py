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