import math

def prime_number(srt, n):
    prime = [True for i in range(n + 2)]
    prime[0] = False
    prime[1] = False

    for p in range(2, int(math.sqrt(n)) + 1):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    for p in range(srt, n + 1):
        if prime[p]:
            print(p, end=" ")



if __name__ == "__main__":
    srt = 1
    end = 100
    prime_number(srt, end)


