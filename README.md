Jogo da Velha (Tic-Tac-Toe) em Python 🎮
Este é um projeto simples de Jogo da Velha desenvolvido em Python para ser jogado diretamente no terminal. O projeto foi criado com o objetivo de praticar conceitos fundamentais da linguagem, como manipulação de listas, funções, loops while, tratamento de erros e lógica de jogos.

✨ Funcionalidades
Sorteio de início: O jogo utiliza o módulo random para decidir aleatoriamente quem começa (Jogador 1 ou Jogador 2).

Escolha de marcadores: O Jogador 1 pode escolher entre "X" ou "O".

Validação de jogadas: O sistema impede que um jogador escolha uma posição já ocupada ou um número fora do intervalo de 1 a 9.

Detecção de vitória e empate: O jogo verifica automaticamente se houve um vencedor ou se o tabuleiro ficou cheio (empate).

Sistema de Replay: Ao final de cada partida, os jogadores podem optar por jogar novamente sem precisar reiniciar o script manualmente.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Módulos Nativos: random

🚀 Como Executar
Certifique-se de ter o Python instalado em sua máquina. Você pode verificar digitando python --version no seu terminal.

Clone o repositório:

Navegue até a pasta do projeto:

Execute o jogo:

🎮 Como Jogar
O tabuleiro é mapeado de acordo com os números do teclado numérico (ou de 1 a 9 começando pela base):

Quando for sua vez, digite o número correspondente à posição desejada.

O objetivo é alinhar três marcadores iguais (na horizontal, vertical ou diagonal).

📝 Estrutura do Código
O código está organizado em funções para manter a legibilidade:

imprimir_tabuleiro(): Renderiza o estado atual do jogo.

verificar_vitoria(): Contém a lógica das 8 combinações vencedoras.

escolha_jogada(): Garante que a entrada do usuário seja um número válido e a posição esteja livre.

🤝 Contribuições
Contribuições são sempre bem-vindas!

Faça um Fork do projeto.

Crie uma Branch para sua feature (git checkout -b feature/NovaFeature).

Dê um Commit nas suas alterações (git commit -m 'Adicionando uma nova funcionalidade').

Dê um Push para a Branch (git push origin feature/NovaFeature).

Abra um Pull Request.

Desenvolvido por [Eduardo Feliciano ] 🚀
