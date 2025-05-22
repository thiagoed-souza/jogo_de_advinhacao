import random

print("Seja muito bem vindo ao Jogo de Adivinhação do Thiago")
p_number =  input("Digite o número teto do desafio: ")

if p_number.isdigit():
    p_number = int(p_number)
else:
    print("Error: valor informado não é númerico. Por favor, execute e informe um número!")
    quit()

random_number = random.randint(0, p_number)

n_escolhas = 0

while True:
    answer_user = input("Advinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Error: valor informado não é númerico. Por favor, execute e informe um número!")
        continue

    n_escolhas = n_escolhas + 1
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, o número randonico é menor que isso...")
    else:
        print("Chutou baixo, o número randonico é maior que isso...")
    
print("Nº de tentativas: " + str(n_escolhas))
