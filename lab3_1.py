#циклға есеп for циклына

numbers = [10,20,30,40,50]
 
zhup_san, taq_san = 0, 0
 
for num in numbers:
  
    if num % 2 == 0:
        zhup_san += 1
 
    else:
        taq_san += 1
         
print("Zhup sandar: ", zhup_san)
print("Taq sandar: ", taq_san)
