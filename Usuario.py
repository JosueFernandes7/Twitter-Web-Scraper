class Usuario:
    def __init__(self, nome, publicacoes,seguidores,seguindo):
      self.nome = nome
      self.publicacoes = publicacoes
      self.seguindo = seguindo
      self.seguidores = seguidores

    def __str__(self):
       return f"Nome: {self.nome}\nPublicacoes: {self.publicacoes}\nSeguidores: {self.seguidores}\nSeguindo: {self.seguindo}\n"