def merging():
    s = input("enter the string:")
    k = int(input("Enter the number u have to divide:"))
    result = []
    for i in range(0, len(s), k):
        substring = s[i:i+k]
        new_string = []
        for char3 in substring:
            if char3 not in new_string:
                new_string.append(char3)
        result.append(''.join(new_string))
    return '\n'.join(result)

