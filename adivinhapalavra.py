import random
import time

dificuldade = 0
palavras = {
"faceis": ["gato", "casa", "bola", "luz", "amor", "fogo", "dado", "chave", "mesa", "rio"],
"medias": ["banana", "cachorro", "elefante", "janela", "computador", "travesseiro", "relogio", "planeta", "girassol", "abacaxi"],
"dificeis": ["psicologia", "biblioteca", "hipopotamo", "extravagante", "paralelepipedo", "melancolia", "xilofone", "refrigerante", "hematoma", "desenvolvimento"]
}


def generate_word(nivel):
    rword = random.choice(palavras[nivel])
    return rword

palavrafacil = generate_word("faceis")
palavramedia = generate_word("medias")
palavradificil = generate_word("dificeis")
letras_descobertasf = ["_"] * len(palavrafacil)
letras_descobertasm = ["_"] * len(palavramedia)
letras_descobertasd = ["_"] * len(palavradificil)

def word_verify(nivelword, dleters, a):
    chances = a
    letras_chutadas = []
    while nivelword != "".join(dleters):
        palpite = input("Chute uma letra: ")
        if palpite in dleters:
            print("você ja acertou esta letra")
            continue
        if len(palpite) != 1:
            print("digite somente uma letra")
            continue
        if palpite in letras_chutadas:
            print("Você ja chutou essa letra")
            continue
        have = False
        for i in range(len(nivelword)):

            if nivelword[i] == palpite:
                dleters[i] = palpite
                have = True
                letras_chutadas.append(palpite)
            elif nivelword[i] != palpite and have == False and i == len(nivelword) - 1:
                print("letra incorreta")
                letras_chutadas.append(palpite)
                chances -= 1
                if chances == 0:
                    print("Suas chances acabaram, fim de jogo!")
                else:
                    print(f"\033[31mvocê tem mais {chances} chances\033[0m\033[1m")

        if chances == 0:
            print(f"a palavra era: {nivelword}")
            break
        if nivelword == "".join(dleters):
            print(f"\033[32mvocê venceu! a palavra era: {nivelword}\033[0m")
        else:
            print(f"letras já chutadas: {", ".join(set(letras_chutadas))}")
            print("".join(dleters))
    return chances



print("\033[1m-------JOGO DA FORCA-------")
print("REGRAS: A cada palavra você tem apenas 5 chances de erro e a cada nível de dificuldade você ga.\n ")
print("1.Nível fácil: Palavras que contêm de 1 a 2 sílabas.")
print("2.Nível médio: Palavras que contêm de 3 a 4 sílabas.")
print("3.Nível difícil: Palavras que contêm de 5 a 7 sílabas.\n ")

time.sleep(1)

while True:
    try:
        dificuldade = int(input("Escolha o nível de dificuldade: "))
    except ValueError:
        print("digite um número válido")
        continue
    if dificuldade == 1:
        word_verify(palavrafacil, letras_descobertasf, 5)
        break
    elif dificuldade == 2:
        word_verify(palavramedia, letras_descobertasm, 6)
        break
    elif dificuldade == 3:
        word_verify(palavradificil, letras_descobertasd, 7)
        break
    else:
        print("digite um número correspondente!")