dictionary = {}
n = int(input())
for i in range(n):
    first, second = input().split()
    dictionary[first] = second
    dictionary[second] = first

print(dictionary[input()])