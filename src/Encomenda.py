import random
import uuid
import Cidade as c


class Encomenda:

    def __init__(self, peso, volume, prazo, morada):
        self.peso = peso
        self.volume = volume
        self.prazo = prazo
        self.prazo_cumprido = True
        self.morada = morada
        self.estafeta = None
        self.velocidade = 0
        self.caminho = []
        self.caminho_estrela = []
        self.caminho_dfs = []
        self.caminho_bfs = []
        self.caminho_greedy = []
        self.id = str(uuid.uuid4()).replace('-', '')

    def get_id(self):
        return self.id

    def get_peso(self):
        return self.peso

    def get_prazo(self):
        return self.prazo

    def get_prazo_cumprido(self):
        return self.prazo_cumprido

    def get_volume(self):
        return self.volume

    def get_morada(self):
        return self.morada

    def set_estafeta(self, estafeta):
        self.estafeta = estafeta

    def get_estafeta(self):
        return self.estafeta

    def set_velocidade(self, velocidade):
        self.velocidade = velocidade

    def get_caminho(self):
        return self.caminho

    def get_caminho_estrela(self):
        return self.caminho_estrela
    
    def get_caminho_dfs(self):
        return self.caminho_dfs
    
    def get_caminho_bfs(self):
        return self.caminho_bfs
    
    def get_caminho_greedy(self):
        return self.caminho_greedy
    
    def set_caminho(self, caminho):
        self.caminho = caminho
    
    def set_caminho_estrela(self, caminho):
        self.caminho_estrela = caminho

    def set_caminho_dfs(self, caminho):
        self.caminho_dfs = caminho
    
    def set_caminho_bfs(self, caminho):
        self.caminho_bfs = caminho

    def set_caminho_greedy(self, caminho):
        self.caminho_greedy = caminho
    
    def __str__(self):
        morada = self.morada
        morada.__str__()
        return f'ID - {self.id} | Peso: {self.peso} | Morada: {self.morada} | Estafeta: {self.estafeta.getnome()})'


def inicializa_encomendas(mapa):
    ruas = mapa.get_ruas()
    encomendas = []
    for _ in range(1000):
        peso = round(random.uniform(0, 100), 2)
        volume = peso * 50
        prazo = random.randint(1, 10)
        morada = random.choice(ruas[2:])
        nova_encomenda = Encomenda(peso, volume, prazo, morada)
        encomendas.append(nova_encomenda)

    return encomendas

