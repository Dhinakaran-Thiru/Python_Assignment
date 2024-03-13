from src.text_alignment.util import print_pattern

def main():

   thickness = int(input("Enter the thickness: "))

   character = input("Enter the character: ")

   pattern_list = print_pattern(thickness, character)

   for line in pattern_list:

       print(line)