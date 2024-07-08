v = ['a','e','i','o','u']
user = input('Digite a frase: ').lower()
c = 0
for i in user:
    if i in v:
        c+=1
print(f" Na sua frase tem {c} vogais")
    