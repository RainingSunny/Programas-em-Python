from random import choice


def jogar():
    while True:
        iniciar_tela()  # Iniciando o código com uma função para a tela de introdução.

        # Função que gera uma palavra aleatória e crie uma string que se adapte a ela.
        palavra_aleatoria = gerar_palavra_aleatoria()
        letras_acertadas = string_para_forca(palavra_aleatoria)

        # Iniciar as variaveis que serão utilizadas no decorrer do game.

        ganhou = False
        perdeu = False
        letras_chutadas = set()
        erros = 0

        while not ganhou and not perdeu:    # Iniciação do jogo pelo Loop While
            print(' '.join(letras_acertadas))

            chute_usuario = pede_chute()    # Pedir chute do usuário com tratamento de erros.

            # 1 - Verificar se o chute que o usuário digitar não terá None como retorno caso seja um número digitado.
            # 2 - Jogar o chute do usuário dentro de um Set e verificar se já foi jogado.
            if chute_usuario is not None:
                if chute_usuario in letras_chutadas:
                    print(f'{chute_usuario} já foi jogado. Jogue outro valor.')
                else:
                    letras_chutadas.add(chute_usuario)

                    # Verificar se o chute do usuário é igual a alguma letra da palavra sorteada.
                    acertou_chute = marca_letra(palavra_aleatoria, chute_usuario, letras_acertadas)

                    if not acertou_chute:
                        erros += 1
                        desenha_forca(erros)
                        if erros == 7:
                            break
                        print(f'Você errou, tente outra letra. {7 - erros} tentativas restantes!')

                # Criar método para finalizar o jogo.
                ganhou = '_' not in letras_acertadas
                perdeu = erros == 7

        if ganhou:
            imprime_mensagem_vencedor(palavra_aleatoria)
        else:
            imprime_mensagem_perdedor(palavra_aleatoria)

        # Criar função para perguntar ao usuário se ele deseja jogar novamente.
        if not perguntar_jogar_novamente():
            break


def iniciar_tela():
    tela_asteristico = '-*' * 20
    print(tela_asteristico)
    # Centraliza o "Jogo da Forca" de acordo com a quantidade de asterísticos utilizados na variável tela
    print('JOGO DA FORCA'.center(len(tela_asteristico)))
    print(tela_asteristico)


def gerar_palavra_aleatoria():
    with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
        todas_palavras = [palavra.strip().upper() for palavra in arquivo]
    escolher_palavra = choice(todas_palavras)
    return escolher_palavra


def string_para_forca(palavra):
    return ['_' for _ in palavra]


def pede_chute():
    chute = input('Digite uma letra: ').strip().upper()
    if len(chute) == 1 and (chute.isalpha() or chute.isascii() and not chute.isnumeric()):
        return chute
    else:
        print('Digite um valor válido!')
        return None


def marca_letra(palavra_aleatoria, chute_usuario, letras_acertadas):
    acertou = False
    for pos, letra in enumerate(palavra_aleatoria):
        if chute_usuario == letra:
            letras_acertadas[pos] = chute_usuario
            acertou = True
    return acertou


def imprime_mensagem_vencedor(palavra_aleatoria):
    print('Parabéns, você ganhou!')
    print(f'A palavra secreta era {palavra_aleatoria}')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_aleatoria):
    print("Puxa, você foi enforcado!")
    print(f'A palavra secreta era {palavra_aleatoria}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def perguntar_jogar_novamente():
    while (jogar_novamente := input('Deseja jogar novamente? [S/N]: ').strip().upper()) not in 'SN':
        print('Escolha uma opção válida!')
    return jogar_novamente == 'S'


if __name__ == "__main__":
    jogar()
