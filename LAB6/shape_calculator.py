import geometry_utils as gu

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")

operation = input("Enter the operation you want to perform: ")

operations = {
    "circle_area": gu.circle_area,
    "circle_perimeter": gu.circle_perimeter,
    "rectangle_area": gu.rectangle_area,
    "rectangle_perimeter": gu.rectangle_perimeter,
    "triangle_area": gu.triangle_area
}

if operation not in operations:
    print("Input Error: Invalid operation selected.")

else:
    if "circle" in operation:
        radius = input("Enter radius: ")

        if radius.replace(".", "", 1).isdigit() and float(radius) > 0:
            result = operations[operation](float(radius))
            print("Result:", round(result, 2))
        else:
            print("Input Error: Dimensions must be strictly positive.")

    elif "rectangle" in operation:
        width = input("Enter width: ")
        height = input("Enter height: ")

        if (width.replace(".", "", 1).isdigit() and float(width) > 0 and
            height.replace(".", "", 1).isdigit() and float(height) > 0):

            result = operations[operation](float(width), float(height))
            print("Result:", round(result, 2))

        else:
            print("Input Error: Dimensions must be strictly positive.")

    elif "triangle" in operation:
        base = input("Enter base: ")
        height = input("Enter height: ")

        if (base.replace(".", "", 1).isdigit() and float(base) > 0 and
            height.replace(".", "", 1).isdigit() and float(height) > 0):

            result = operations[operation](float(base), float(height))
            print("Result:", round(result, 2))

        else:
            print("Input Error: Dimensions must be strictly positive.")