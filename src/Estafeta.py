import math
import random

import Grafo as g


class Estafeta:
    id = 1

    # Initializa um objeto Estafeta
    def __init__(self, nome, veiculo, x, y):
        self.nome = nome
        self.soma_avaliacao = 0
        self.rating = 0
        self.avaliacoes = 0
        self.id = Estafeta.id
        self.veiculo = veiculo
        self.coords_atuais = (x, y)
        self.x = x
        self.y = y
        self.distancia_percorrida = 0
        self.distancia_total_encomendas = 0
        self.encomendas = []
        Estafeta.id += 1

    def __str__(self):
        return f"Nome: {self.nome} | Coordenadas: ({self.x}, {self.y}) | Distância: {self.distancia_total_encomendas}"

    # Retorna o nome do/da Estafeta
    def getnome(self):
        return self.nome

    # Retorna o ID do/da Estafeta
    def getid(self):
        return self.id

    # Retorna o rating do/da Estafeta
    def getrating(self):
        return self.rating

    # Retorna o veiculo do/da Estafeta
    def getveiculo(self):
        return self.veiculo

    # Retorna as coordenadas do/da Estafeta
    def get_coordenadas(self):
        return self.x, self.y

    def get_avaliacoes(self):
        return self.avaliacoes

    def get_soma_avaliacao(self):
        return self.soma_avaliacao

    def get_coords_atuais(self):
        return self.coords_atuais

    def get_distancia_total_encomendas(self):
        return self.distancia_total_encomendas

    def get_distancia_percorrida(self):
        return self.distancia_percorrida

    def get_encomendas(self):
        return self.encomendas

    def add_encomenda(self, encomenda):
        self.encomendas.append(encomenda)

    def atualiza_coordenadas(self, x, y):
        self.x = x
        self.y = y

    def atualiza_coords_atuais(self, x, y):
        self.coords_atuais = (x, y)

    def atualiza_rating(self, prazo, dias_para_entregar):
        if dias_para_entregar <= prazo:
            self.soma_avaliacao += 5
        else:
            self.soma_avaliacao += 5 - 0.5 * (dias_para_entregar - prazo)

        self.avaliacoes += 1
        self.rating = round(self.soma_avaliacao / self.avaliacoes, 2)

    def atualiza_distancia_percorrida(self, distancia):
        self.distancia_percorrida += distancia

    def atualiza_distancia_total_encomendas(self, distancia):
        self.distancia_total_encomendas += distancia

    def velocidade_media(self, peso):
        veiculo = self.veiculo

        if isinstance(veiculo, Carro):
            return veiculo.get_velocidade() - 0.1 * round(peso, 0)
        if isinstance(veiculo, Mota):
            return veiculo.get_velocidade() - 0.5 * round(peso, 0)
        elif isinstance(veiculo, Bicicleta):
            return veiculo.get_velocidade() - 0.6 * round(peso, 0)


class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def get_info_veiculo(self):
        return self.marca, self.modelo

    def get_velocidade(self):
        return self.velocidade

    def set_velocidade(self, velocidade):
        self.velocidade = velocidade


class Bicicleta(Veiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.capacidade = 5
        self.velocidade = 10


class Mota(Veiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.capacidade = 20
        self.velocidade = 35


class Carro(Veiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.capacidade = 100
        self.velocidade = 50


def inicializa_estafetas():
    b1 = Bicicleta("Caloi", "Elite")
    b2 = Bicicleta("Trek", "X-Caliber")
    b3 = Bicicleta("Specialized", "Rockhopper")

    m1 = Mota("Honda", "CBR600RR")
    m2 = Mota("Yamaha", "YZF-R1")
    m3 = Mota("Kawasaki", "Ninja ZX-10R")

    c1 = Carro("Toyota", "Corolla")
    c2 = Carro("Ford", "Fiesta")
    c3 = Carro("Renault", "Megane")

    estafetas = [Estafeta("Albertino Ribeiro", b1, 0, 200),
                 Estafeta("Bernardo Silva", b2, 800, 100),
                 Estafeta("Cláudia Oliveira", b3, 800, 800),
                 Estafeta("David Santos", m1, 200, 200),
                 Estafeta("Eduarda Pereira", m2, 600, 600),
                 Estafeta("Fernando Almeida", m3, 400, 400),
                 Estafeta("Gisela Costa", c1, 200, 300),
                 Estafeta("Hugo Martins", c2, 400, 0),
                 Estafeta("Isabel Oliveira", c3, 50, 700),
                 Estafeta("João Silva", b1, 250, 750),
                 Estafeta("Maria Oliveira", m2, 450, 100),
                 Estafeta("Carlos Mendes", c1, 550, 100),
                 Estafeta("Ana Santos", b3, 500, 50),
                 Estafeta("Rui Martins", m3, 700, 200),
                 Estafeta("Sofia Costa", c2, 362.5, 37.5),
                 Estafeta("Pedro Alves", b2, 0, 0),
                 Estafeta("Carla Pereira", m1, 600, 0),
                 Estafeta("Miguel Oliveira", c3, 0, 800),
                 Estafeta("Teresa Mendes", b1, 0, 400),
                 Estafeta("Ricardo Silva", m2, 450, 550),
                 Estafeta("Felícia Santos", c1, 600, 200),
                 Estafeta("Fábio Martins", b3, 600, 700),
                 Estafeta("Catarina Almeida", m3, 200, 650),
                 Estafeta("Eduardo Costa", c2, 600, 50),
                 Estafeta("Inês Pereira", b2, 800, 700),
                 Estafeta("Nuno Oliveira", m1, 100, 150),
                 Estafeta("Helena Silva", c3, 100, 550),
                 Estafeta("Rita Santos", b1, 450, 450),
                 Estafeta("Diogo Almeida", m2, 300, 300),
                 Estafeta("Michelle Oliveira", c3, 750, 100)
                 ]

    return estafetas


def distancia_estafeta_morada(estafeta, x, y):
    coords_estafeta = estafeta.get_coordenadas()

    distancia = math.sqrt((coords_estafeta[0] - x) ** 2 + (coords_estafeta[1] - y) ** 2)

    return distancia


def distribuir_encomendas(encomendas, estafetas):
    tempo_entrega_esperado = {"Carro": [], "Mota": [], "Bicicleta": []}

    for estafeta in estafetas:
        if isinstance(estafeta.getveiculo(), Carro):
            tempo_entrega_esperado["Carro"].append(estafeta)
        if isinstance(estafeta.getveiculo(), Mota):
            tempo_entrega_esperado["Mota"].append(estafeta)
        elif isinstance(estafeta.getveiculo(), Bicicleta):
            tempo_entrega_esperado["Bicicleta"].append(estafeta)

    for encomenda in encomendas:
        peso = encomenda.get_peso()
        morada = encomenda.get_morada()

        if peso <= 5:
            chave = "Bicicleta"
            lista_tempo = tempo_entrega_esperado.get(chave)
        elif peso <= 20:
            chave = "Mota"
            lista_tempo = tempo_entrega_esperado.get(chave)
        else:
            chave = "Carro"
            lista_tempo = tempo_entrega_esperado.get(chave)

        menor_distancia_total = float("inf")
        ind = -1

        x = round(abs((round(morada.getx1() / 100, 2) + round(morada.getx2() / 100, 2)) / 2), 2)
        y = round(abs((round(morada.gety1() / 100, 2) + round(morada.gety2() / 100, 2)) / 2), 2)
        distancia = 0

        for i, estafeta in enumerate(lista_tempo):
            distancia = distancia_estafeta_morada(estafeta, x, y)
            distancia_total = distancia + estafeta.get_distancia_total_encomendas()

            if distancia_total < menor_distancia_total:
                menor_distancia_total = distancia_total
                ind = i

        estafeta = lista_tempo[ind]
        encomenda.set_estafeta(estafeta)
        aux = estafeta.getid()
        estafetas[aux - 1].atualiza_distancia_total_encomendas(distancia)
        estafetas[aux - 1].add_encomenda(encomenda)
        x1 = morada.getx1()
        x2 = morada.getx2()
        y1 = morada.gety1()
        y2 = morada.gety2()
        estafetas[aux - 1].atualiza_coordenadas((x1 + x2) / 2, (y1 + y2) / 2)
        lista_tempo[ind] = estafetas[aux - 1]

        tempo_entrega_esperado[chave] = lista_tempo


def entrega(nodos, estafetas):
    for estafeta in estafetas:

        for encomenda in estafeta.encomendas:
            morada = encomenda.get_morada()
            peso = encomenda.get_peso()
            prazo = encomenda.get_prazo()
            dias_para_entregar = random.randint(1, 10)
            velocidade = estafeta.velocidade_media(peso)
            coords_estafeta = estafeta.get_coords_atuais()
            encomenda.set_velocidade(velocidade)

            x1 = morada.getx1()
            y1 = morada.gety1()
            x2 = morada.getx2()
            y2 = morada.gety2()
            d1 = distancia_estafeta_morada(estafeta, x1, y1)
            d2 = distancia_estafeta_morada(estafeta, x2, y2)
            inicio = str(coords_estafeta[0]) + "-" + str(coords_estafeta[1])

            if d1 < d2:
                fim = str(x1) + "-" + str(y1)
                distancia, caminho = g.a_estrela(nodos, inicio, fim)
                encomenda.set_caminho(caminho)
                encomenda.set_caminho_estrela(caminho)
                _, caminho2 = g.dfs(nodos, inicio, fim)
                encomenda.set_caminho_dfs(caminho2)
                _, caminho2 = g.bfs(nodos, inicio, fim)
                encomenda.set_caminho_bfs(caminho2)
                _, caminho2 = g.greedy(nodos, inicio, fim)
                encomenda.set_caminho_greedy(caminho2)
                estafeta.atualiza_coords_atuais(x1, y1)
                estafeta.atualiza_distancia_percorrida(round(distancia, 2))

            else:
                fim = str(x2) + "-" + str(y2)
                distancia, caminho = g.a_estrela(nodos, inicio, fim)
                encomenda.set_caminho(caminho)
                encomenda.set_caminho_estrela(caminho)
                _, caminho2 = g.dfs(nodos, inicio, fim)
                encomenda.set_caminho_dfs(caminho2)
                _, caminho2 = g.bfs(nodos, inicio, fim)
                encomenda.set_caminho_bfs(caminho2)
                _, caminho2 = g.greedy(nodos, inicio, fim)
                encomenda.set_caminho_greedy(caminho2)
                estafeta.atualiza_coords_atuais(x2, y2)
                estafeta.atualiza_distancia_percorrida(round(distancia, 2))

            estafeta.atualiza_rating(prazo, dias_para_entregar)
