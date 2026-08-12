n = int(input())

numbers = map(int, input().split())

t = tuple(numbers)

print(hash(t))