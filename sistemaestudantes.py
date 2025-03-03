estudantes = {

}
print("-----Sistema de registro de estudantes-----")
print("1. Cadastrar estudante")
print("2. Listar estudantes")
print("3. Buscar estudante por nome")
print("4. Excluir estudante")
print("5. Sair")

while True:
    try:
        seletor = int(input(" \nEscolha uma opção: "))
    except ValueError:
        print("Digite um número de acordo com a opção que deseja escolher!\n ")
        continue
    if seletor == 1:

        nome = input("Digite o nome do estudante: ")
        try:
            idade = int(input(f"digite a idade de {nome}: "))
        except ValueError:
            print("Idade inválida.")
            continue
        estudantes[nome] = (nome, idade)

    elif seletor == 2:
        if len(estudantes) < 1:
            print("Nenhum estudante cadastrado.")
            continue
        print("Estudantes cadastrados:")

        for estudante in estudantes:
            nome, idade = estudantes[estudante]
            print(f"- {nome}, {idade} anos")

    elif seletor == 3:
        busca = input("Digite o nome do estudante a ser buscado: ")
        if not busca in estudantes:
            print(f"Nenhum estudante com o nome '{busca}' encontrado")
            continue
        nome, idade = estudantes[busca]
        print(f"Resultado: {nome}, {idade} anos")

    elif seletor == 4:
        delete = input("Digite o nome do aluno a ser removido: ")
        if not delete in estudantes:
            print(f"Estudante '{delete}' não encontrado.")
            continue
        estudantes.pop(delete)

    elif seletor == 5:
        print("Saindo...")
        break
    elif (seletor < 1) or (seletor > 5):
        print("Opção inexistente, Tente novamente.")
