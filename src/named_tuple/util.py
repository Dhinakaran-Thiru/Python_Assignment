from collections import namedtuple

# Read input
def avg():
    n = int(input())
    columns = input().split()

    # Define namedtuple dynamically
    Student = namedtuple('Student', columns)

    # Calculate and print average marks
    return"{:.2f}".format(sum(int(student.MARKS) for student in (Student(*input().split()) for _ in range(n))) / n)