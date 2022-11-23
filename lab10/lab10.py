file = open('lab10.txt', 'w')

while True:
    i = input("Введите элемент: ")
    if i ==" " or i =="":
        break
    file.writelines(str(i) + '\n')
file.close()

lst = []
file1 = open('lab10.txt', 'r')

while True:
    line = file1.readline()
    if not line:
        break
    lst.append(int(line.strip()))
print(lst)


print("SORTED LIST",sorted(lst))
print("MIN ELEMENT OF LIST: ", min(lst))
print("MAX ELEMENT OF LIST: ", max(lst))
print("LIST IN BIN ",bin(lst[1]))
print("LIST IN HEX",hex(lst[1]))
print("LIST IN OCT", (lst[1]))

print("NUMERATED LIST: ",list(enumerate(lst)))
print("NUMBER IN ASCII CODE ", chr(lst[1]))
print("LIST IN BYTES ",bytes(lst))
print(reversed(lst))

file1.close()

lst2 = [2, 1, 3, 4, 7]
for i, n in zip(lst, lst2):      
    print(n, i)