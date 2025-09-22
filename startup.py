class Startup:
    def __init__(self, responsavel, email, nome, pitch, tema, cnpj, site="", rede_social=""):
        self.responsavel = responsavel
        self.email = email
        self.nome = nome
        self.pitch = pitch
        self.tema = tema
        self.cnpj = cnpj
        self.site = site
        self.rede_social = rede_social

    def __str__(self):
        return (f"Startup: {self.nome}\n"
                f"Responsável: {self.responsavel}\n"
                f"Email: {self.email}\n"
                f"Tema: {self.tema}\n"
                f"Pitch: {self.pitch}\n")
