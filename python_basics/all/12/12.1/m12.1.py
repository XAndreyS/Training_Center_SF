#month = input ("Какой сейчас месяц?")
#print ("Текущий месяц -", month)

L=['', '', '17', '2', '17', '3', '17', '4', '17', '5', '17', '6', '17', '7', '17', '8', '17', '9', '17', '10', '17']
Ls=[]

for i in L:
    if i == '':
        L.pop(0)
    else:
        Ls.append(int(i))



#Ls=[int(x) for x in Ls]
print(Ls)
#print(sorted(Lm))

