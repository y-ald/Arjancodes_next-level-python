def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_chained_permutations(data: list[int]) -> list[int]:
    ...

def main() -> None:
    # Test data
    data = [1, 2, 3, 4, 5]
    
    # TODO: Use itertools to generate all permutations of the data list

    # TODO: Filter the permutations to keep only those where the first element is prime

    # TODO: Use itertools to chain together the filtered permutations
    chained_permutations: list[int] = calculate_chained_permutations(data)

    # Print the sum of the chained permutations

    return sum(chained_permutations)


if __name__ == "__main__":
    main(data)
