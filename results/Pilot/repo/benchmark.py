import pytest

from primes import main

N = 5 * 10**3


def test_primes_benchmark(benchmark):
    benchmark(main, N)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "--benchmark-only"]))
