class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.pi = 3.14

    def Color(self):
        return self.color

    def Circumference(self):
        return 2 * self.pi * self.radius


def main():
    radius = float(input("Input the radius of the circle:"))
    color = input("Input the color of the circle:")

    if color == 'red' or 'blue' or 'green':
        print('Ur a basic ass mf.')
    else:
        print('U are not basic :D.')

    # Create a Circle object with user input
    circle = Circle(radius, color)

    # Print the color and circumference of the circle
    print(f"Color: {circle.Color()}")
    print(f"Circumference: {circle.Circumference():.2f}")


if __name__ == "__main__":
    main()