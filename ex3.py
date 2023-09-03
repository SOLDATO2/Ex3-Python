"""
A estrategia utilizada para este exercicio foi efetuar 3 tipos de verificações entre as caracteres que o usuario digitou e as palavras escolhidas pelo usuario.

1. caracteres que existem na palavra objetivo mas não estão na mesma posição
2. caracteres que existem e estão na mesma posição
3. caracteres que não existem na palavra objetivo


"""
import random



def ler_arq(arq): #Função para obter o conteudo do arquivo txt
       
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f]

def escolher_pal(lista): # função para escolher uma palavra aleatoria de uma lista e retornar da função 
    palavra = random.choice(lista) # obtem uma palavra da lista txt
    return palavra


def verificar_char(palavra_usuario, palavra_sistema): # tem o objetivo de informar quais caracteres do usuario se encontram na palavra
    if palavra_usuario == palavra_sistema:
        print("Voce acertou!")
        return True
    else:
        #fazer verificação se x palavras de palavra_usuario se encontram em palavra_sistema
        for i in range(len(palavra_usuario)): 
            if palavra_usuario[i] in palavra_sistema: # porção do codigo responsavel por pegar cada palavra da palavra_usuario e verificar se ela(s) existe(m) na palavra escolhida pelo sistema
                index = palavra_sistema.find(palavra_usuario[i]) #pega o index da char palavra_sistema que existe simultaneamente em palavra_usuario
                if i == index:                                   #Ex: palavra_usuario[i] = "a".        palavra_sistema.find(palavra_usuario[i]) retorna "a"
                    print(f"A letra '{palavra_usuario[i]}' na posição {i} está na mesma posição da palavra escolhida!")
                else:
                    print(f"A letra '{palavra_usuario[i]}' na posição {i} se encontra, porem não está na posição correta.")
            else:
                print(f"A letra '{palavra_usuario[i]}' na posição {i} não se encontra")
        
    

def jogo(): # funcao principal
    vidas = 6
    arq_txt = "lista_palavras.txt"
    lista = ler_arq(arq_txt) # retorna lista com palavras do arquivo
    palavra_escolhida = escolher_pal(lista) # retorna palavra escolhida pelo programa
    while(vidas != 0):
        
        print(f"A palavra possui {len(palavra_escolhida)} caracteres.")
        
        input_usuario = input("Digite uma palavra: ")
        vidas -= 1
        
        if verificar_char(input_usuario, palavra_escolhida) == True: #se a função retornar true, signfica que o usuario descobriu a palavra
            print(f"Palavra que foi escolhida pelo sistema: {palavra_escolhida}")
            break
        print(f"tentativas restantes: {vidas}")
    if vidas == 0:
        print("Tentativas esgotadas, voce perdeu")
        
           
jogo()