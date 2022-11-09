import random
num = random.randrange(15,55)
print("random number: " , num)

for i in range(1, num ):
  if(i%3==0 and i%2==0):
    print(i)