def print_christmas_tree(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

# Example usage:
print_christmas_tree(5)
