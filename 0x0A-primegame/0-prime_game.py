#!/usr/bin/python3
"""
Two frienda play a prime number game and retuen the winner
"""

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        return {i for i in range(2, n + 1) if is_prime(i)}

    def play_round(n):
        primes = get_primes_up_to_n(n)
        maria_turn = True

        while primes:
            chosen = min(primes)
            primes -= set(range(chosen, n + 1, chosen))
            maria_turn = not maria_turn

        return "Maria" if not maria_turn else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
