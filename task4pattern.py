def print_number_pyramid(height):
    for i in range(1, height + 1):
        
        for j in range(height - i):
            print(" ", end="")
        
        for k in range(1, i + 1):
            print(k, end=" ")
        
        print()

pyramid_height = 50
print("Number Pyramid:")
print_number_pyramid(pyramid_height)
