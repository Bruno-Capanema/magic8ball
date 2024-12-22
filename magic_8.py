# Importa o módulo random para gerar números aleatórios
import random

# Exibe uma mensagem de boas-vindas
print("Bem-vindo à Magic 8 Ball!")
print("Faça uma pergunta e receba sua resposta. Digite 'sair' para encerrar o programa.\n")

# Inicia um loop que ficará perguntando até o usuário digitar 'sair'
while True:
    # Solicita uma pergunta ao usuário
    question = input("Pergunta: ")
    
    # Se o usuário digitar 'sair', encerra o programa
    if question.lower() == "sair":
        print("Obrigado por usar a Magic 8 Ball! Até mais!")
        break

    # Gera um número aleatório de 1 a 9
    random_number = random.randint(1, 9)

    # Define a resposta com base no número gerado
    respostas = {
        1: "Sim - definitivamente.",
        2: "É decididamente assim.",
        3: "Sem dúvida.",
        4: "Resposta vaga, tente novamente.",
        5: "Pergunte novamente mais tarde.",
        6: "Melhor não te contar agora.",
        7: "Minhas fontes dizem que não.",
        8: "O futuro não é bom.",
        9: "Muito duvidoso."
    }

    # Exibe a resposta correspondente ao número gerado
    print(f"Magic 8 Ball: {respostas[random_number]}\n")
