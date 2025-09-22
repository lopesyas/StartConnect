from startconnect import StartConnect

if __name__ == "__main__":
    app = StartConnect()
    while True:
        escolha = app.menu_principal()
        if escolha == "1":
            app.cadastrar_startup()
        elif escolha == "2":
            app.cadastrar_investidor()
        else:
            print("Opção inválida! Tente novamente.\n")
