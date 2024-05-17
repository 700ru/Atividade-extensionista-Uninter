def simular_dados_empregos():
    empregos = []
    for i in range(1, 6):
        emprego = {"id": i, "titulo": f"Emprego {i}"}
        empregos.append(emprego)
    return empregos

def simular_dados_cursos():
    cursos = []
    for i in range(1, 6):
        curso = {"id": i, "nome": f"Curso {i}"}
        cursos.append(curso)
    return cursos

def main():
    print("Bem-vindo ao Projeto ADA!")

    usuario = input('Digite o seu usuario no sistema: ')
    senha = input('Digite a senha de seu usuario no sistema: ')

    escolha = input("Escolha o que deseja buscar (1 para empregos, 2 para cursos): ")

    if escolha == "1":
        empregos = simular_dados_empregos()
        print("Lista de Empregos:")
        for emprego in empregos:
            print(f"ID: {emprego['id']}, Título: {emprego['titulo']}")
    elif escolha == "2":
        cursos = simular_dados_cursos()
        print("Lista de Cursos:")
        for curso in cursos:
            print(f"ID: {curso['id']}, Nome do Curso: {curso['nome']}")
    else:
        print("Escolha inválida. Por favor, escolha 1 para empregos ou 2 para cursos.")

if __name__ == "__main__":
    main()