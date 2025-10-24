import random

def jogar_adivinhacao():
    numero = random.randint(1, 20)
    tentativas = 0
    print("Tente advinhar um número de 1 a 20.")

    while True:
        palpite = input("Seu palpite: ")
        if not palpite.isdigit():
            print("Digite um número inteiro válido.")
            continue

        palpite = int(palpite)
        tentativas += 1

        if palpite < numero:
            print("Mais alto.")
        elif palpite > numero:
            print("Mais baixo.")
        else:
            print(f"Acertou! O número era {numero}. Você tentou {tentativas} vez(es).")
            break

if __name__ == "__main__":
    jogar_adivinhacao()