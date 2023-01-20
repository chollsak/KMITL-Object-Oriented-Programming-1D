import itertools

digits = input().split()
n = len(digits)

digits = [int(digit) for digit in digits]

result = set()
for permutation in itertools.permutations(digits, n):
    if permutation[0] != 0:
        number = int("".join(map(str,permutation)))
        result.add(number)

print(min(result)) 