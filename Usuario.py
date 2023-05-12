class Usuario:
    def __init__(self,arroba,nome,tweets,seguidores,seguindo):
        self.arroba = arroba
        self.nome = nome
        self.tweets = tweets
        self.seguidores = seguidores
        self.seguindo = seguindo
    def __str__(self):
       return f"Nome da Página: {self.nome}\nTweets: {self.tweets}\nSeguidores: {self.seguidores}\nSeguindo: {self.seguindo}\nLink:https://twitter.com/{self.arroba}"