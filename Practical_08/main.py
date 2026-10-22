"""
File 3: main.py (Main Program)
Demonstrates importing and using modules from the custom package 'MyPackage'.
"""

from MyPackage import arithmetic, geometry

def main():
    # Using arithmetic module
    sum_result = arithmetic.add(10, 5)
    diff_result = arithmetic.subtract(10, 5)

    # Using geometry module
    area = geometry.area_of_circle(7)
    perimeter = geometry.perimeter_of_circle(7)

    # Display results
    print("Sum:", sum_result)
    print("Difference:", diff_result)
    print("Area of Circle:", area)
    print("Perimeter of Circle:", perimeter)

if __name__ == "__main__":
    main()
