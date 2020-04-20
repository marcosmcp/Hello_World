#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""
def campeonato():
    i = 1
    vitorias_u = 0
    vitorias_c = 0
    while i <= 3:
        print("*** Rodada,",i,"***")
        vitoria = partida()
        if(vitoria):
            vitorias_u = vitorias_u + 1
        else:
            vitorias_c = vitorias_c + 1            
        i = i + 1
    
    print("Placar: Você", vitorias_u,"X", vitorias_c,"Computador")
    print("**** Final do campeonato! ****")

def computador_escolhe_jogada(n, m):
    i = 1    
    while i <= m:
        t = n - i
        if (t % (m + 1) == 0):            
            return i
        i = i + 1
    return m        


def usuario_escolhe_jogada(n, m):        
    numero_valido = True
    while numero_valido:
        usuario_p = int(input("Quantas peças você vai tirar? "))        
        if usuario_p > 0 and usuario_p <= m:                                
            numero_valido = False            
        else:
            print("Oops! Jogada inválida! Tente de novo.")

    return usuario_p


def partida():
    
    n = int(input("Quantas peças? "))    
    m = int(input("Limite de peças por jogada? "))
    total_p = n
    piezas_u = 0
    piezas_c = 0
    usuario_ativo = False
    
    if (not (n % (m+1))):
        usuario_ativo = True
        print("Voce começa!")
    else:
        print("Computador começa!")
    
    while total_p >= 1:
        if usuario_ativo:            
            piezas_u = usuario_escolhe_jogada(n, m)            
            total_p = total_p - piezas_u
            print("Voce tirou", piezas_u, "peças.")
            print("Agora resta apenas", total_p, "peças no tabuleiro.")
            usuario_ativo = False
        else:   
            piezas_c = computador_escolhe_jogada(total_p, m)
            total_p = total_p - piezas_c
            print("O computador tirou", piezas_c, "peças.")
            print("Agora resta apenas", total_p,"peças no tabuleiro.")
            usuario_ativo = True

    if usuario_ativo:
        print("Fim do jogo! O computador ganhou!")
        return False
    else:
        print("Fim do jogo! Você ganhou!")
        return True
            
    
def main():
    print("""
            Bem-vindo ao jogo do NIM! Escolha:
                1 - para jogar uma partida isolada
                2 - para jogar um campeonato 2
                outra - Sair
            """)
    opcao = int(input(": "))
    if opcao == 1:
        print("Voce escolheu uma partida!")
        partida()
    elif opcao == 2:
        print("Voce escolheu um campeonato!")        
        campeonato()
    else:        
        return        
    


main()
