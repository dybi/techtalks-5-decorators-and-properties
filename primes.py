from datetime import datetime


def is_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True


def print_next_prime(number):
    """Print the closest prime number larger than *number*."""

    start = datetime.now()
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
            break
    stop = datetime.now()
    print(f"Execution time: {(stop-start).microseconds} microseconds")


print_next_prime(35)

print_next_prime(11123)

