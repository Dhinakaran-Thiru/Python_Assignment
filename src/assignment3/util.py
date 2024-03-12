def given_string(s,pos,character):
    s = input("Enter your string: ") #pos --position
    pos, character = input("Enter the exact position and character separated by space: ").split()
    pos = int(pos)


    return s[:pos] + character + s[pos + 1:]
