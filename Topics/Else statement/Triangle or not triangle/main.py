a = int(input())
b = int(input())
c = int(input())


def valid_triangle(side_a, side_b, side_c):
    return (side_a + side_b + side_c == 180) and a != 0 and b != 0 and c != 0


print("The triangle is valid!" if valid_triangle(a, b, c) else "The triangle is not valid!")
