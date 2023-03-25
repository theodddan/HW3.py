from random import randint

def shuffle(S):
    n = len(S)
    for i in range(n - 1):
        j = randint(i,n - 1)
        S(i), S(j), = S(j), S(i)
    return S

def perfect_square(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False

def rps(n):
    count = 0
    while count < n:
        p1 = int(input("Player 1: type 1 for R, 2 for P, or 3 for S:"))
        p2 = int(input("Player 2: type 1 for R, 2 for P, or 3 for S:"))
        if p1 == p2:
            print("It's a tie!")
        elif p1 == 1 and p2 == 3 or p1 == 2 and p2 == 1 or p1 == 3 and p2 ==2:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        count += 1
