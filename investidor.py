class Investidor:
    def __init__(self, nome, contato, email, empresa):
        self.nome = nome
        self.contato = contato
        self.email = email
        self.empresa = empresa

    def __str__(self):
        return (f"Investidor: {self.nome}\n"
                f"Contato: {self.contato}\n"
                f"Email: {self.email}\n"
                f"Empresa: {self.empresa}\n")
