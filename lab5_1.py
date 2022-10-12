# # #lab 5.1
# last_names = []
# n=int(input())
# grades = []
# while n>0:
#   last_names.append(input("name: "))
#   grades.append(input("course: "))
#   n=n-1

# print(last_names[0]+": "+grades[0]+"\n"+last_names[1]+": "+grades[1]+"\n"+last_names[2]+": "+grades[2]+"\n")
# print(grades.sort())




#lab5.2
resume = ["Aruzhan", "Abylkassym", "87057774612", "Satbayev University"]
print("Lastname:", resume[0], "\nName:", resume[1], "\nPhone:", resume[2], "\nUniversity:",resume[3])

resume.append(20)
print("APPEND: \n", resume)

resumesecond = ["16.09.2002","Almaty city"]
resume.extend(resumesecond)
print("EXTEND: \n", resume)

x = "87070192484"
resume.insert(2, x)
print("iNSERT: \n", resume)

resume.remove(20)
print("REMOVE: \n", resume)

resume.reverse()
print("REVERSING: \n", resume)

resume.clear()
print("\n", resume)


#lab5.3


# a = [99,25,65,75,12,66,44]

# if(a.sort()==True):
#   print("true")

# else:
#   print("false")

            



