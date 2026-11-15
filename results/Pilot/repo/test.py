from primes import main


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def test_empty_ranges():
    assert main(0) == []
    assert main(1) == []


def test_small_values():
    assert main(2) == [2]
    assert main(3) == [2, 3]
    assert main(10) == [2, 3, 5, 7]
    assert main(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_count_below_100():
    assert len(main(100)) == 25


def test_all_results_are_prime():
    for value in main(200):
        assert is_prime(value)


def test_returns_sorted_unique_values():
    result = main(100)
    assert result == sorted(result)
    assert len(result) == len(set(result))
