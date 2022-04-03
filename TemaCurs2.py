#declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6

l=[7,8,9,2,3,1,4,10,5,6]

#afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

print("Afișarea unei alte liste ordonată ascendent: " , sorted(l))

#afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

print("Afișarea unei liste ordonată descendent: " , sorted(l, reverse=True))

#afișarea numerelor aflate pe indecsi pari din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

indecsi_pari= l[::2]
print("Afișarea numerelor aflate pe indecsi pari din listă: " , indecsi_pari)

#afișarea numerelor aflate pe indecsi impari din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

indecsi_impari= l[1::2]
print("Afișarea numerelor aflate pe indecsi impari din listă: " , indecsi_impari)

#afișarea elementelor multipli ai lui 3.
l_noua=[]
for numar in l:
    m=numar%3
    if m == 0:
        l_noua.append(numar)
print("Afișarea elementelor multipli ai lui 3: ", l_noua)

