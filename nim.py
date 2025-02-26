import random

class NimGame:
    def __init__(self):
        self.piles = [3, 4, 5]
        self.current_player = None
        self.last_player = None  

    def display_piles(self):
        print("\nEstado atual das pilhas:")
        for i, pile in enumerate(self.piles):
            print(f"Pilha {i + 1}: {pile} palitos")

    def check_game_over(self):
        return all(pile == 0 for pile in self.piles)

    def player_move(self, player_name):
        while True:
            try:
                pile = int(input(f"\n{player_name}, escolha a pilha (1, 2 ou 3): ")) - 1
                if pile not in [0, 1, 2]:
                    print("Escolha uma pilha válida.")
                    continue
                
                if self.piles[pile] == 0:
                    print("Essa pilha está vazia. Escolha outra.")
                    continue
                
                num = int(input("Quantos palitos deseja remover? "))
                if num < 1 or num > self.piles[pile]:
                    print("Número inválido de palitos.")
                    continue
                
                self.piles[pile] -= num
                print(f"{player_name} removeu {num} palitos da pilha {pile + 1}.")
                self.last_player = player_name  # Atualiza o último jogador
                break
            
            except ValueError:
                print("Entrada inválida. Tente novamente.")

    def computer_move(self):
        while True:
            pile = random.choice([0, 1, 2])
            if self.piles[pile] > 0:
                num = random.randint(1, self.piles[pile])
                self.piles[pile] -= num
                print(f"\nMáquina removeu {num} palitos da pilha {pile + 1}.")
                self.last_player = "Máquina"  # Atualiza o último jogador
                break

    def play(self):
        print("Bem-vindo ao jogo Nim!")
        print("Modo de jogo:")
        print("1. Player vs Player")
        print("2. Player vs Máquina")
        
        while True:
            mode = input("Escolha o modo (1 ou 2): ")
            if mode in ['1', '2']:
                break
            print("Escolha inválida. Tente novamente.")
        
        player1 = input("Nome do Player 1: ")
        player2 = "Máquina" if mode == '2' else input("Nome do Player 2: ")

        self.current_player = player1

        while True:
            self.display_piles()
            
            # Jogada do Player 1
            if self.current_player == player1:
                self.player_move(player1)
                if self.check_game_over():
                    print(f"\n{player1} pegou o último palito e perdeu!")
                    break
                self.current_player = player2
            
            # Jogada do Player 2 (ou Máquina)
            else:
                if player2 == "Máquina":
                    self.computer_move()
                else:
                    self.player_move(player2)
                
                if self.check_game_over():
                    print(f"\n{player2} pegou o último palito e perdeu!")
                    break
                self.current_player = player1

        self.display_piles()
        print("\nFim do jogo!")

# Executando o jogo
if __name__ == "__main__":
    game = NimGame()
    game.play()
