def linear_search(arr: list, target: any) -> int:
    """
    Perform a linear search on an array to find the target element (returns `-1` if `target` is not found)
    """

    for i,elem in enumerate(arr):
        if elem == target:
            return i

    return -1

# Example usage; this will only execute if you run `main.py`
if __name__ == "__main__":
    import random

    n = 10 # Number of random numbers (exclusive)
    numbers = [int(random.random() * 100) for x in range(n)]
    print(
        linear_search(
            numbers,
            random.choice(numbers)
        )
    )
