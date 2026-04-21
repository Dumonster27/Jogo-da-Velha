import random  # Importa o módulo para sortear quem começa o jogo

def imprimir_tabuleiro(board):
    """Exibe o tabuleiro no console usando f-strings para formatação."""
    # O mapeamento segue o estilo de um teclado numérico (7,8,9 no topo)
    print("\n")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("\n")

def escolha_marcador():
    """Pergunta ao Jogador 1 qual símbolo ele deseja e atribui ao Jogador 2 o restante."""
    marcador = ''
    while marcador != 'X' and marcador != 'O':
        marcador = input("Jogador 1, você quer ser 'X' ou 'O'? ").upper().strip()

    if marcador == 'X':
        return ('X', 'O')  # Retorna uma tupla (Jogador 1, Jogador 2)
    else:
        return ('O', 'X')

def colocar_marcador(board, marcador, posicao):
    """Atribui o marcador à posição escolhida (ajustando para o índice 0-8 da lista)."""
    board[posicao - 1] = marcador

def verificar_vitoria(board, mark):
    """Verifica todas as 8 combinações possíveis de vitória."""
    return (
        # Linhas Horizontais
        (board[0] == mark and board[1] == mark and board[2] == mark) or
        (board[3] == mark and board[4] == mark and board[5] == mark) or
        (board[6] == mark and board[7] == mark and board[8] == mark) or
        # Colunas Verticais
        (board[0] == mark and board[3] == mark and board[6] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        # Diagonais
        (board[0] == mark and board[4] == mark and board[8] == mark) or
        (board[6] == mark and board[4] == mark and board[2] == mark)
    )

def escolher_primeiro():
    """Sorteia aleatoriamente qual jogador começa."""
    if random.randint(0, 1) == 0:
        return 'Jogador 1'
    else:
        return 'Jogador 2'

def espaco_livre(board, posicao):
    """Verifica se a casa escolhida no tabuleiro está vazia."""
    return board[posicao - 1] == ' '

def tabuleiro_cheio(board):
    """Verifica se ainda existem espaços vazios no tabuleiro (para detectar empate)."""
    for i in range(1, 10):
        if espaco_livre(board, i):
            return False
    return True

def escolha_jogada(board):
    """Solicita a jogada do usuário e valida se o número e o espaço estão corretos."""
    posicao = 0
    while posicao not in range(1, 10) or not espaco_livre(board, posicao):
        try:
            posicao = int(input("Escolha sua jogada (1-9): "))
            if posicao not in range(1, 10):
                print("Inválido! Digite um número de 1 a 9.")
            elif not espaco_livre(board, posicao):
                print("Essa posição já está ocupada!")
        except ValueError:
            print("Erro: Digite apenas números inteiros.")
    return posicao

def jogar_novamente():
    """Pergunta se os jogadores desejam iniciar uma nova partida."""
    return input("Deseja jogar novamente? (S/N): ").strip().upper().startswith('S')

# --- LOOP PRINCIPAL DO JOGO ---
print("BEM-VINDO AO JOGO DA VELHA!")

while True:
    # Reset do jogo: cria lista de 9 espaços vazios
    o_tabuleiro = [' '] * 9 
    marcador_p1, marcador_p2 = escolha_marcador()
    vez = escolher_primeiro()
    print(f"\nO {vez} começa!")
    
    jogo_on = True

    while jogo_on:
        if vez == 'Jogador 1':
            # Turno do Jogador 1
            imprimir_tabuleiro(o_tabuleiro)
            posicao = escolha_jogada(o_tabuleiro)
            colocar_marcador(o_tabuleiro, marcador_p1, posicao)

            # Verifica se venceu após a jogada
            if verificar_vitoria(o_tabuleiro, marcador_p1):
                imprimir_tabuleiro(o_tabuleiro)
                print("BOOOA! O Jogador 1 venceu!")
                jogo_on = False
            else:
                # Verifica se deu empate (tabuleiro cheio e ninguém venceu)
                if tabuleiro_cheio(o_tabuleiro):
                    imprimir_tabuleiro(o_tabuleiro)
                    print("Temos um EMPATE!")
                    break
                else:
                    vez = 'Jogador 2' # Passa a vez
        else:
            # Turno do Jogador 2
            imprimir_tabuleiro(o_tabuleiro)
            posicao = escolha_jogada(o_tabuleiro)
            colocar_marcador(o_tabuleiro, marcador_p2, posicao)

            if verificar_vitoria(o_tabuleiro, marcador_p2):
                imprimir_tabuleiro(o_tabuleiro)
                print("BOOOA! O Jogador 2 venceu!")
                jogo_on = False
            else:
                if tabuleiro_cheio(o_tabuleiro):
                    imprimir_tabuleiro(o_tabuleiro)
                    print("Temos um EMPATE!")
                    break
                else:
                    vez = 'Jogador 1' # Passa a vez

    # Condição de saída do loop principal
    if not jogar_novamente():
        print("\nObrigado por jogar! Até a próxima.")
        break