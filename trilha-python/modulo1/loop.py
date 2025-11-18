def menu_voltar_sair(nome):
    while True:
        opcao_voltar_sair = input("\nDigite [1] para encerrar o atendimento ou [2] para voltar ao menu anterior: ")
        if opcao_voltar_sair == "1":
            print(f"Obrigado {nome} por usar nosso atendimento. Volte sempre!")
            exit()
        elif opcao_voltar_sair == "2":
            break
        else:
            print("Insira uma opção válida")


def sair(nome):
    print(f"Obrigado {nome} por usar nosso atendimento. Volte sempre!")
    exit()

print("Olá! Seja Bem vindo a loja SQUAD 3\n")
nome = input("Como você gostaria de ser chamado(a)? ").title()

#LOOP PRINCIPAL
while True:
    #MENU PRINCIPAL 
    opcoes = input(
        f"\n{nome}, em que podemos te ajudar?\n"
        "[1] Entregas\n"
        "[2] Pedidos e Pagamentos\n"
        "[3] Trocas e Devolução\n"
        "[4] Produtos\n"
        "[5] Cadastro\n"
        "[6] Encerrar Atendimento\n"
        "Insira o número do atendimento que deseja: "
    )
    
    if opcoes == "1": #ENTRA NO LOOP OPÇÃO ENTREGAS
        while True:
            opcao_entregas = input(
                "\nQual a sua dúvida sobre entregas:\n"
                "[1] Como rastrear meu pedido?\n"
                "[2] Qual o prazo de entrega do meu pedido?\n"
                "[3] Como alterar meu endereço de entrega?\n"
                "[4] Encerrar atendimento\n"
                "[5] Voltar ao menu anterior\n"
                "\nInsira o número referente a sua dúvida: "
            )
            if opcao_entregas == "1": #COMO RASTREAR PEDIDO
                print("\nDentro de “Minha conta” clique em “Meus pedidos” e procure pela sua comprinha. Elas estão organizadas pelo número de identificação. Para ver mais detalhes clique em VER DETALHES. O código de rastreio deve aparecer logo abaixo do resumo da sua compra. Mas lembre-se que ele aparece de formas diferentes dependendo da forma de entrega que você selecionou. Com o código de rastreio em mãos, basta você localizar a sua comprinha no site dos Correios.")
                menu_voltar_sair(nome)
            elif opcao_entregas == "2": #PRAZO DE ENTREGA
                print("\nO prazo de entrega vai depender do seu estado.")
                menu_voltar_sair(nome)
            elif opcao_entregas == "3": #ALTERAR ENDEREÇO DE ENTREGA
                print("\nOs Correios não permitem que a gente altere nenhuma informação após o despacho da sua comprinha. Por isso, vamos ter que aguardar a sua comprinha retornar para a nossa loja para um novo despacho.")
                menu_voltar_sair(nome)
            elif opcao_entregas == "4": #ENCERRAR ATENDIMENTO
                sair(nome)
            elif opcao_entregas == "5": #VOLTAR AO MENU ANTERIOR
                break
            else: 
                print("Por favor, insira uma opção válida: ")

        