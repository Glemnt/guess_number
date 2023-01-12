import random

alcance = input('Escolha um número: ')

if alcance.isdigit():
    alcance = int(alcance)

    if alcance <= 0:
        print('Por favor escolha um número maior que zero da próxima vez ')
        quit()
else:
    print('Por favor escolha um número da próxima vez ')
    quit()

r = random.randint(0, alcance)
escolhas = 0

while True:
    escolhas += 1
    chute_usuario = input('Tenta acertar: ')
    if chute_usuario.isdigit():
        chute_usuario = int(chute_usuario)
    else:
        print('Por favor escolha um número da próxima vez ')
        continue

    if chute_usuario == r:
        print('Ai sim, acertou!')
        break
    elif chute_usuario > r:
        print('Errou amigão, o número é menor!')
    else:
        print('Errou amigão, o número é maior!')

print('Você conseguiu em', escolhas, 'chutes')