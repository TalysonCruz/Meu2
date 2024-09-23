import json

# Função para carregar tarefas de um arquivo JSON
def carregar_tarefas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função para salvar tarefas em um arquivo JSON
def salvar_tarefas(tarefas, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas, descricao):
    tarefas.append({"descricao": descricao, "concluida": False})
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

# Função para listar todas as tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. {tarefa['descricao']} - {status}")

# Função para marcar uma tarefa como concluída
def concluir_tarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print(f"Tarefa '{tarefas[indice]['descricao']}' concluída!")
    else:
        print("Índice inválido.")

# Função para excluir uma tarefa
def excluir_tarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefa = tarefas.pop(indice)
        print(f"Tarefa '{tarefa['descricao']}' excluída!")
    else:
        print("Índice inválido.")

# Função principal que executa o programa
def main():
    nome_arquivo = "tarefas.json"
    tarefas = carregar_tarefas(nome_arquivo)

    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da nova tarefa: ")
            adicionar_tarefa(tarefas, descricao)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a concluir: ")) - 1
            concluir_tarefa(tarefas, indice)
        elif opcao == "4":
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a excluir: ")) - 1
            excluir_tarefa(tarefas, indice)
        elif opcao == "5":
            salvar_tarefas(tarefas, nome_arquivo)
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
