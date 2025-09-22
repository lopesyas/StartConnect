from startup import Startup
from investidor import Investidor

class StartConnect:
    def __init__(self):
        self.startups = []
        self.investidores = []
        self.temas = {"1": "Saúde", "2": "Educação", "3": "Meio Ambiente", "4": "Agricultura"}

    def menu_principal(self):
        print("===STARTCONNECT===")
        print("1 - Sou Startup")
        print("2 - Sou Investidor")
        escolha = input("Escolha uma opção: ").strip()
        return escolha

    def cadastrar_startup(self):
        print("\n--- Cadastro de Startup ---")
        responsavel = input("Nome do responsável: ")
        email = input("Email do responsável: ")
        nome = input("Nome da startup: ")

        while True:
            pitch = input("Pitch resumido (até 200 caracteres): ")
            if len(pitch) <= 200:
                break
            else:
                print("Pitch muito longo! Digite até 200 caracteres.")

        print("Tema da startup:")
        for chave, valor in self.temas.items():
            print(f"{chave} - {valor}")
        tema = self.temas.get(input("Escolha o tema (1-4): "), "Não informado")

        cnpj = input("CNPJ da startup: ")
        site = input("Site (opcional): ")
        rede_social = input("Rede social (opcional): ")

        startup = Startup(responsavel, email, nome, pitch, tema, cnpj, site, rede_social)
        self.startups.append(startup)

        print("\nStartup cadastrada com sucesso!\n")

    def cadastrar_investidor(self):
        print("\n--- Cadastro de Investidor ---")
        nome = input("Nome do investidor: ")
        contato = input("Número de contato: ")
        email = input("Email do investidor: ")
        empresa = input("Empresa: ")

        investidor = Investidor(nome, contato, email, empresa)
        self.investidores.append(investidor)

        print("\nCadastro de investidor realizado com sucesso!\n")

        while True:
            print("===Perfil Investidor===")
            print("1 - Procurar Startup")
            print("2 - Sair do programa")
            escolha = input("Escolha uma opção: ").strip()

            if escolha == "2":
                print("Saindo do programa...")
                exit()
            elif escolha == "1":
                self.procurar_startup()
            else:
                print("Opção inválida. Tente novamente.")

    def procurar_startup(self):
        print("\n--- Procurar Startup ---")
        for chave, valor in self.temas.items():
            print(f"{chave} - {valor}")
        escolha = input("Tema desejado (1-4): ")

        tema_desejado = self.temas.get(escolha, None)

        if not tema_desejado:
            print("Opção inválida!")
            return

        print(f"\nStartups no tema {tema_desejado}:")
        encontradas = [s for s in self.startups if s.tema == tema_desejado]

        if encontradas:
            for s in encontradas:
                print(s)
        else:
            print("Nenhuma startup encontrada nesse tema.\n")
