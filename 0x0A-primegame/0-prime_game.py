#!/usr/bin/python3
"""game theory module"""


def isWinner(x, nums):
    """who is the winner"""
    if not nums or x == 0:
        return None
    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= max_n:
        if sieve[p]:
            for multiple in range(p * p, max_n + 1, p):
                sieve[multiple] = False
        p += 1
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]

    def play_game(n):
        if n < 2:
            return "Ben"
        remaining = list(range(1, n + 1))
        prime_counts = {num: 0 for num in primes if num <= n}
        maria_turn = True
        while True:
            move_made = False
            for prime in primes:
                if prime > n:
                    break
                if prime_counts[prime] == 0:
                    move_made = True
                    for multiple in range(prime, n + 1, prime):
                        if multiple in prime_counts.keys():
                            prime_counts[multiple] += 1
                    break
            if not move_made:
                return "Maria" if not maria_turn else "Ben"
            maria_turn = not maria_turn
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
