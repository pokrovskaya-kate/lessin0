first = 6
second = 9
third = 4
if first == second and second == third and third == first:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif first != second and second != third and third != first:
    print(0)