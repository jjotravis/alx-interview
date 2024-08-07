def isWinner(x, nums):
    """
    Determines the winner of a game played between Maria and Ben over x rounds.
    In each round, they take turns picking prime numbers from a set of consecutive integers starting from 1 up to n,
    removing the chosen prime and its multiples. The player who cannot make a move loses.
    The function returns the name of the player who wins the most rounds.
    """
    def findPrimes(num):
        if num < 2:
            return 0
        primes = [True] * (num + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= num:
            if primes[p]:
                for i in range(p * p, num + 1, p):
                    primes[i] = False
            p += 1
        return sum(primes)

    players = {'Maria': 0, 'Ben': 0}
    
    for n in nums:
        primes_count = findPrimes(n)
        if primes_count % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
