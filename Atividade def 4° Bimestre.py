import time
def escrever(texto):
    for I in texto:
        print(I, end="", flush= True)
        time.sleep(0.05)



q1= '''
def inter(q1l1, q1l2):
    return list(set(q1l1) & set(q1l2))
 

q1l1a = input("Mim dê alguns valores: ")
q1l1 = list(map(int, q1l1a.split()))
q1l2a = input("Mim dê mais alguns valores: ")
q1l2 = list(map(int, q1l2a.split()))
print(inter(q1l1, q1l2))'''

q2 = '''
def dectpar():
    while True:
        q2a = int(input("Me dê um número: "))
        if q2a % 2 == 0:
            print("Seu número é par")
        else:
            print("Seu número é impar")'''


q3 = '''
def repete(q3l1):
    if q3l1.count(q3l1b) != 0:
        return q3l1.count(q3l1b)
    else:
        return 0

q3l1a = input("Mim dê alguns valores: ")
q3l1 = list(map(int, q3l1a.split()))
q3l1b = int(input("Mim dê um valor: "))
print(repete(q3l1))'''


q4 ='''
def naota(q4l1, q4l2):
    return list(set(q4l1).difference(q4l2))

q4l1a = input("Mim dê alguns valores: ")
q4l1 = list(map(int, q4l1a.split()))
q4l2a = input("Mim dê mais alguns valores: ")
q4l2 = list(map(int, q4l2a.split()))
print(naota(q4l1, q4l2))'''


q5 = '''
def soma(q5a, q5b, q5c):
    return q5a + q5b + q5c

q5a = int(input("Mim dê um número: "))
q5b = int(input("Mim dê outro número: "))
q5c = int(input("Mim dê mais um número: "))
print(soma(q5a, q5b, q5c))'''


q6 = '''
def desconto(q5a):
    if q5a <= 100:
        return "Sem desconto"
    elif q5a > 100 & q5a <= 300:
        return "Tem desconto de 10% e o valor de seu produto agora é {}".format(round(q5a - q5a * 0.1))
    elif q5a > 300:
        return "Tem desconto de 15% e o valor de seu produto agora é {}".format(round(q5a - q5a * 0.15))
    
q5a = int(input("Mim dê um valor: "))
print(desconto(q5a))'''


q7 = '''
def celfah(q7a):
    return("{}°C".format(round(q7a * 1.8 + 32)))
def fahcel(q7a):
    return("{}°F".format(round((q7a - 32) / 1.8)))
def menu():
    while True:
        escrever('1 - Celsius para Fahrenheit\n2 - Fahrenheit para Celsius')
        q7r = int(input("\nR: "))
        if q7r == 1:
            q7a = int(input("Mim dê uma temperatura: "))
            print(celfah(q7a))
        elif q7r == 2:
            q7a = int(input("Mim dê uma temperatura: "))
            print(fahcel(q7a))
        else:
            print("Resposta inválida")
menu()'''


def diff(q8l):
    return len(q8l) != len(set(q8l))
 

q8la = input("Mim dê alguns valores: ")
q8l = list(map(int, q8la.split()))
print(diff(q8l))

#https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list


