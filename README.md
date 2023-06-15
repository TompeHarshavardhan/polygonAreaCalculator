Rectangle and Square Classes

In this project, you will find the implementation of two classes: Rectangle and Square, using object-oriented programming principles.
Rectangle Class

The Rectangle class represents a rectangle shape. When a Rectangle object is created, it is initialized with width and height attributes. The class provides the following methods:

    set_width: Sets the width of the rectangle.
    set_height: Sets the height of the rectangle.
    get_area: Returns the area of the rectangle (width * height).
    get_perimeter: Returns the perimeter of the rectangle (2 * width + 2 * height).
    get_diagonal: Returns the diagonal of the rectangle ((width ** 2 + height ** 2) ** .5).
    get_picture: Returns a string representation of the shape using lines of "". The number of lines is equal to the height, and the number of "" in each line is equal to the width. If the width or height is larger than 50, the string "Too big for picture." is returned instead.
    get_amount_inside: Takes another shape (square or rectangle) as an argument and returns the number of times the passed-in shape could fit inside the rectangle (with no rotations).

Additionally, the Rectangle class provides a string representation when an instance is printed, which looks like: Rectangle(width=5, height=10).
Square Class

The Square class is a subclass of the Rectangle class, inheriting its methods and attributes. A Square object is created by passing a single side length. The side length is stored as both the width and height attributes in the Rectangle class.

The Square class also includes a method called set_side, which allows setting the side length of the square. When an instance of Square is printed, it appears as: Square(side=9).

Unit Tests

To ensure the correctness of the implementation, unit tests are provided in test_module.py. You can run the tests autpmatically ,by running the main.py included here, to verify that the functionality of the Rectangle and Square classes is working as expected.
