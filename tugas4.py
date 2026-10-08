class Rectangle:
    
    def __init__(self, length, width):
        if length == 0 or width == 0:
            raise ValueError("The input value cannot be 0.")
        self.length = length
        self.width = width
