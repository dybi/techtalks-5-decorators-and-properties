from decorators import execution_timer, execution_counter, sleeper


def is_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True


@sleeper(1)
@execution_counter
@execution_timer
def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
            break


print_next_prime(35)
print()
print_next_prime(11123)

