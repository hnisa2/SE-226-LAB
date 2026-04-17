from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)
try:
    user_input=input(
        "Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): "
    )
    parts=user_input.split(",")

    parts=strip_whitespaces(parts)

    numbers=[float(x) for x in parts]
    numbers=remove_duplicates(numbers)

    print(f"Cleaned and unique data: {numbers}")
    print("-" * 20)

    mean_val=calculate_mean(numbers)
    max_val=find_maximum(numbers)
    min_val=find_minimum(numbers)

    print(f"Mean: {mean_val:.2f}")
    print(f"Maximum: {max_val}")
    print(f"Minimum: {min_val}")

except ValueError:
    print("Data Error: Please make sure you only enter numbers separated by commas.")