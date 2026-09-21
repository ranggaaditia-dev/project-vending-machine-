import random

angka_random = random.randint(1,10)

print("Gua udah mikir angka 1-10, ayo tebak!!")

while True:
    try:
        tebak = int(input("Tebak angka : "))
        if tebak < angka_random:
            print("Angkanya kekecilann bos")
        elif tebak > angka_random:
            print("Angkanya kebesaran bos")
        else:
            print("Widih angkanya benar")   
    except ValueError:
            print("Angka ya bos bukan hurus atau apa!!")