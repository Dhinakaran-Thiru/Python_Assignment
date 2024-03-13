def new_array(arr):
    # Split the input string into a list of floats
    arr = [float(x) for x in arr.split()]

    # Round down each element
    floor_arr = [int(x) for x in arr]

    # Increment each element by 1
    ceil_arr = [x + 1 for x in arr]

    # Remove the element at index 5
    rint_arr = arr[:5] + arr[6:]

    return floor_arr, ceil_arr, rint_arr


# Sample input
input_str = "1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"

# Call the function
floor_arr, ceil_arr, rint_arr = new_array(input_str)

# Print the results
print(floor_arr)
print(ceil_arr)
print(rint_arr)