import argparse


def primes(n):
    composites = set()
    for i in range(2, n+1):
        for j in range(i, n // i + 1):
            composites.add(i * j)
    primes = []
    for y in range(2, n+1):
        if y not in composites:
            primes.append(y)
    return primes


def main(n):
    return primes(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print all primes up to n.")
    parser.add_argument("n", type=int, help="upper bound (inclusive)")
    args = parser.parse_args()
    print(main(args.n))
