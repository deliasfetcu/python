#Fiind date listele;
#       prenume = ['Mihai','George','Ana','Dan','Ion','Geta','Vio'] 
#       varsta = [14, 23, 15, 14, 12, 41, 39] încercați să rezolvați cerințele următoare:
#a)	cosiderând că fiecare persoană are asociată vârsta pe același indice, afișați precum mai jos:
#Mihai are varsta de 14 ani. 
#George are varsta de 23 de ani.
#….
#b)	Adăugați în liste la final, corespunzător, datele: Andreea, 34 și Ioan, 23. Tipăriți ambele liste apoi.
#c)	Ștergeți datele din ambele liste despre Ana (atenție la indici).
#d)	Ordonați crescător ambele liste și afișați-le!
#e)	Ștergeți definitiv lista varsta. Verificați cu print() apoi.
#f)	Afișați primele trei elemente din lista prenume.
#g)	Afișați ultimele elemente din lista prenume.
#h)	Afișați lista prenume de la dreapta la stânga.
#i)	Extindeți lista cu una la alegere care să conțină alte prenume și afișați apoi noua listă formată.
#j)	Tipăriți elementele cu indicii 2 și 4, apoi de la 0 la 5.
#Rezolvare:
prenume = ['Mihai','George','Ana','Dan','Ion','Geta','Vio']
varsta = [14, 23, 15, 14, 12, 41, 39] 
for i in range(len(prenume)):
    print(f"{prenume[i]} are vârsta de {varsta[i]} ani.")
prenume.append('Andreea')
prenume.append('Ioan')
varsta.append(34)
varsta.append(23)
print(prenume)
print(varsta)
prenume.pop(2)
varsta.pop(2)
prenume.sort()
varsta.sort()
print(prenume)
print(varsta)
varsta.clear()
print(varsta)
print(prenume[0:3])
print(prenume[-2:])
print(prenume[::-1])
lista_noua = ['Maria', 'Ioana', 'Dana', 'Marcel']
print(prenume + lista_noua)
print(prenume[2])
print(prenume[4])
print(prenume[0:5])
