# -*- coding: utf-8 -*-
from jogo_da_Velha import criarBoard, fazMovimento, getInputValido, printBoard, verificaGanhador, verificaMovimento

jogador = 0 #jogador 1

board = criarBoard()
ganhador = verificaGanhador(board)

while(not ganhador):
    printBoard(board)
    i = getInputValido("Digite a linha: ")
    j = getInputValido("Digite a Coluna: ")
    
    if(verificaMovimento(board, i, j)):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1)%2
    else:
        print("A posição informada já está em uso")

    ganhador = verificaGanhador(board)

print("============")
printBoard(board)
print ("Ganhador = ", ganhador)
print("============")
