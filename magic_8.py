# Importamos o módulo random para trabalhar com números aleatórios.
import random

# Exibimos uma mensagem inicial para orientar o usuário.
print("Bem-vindo à Magic 8 Ball!")
print("Faça uma pergunta e receba sua resposta. Digite 'sair' para encerrar o programa.\n")

# Usamos um loop while para repetir o processo de perguntas e respostas.
# Esse loop continuará até que o usuário digite 'sair'.
while True:
    # Solicitamos ao usuário que faça uma pergunta.
    question = input("Pergunta:      ")

    # Se o usuário digitar 'sair', interrompemos o loop com break.
    if question.lower() == "sair":
        print("Obrigado por usar a Magic 8 Ball! Até mais!")
        break

    # Geramos um número aleatório entre 1 e 9.
    random_number = random.randint(1, 9)

    # Usamos uma estrutura de decisão (if/elif/else) para definir
    # a resposta com base no número gerado.
    if random_number == 1:
        answer = "Sim - definitivamente."
    elif random_number == 2:
        answer = "É decididamente assim."
    elif random_number == 3:
        answer = "Sem dúvida."
    elif random_number == 4:
        answer = "Resposta vaga, tente novamente."
    elif random_number == 5:
        answer = "Pergunte novamente mais tarde."
    elif random_number == 6:
        answer = "Melhor não te contar agora."
    elif random_number == 7:
        answer = "Minhas fontes dizem que não."
    elif random_number == 8:
        answer = "O futuro não é bom."
    else:  # Caso o número seja 9
        answer = "Muito duvidoso."

    # Exibimos a resposta da Magic 8 Ball.
    print(f"Magic 8 Ball: {answer}\n")
