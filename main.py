import pickle

from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print("Olá {}, você poderá escolher agora o pokemon que irá lhe acompanhar nessa jornada!".format(player))

    pikachu = PokemonEletrico("Pikachu", level = 1)
    charmander = PokemonFogo("Charmander", level = 1)
    squirtle = PokemonAgua("Squirtle", level = 1)

    print("Você possui 3 escolhas: ")
    print("1", pikachu)
    print("2", charmander)
    print("3", squirtle)

    while True:
        escolha = input("Escolha o seu pokemon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida, tente novamente")

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print(error)

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            ptinr("Loading feito com sucesso")
            return player
    except Exception as error:
        print("Save não encontrado")

if __name__ == "__main__":
    print("---------------------------------------------")
    print("Bem-vindo ao game Pokemon RPG de terminal")
    print("---------------------------------------------")

    player = carregar_jogo()

    if not player:
        nome = input("Olá, qual é o seu nome? ")
        player = Player(nome)
        print("Olá {}, esse é um mundo habitado por pokemons,"
            " a partir de agora sua missão é se tornar um mestre dos pokemons!".format(player))
        print("Capture o máximo de pokemons que conseguir e lute com seus inimigos")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você tem alguns pokemons")
            player.mostrar_pokemons()
        else:
            print("Você não tem nenhum pokemon, portanto precisa escolhe um")
            escolher_pokemon_inicial(player)

        print("Pronto, agora você já possui um pokemon, enfrente seu arqui-rival desde o jardim da infância Gary")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle, level=1")])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("---------------------------------------------")
        print("O que você deseja fazer?")
        print("1 - Explorar pelo mundão a fora")
        print("2 - Lutar com o inimigo")
        print("3 - Ver pokeagenda")
        print("0 - Sair do jogo")
        escolha = input("Sua escolha: ")

        if escolha == "0":
            print("Fechando o jogo...")
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        else:
            print("EScolha inválida")

