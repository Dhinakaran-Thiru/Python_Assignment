import numpy
def new_array(arr):

    arr = [float(x) for x in arr.split()]

    
    floor_arr = [int(x) for x in arr]

    
    ceil_arr = [ceil(x) for x in arr]

   
    rint_arr = [rint(x) for x in arr]

    return floor_arr, ceil_arr, rint_arr


# Sample input
input_str = "1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"

# Call the function
floor_arr, ceil_arr, rint_arr = new_array(input_str)

# Print the results
print(floor_arr)
print(ceil_arr)
print(rint_arr)
