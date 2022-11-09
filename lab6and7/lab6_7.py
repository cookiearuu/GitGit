#  Тізімдерді, кортеждерді, жиындарды және сөздіктерді
# бір бағдарламаның ішінде көрсететін бағдарлама жаз.
#  Мәлеметтер ретінде әр студент өзіне байланысты
# ақпарат немесе резюмесін ұсыну қажет.


list = ["Aruzhan","Aliya","Zhanerke","Almash"]
tuple = ("math","history","art", "physics")
set= {"16.09.02","08.01.02","26.05.02","25.07.02"}
dict ={"city":"Almaty","district":"Alatau","street":"Michurina","home":"16","flat":"a"}


print(list)
print(tuple)
print(set)
print(dict)

# Тізімдердегі, кортеждердегі, жиындардағы
# және сөздіктердегі әдістерді қарастырып,
# барлығына ортақ 5 әдісті және ерекшеленетін
# бірнеше (2-3) әдістерді қолдананатын бағдарлама жаз.

from re import L


list = ["apple","pear","banana","grape"]
tuple=("python","java","c++","php")
set={"fuse tea","max tea","ice tea","lemon tea","black tea"}
dict={"cake1":"chocolate","cake2":"milky","cake3":"fruity","cake4":"with nuts","cake5:":"with spinach"}



#list
print("LISTS")

list2 = ["watermelon","peach"]
list.extend(list2)  #extends
list.append("abrikos") #adds
list.insert(1,"new fruit") #adds by i
list.remove("new fruit")
#list.clear()
print(list)


#tuple
print("TUPLES" )
tuple2 = ("javascript","c#")
print(tuple+tuple2)#extended
print(tuple[::-1]) #reversed
print(len(tuple))
print(tuple2.count("c#"))
tuple3 = (80,55,40,50,60,20)
print(sorted(tuple3))
print(max(tuple3))
#del tuple




#set 
print("SETS ")
set.add("milkshake")#added
set.pop()#random el
set.discard("ice tea") #delete
# set.clear()
print(set)
set2 = {"water","wine"}
print(set.union(set2))
set3 = set2.copy()
print(len(set3))


#dict
print("DICTIONARY ")
print(dict)
print(dict.values())
print(dict.get("cake3"))
print(dict.items())
print(dict.keys())
print(dict.pop("cake1"))
print(dict)


#3. Берілген есептерден бір есепті таңдап шығару
#  Словарь синонимов
# Вам дан словарь, состоящий из пар слов. 
# Каждое слово является синонимом к парному ему слову. 
# Все слова в словаре различны. Для одного данного слова определите его синоним.


dictionary = {}
n = int(input())
for i in range(n):
    first, second = input().split()
    dictionary[first] = second
    dictionary[second] = first

print(dictionary[input()])