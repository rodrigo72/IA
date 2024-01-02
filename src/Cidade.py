import tkinter as tk
from tkinter import ttk
from Menu import Menu

linha_anterior = None

class Freguesia:

    def __init__(self, nome, y1, x1, y2, x2):
        self.nome = nome
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2

    def get_nome(self):
        return self.nome

    def getx1(self):
        return self.x1

    def getx2(self):
        return self.x2

    def gety1(self):
        return self.y1

    def gety2(self):
        return self.y2


class Rua:

    def __init__(self, nome, y1, x1, y2, x2, velocidade_maxima, freguesia):
        self.nome = nome
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.velocidade_maxima = velocidade_maxima
        self.freguesia = freguesia

    def get_nome(self):
        return self.nome

    def getx1(self):
        return self.x1

    def getx2(self):
        return self.x2

    def gety1(self):
        return self.y1

    def gety2(self):
        return self.y2

    def get_velocidade_maxima(self):
        return self.velocidade_maxima

    def get_freguesia(self):
        return self.freguesia

    def __str__(self):
        return f'{self.nome}, {self.freguesia}'


class Mapa:

    def __init__(self, nome, ruas):
        self.nome = nome
        self.ruas = ruas
        self.moradas = None
        self.freguesias = [
            Freguesia("Gualtar", 0, 0, 200, 200),
            Freguesia("Belos e Belas", 200, 0, 400, 200),
            Freguesia("La Casa Rosa", 400, 0, 600, 200),
            Freguesia("Sucupira", 600, 0, 800, 200),
            Freguesia("Lagoa Azul", 0, 200, 200, 400),
            Freguesia("Monte Verde", 200, 200, 400, 400),
            Freguesia("Fonte Serena", 400, 200, 600, 400),
            Freguesia("Serra Dourada", 600, 200, 800, 400),
            Freguesia("Nova Primavera", 0, 400, 200, 600),
            Freguesia("Belo Horizonte", 200, 400, 400, 600),
            Freguesia("Sol Nascente", 400, 400, 600, 600),
            Freguesia("Porto do Sol", 600, 400, 800, 600),
            Freguesia("Pedras do Mar", 0, 600, 200, 800),
            Freguesia("Terras da Aurora", 200, 600, 400, 800),
            Freguesia("Jardim da Lua", 400, 600, 600, 800),
            Freguesia("Vale da Paz", 600, 600, 800, 800),
        ]

    def get_nome(self):
        return self.nome

    def get_ruas(self) -> [Rua]:
        return self.ruas

    def get_freguesias(self):
        return self.freguesias

def obter_tag_morada(nome, freguesia, moradas):

    for morada in moradas:
        if nome == morada.get_nome() and freguesia == morada.get_freguesia():
            return str(morada.gety1() + 25) + str(morada.getx1() + 40) + str(morada.gety2() + 25) + str(morada.getx2() + 40)

    return None


def inicializa_mapa():

    ruas = [
        Rua("AutoEstrada1", 0, 0, 800, 0, 80, "A1"),
        Rua("AutoEstrada2", 400, 0, 400, 800, 80, "A2"),
        Rua("Avenida da Liberdade", 0, 0, 0, 200, 80, "Gualtar"),
        Rua("Avenida da Liberdade", 0, 200, 0, 400, 80, "Lagoa Azul"),
        Rua("Avenida da Liberdade", 0, 400, 0, 600, 80, "Nova Primavera"),
        Rua("Avenida da Liberdade", 0, 600, 0, 800, 80, "Pedras do Mar"),
        Rua("Avenida da Esperança", 0, 800, 200, 800, 80, "Pedras do Mar"),
        Rua("Avenida da Esperança", 200, 800, 400, 800, 80, "Terras da Aurora"),
        Rua("Avenida da Esperança", 400, 800, 600, 800, 80, "Jardim da Lua"),
        Rua("Avenida da Esperança", 600, 800, 800, 800, 80, "Vale da Paz"),
        Rua("Avenida D.Afonso Henriques", 800, 0, 800, 200, 80, "Sucupira"),
        Rua("Avenida D.Afonso Henriques", 800, 200, 800, 400, 80, "Serra Dourada"),
        Rua("Avenida D.Afonso Henriques", 800, 400, 800, 600, 80, "Porto do Sol"),
        Rua("Avenida D.Afonso Henriques", 800, 600, 800, 800, 80, "Vale da Paz"),
        Rua("Avenida Central", 0, 400, 200, 400, 80, "Lagoa Azul"),
        Rua("Avenida Central", 200, 400, 400, 400, 80, "Monte Verde"),
        Rua("Avenida Central", 400, 400, 600, 400, 80, "Fonte Serena"),
        Rua("Avenida Central", 600, 400, 800, 400, 80, "Serra Dourada"),
        Rua("Avenida Central", 0, 400, 200, 400, 80, "Nova Primavera"),
        Rua("Avenida Central", 200, 400, 400, 400, 80, "Belo Horizonte"),
        Rua("Avenida Central", 400, 400, 600, 400, 80, "Sol Nascente"),
        Rua("Avenida Central", 600, 400, 800, 400, 80, "Porto do Sol"),
        Rua("Avenida João Paulo II", 0, 600, 200, 600, 80, "Nova Primavera"),
        Rua("Avenida João Paulo II", 200, 600, 400, 600, 80, "Belo Horizonte"),
        Rua("Avenida João Paulo II", 400, 600, 600, 600, 80, "Sol Nascente"),
        Rua("Avenida João Paulo II", 600, 600, 800, 600, 80, "Porto do Sol"),
        Rua("Avenida João Paulo II", 0, 600, 200, 600, 80, "Pedras do Mar"),
        Rua("Avenida João Paulo II", 200, 600, 400, 600, 80, "Terras da Aurora"),
        Rua("Avenida João Paulo II", 400, 600, 600, 600, 80, "Jardim da Lua"),
        Rua("Avenida João Paulo II", 600, 600, 800, 600, 80, "Vale da Paz"),
        Rua("Avenida Egas Moniz", 0, 200, 200, 200, 80, "Gualtar"),
        Rua("Avenida Egas Moniz", 200, 200, 400, 200, 80, "Belos e Belas"),
        Rua("Avenida Egas Moniz", 400, 200, 600, 200, 80, "La Casa Rosa"),
        Rua("Avenida Egas Moniz", 600, 200, 800, 200, 80, "Sucupira"),
        Rua("Avenida Egas Moniz", 0, 200, 200, 200, 80, "Lagoa Azul"),
        Rua("Avenida Egas Moniz", 200, 200, 400, 200, 80, "Monte Verde"),
        Rua("Avenida Egas Moniz", 400, 200, 600, 200, 80, "Fonte Serena"),
        Rua("Avenida Egas Moniz", 600, 200, 800, 200, 80, "Serra Dourada"),
        Rua("Avenida Bela", 200, 0, 200, 200, 80, "Gualtar"),
        Rua("Avenida Bela", 200, 0, 200, 200, 80, "Belos e Belas"),
        Rua("Avenida Bela", 200, 200, 200, 400, 80, "Lagoa Azul"),
        Rua("Avenida Bela", 200, 200, 200, 400, 80, "Monte Verde"),
        Rua("Avenida Bela", 200, 400, 200, 600, 80, "Nova Primavera"),
        Rua("Avenida Bela", 200, 400, 200, 600, 80, "Belo Horizonte"),
        Rua("Avenida Bela", 200, 600, 200, 800, 80, "Pedras do Mar"),
        Rua("Avenida Bela", 200, 600, 200, 800, 80, "Terras da Aurora"),
        Rua("Avenida das Palmeiras", 600, 0, 600, 200, 80, "La Casa Rosa"),
        Rua("Avenida das Palmeiras", 600, 0, 600, 200, 80, "Sucupira"),
        Rua("Avenida das Palmeiras", 600, 200, 600, 400, 80, "Fonte Serena"),
        Rua("Avenida das Palmeiras", 600, 200, 600, 400, 80, "Serra Dourada"),
        Rua("Avenida das Palmeiras", 600, 400, 600, 600, 80, "Sol Nascente"),
        Rua("Avenida das Palmeiras", 600, 400, 600, 600, 80, "Porto do Sol"),
        Rua("Avenida das Palmeiras", 600, 600, 600, 800, 80, "Jardim da Lua"),
        Rua("Avenida das Palmeiras", 600, 600, 600, 800, 80, "Vale da Paz"),
        Rua("Travessa dos Girassóis", 0, 50, 50, 50, 80, "Gualtar"),
        Rua("Rua dos Pinheiros", 50, 50, 50, 150, 80, "Gualtar"),
        Rua("Travessa da Amizade", 50, 50, 100, 50, 80, "Gualtar"),
        Rua("Rua do Bosque", 0, 100, 50, 100, 80, "Gualtar"),
        Rua("Rua das Oliveiras", 100, 50, 150, 50, 80, "Gualtar"),
        Rua("Rua Impetuosa", 100, 50, 100, 100, 80, "Gualtar"),
        Rua("Alameda dos Cravos", 150, 50, 150, 100, 80, "Gualtar"),
        Rua("Rua da Felicidade", 50, 100, 100, 100, 80, "Gualtar"),
        Rua("Alameda dos Sabiás", 100, 100, 100, 200, 80, "Gualtar"),
        Rua("Travessa das Maravilhas", 150, 100, 200, 100, 80, "Gualtar"),
        Rua("Travessa das Borboletas", 150, 100, 150, 200, 80, "Gualtar"),
        Rua("Rua das Cachoeiras", 150, 100, 100, 150, 80, "Gualtar"),
        Rua("Alameda dos Flamboyants", 0, 150, 100, 150, 80, "Gualtar"),
        Rua("Alameda dos Diamantes", 200, 100, 300, 100, 80, "Belos e Belas"),
        Rua("Travessa das Fadas", 300, 100, 300, 200, 80, "Belos e Belas"),
        Rua("Rua dos Sonhos", 300, 150, 250, 150, 80, "Belos e Belas"),
        Rua("Alameda das Pedras", 250, 150, 250, 200, 80, "Belos e Belas"),
        Rua("Travessa dos Poetas", 200, 50, 400, 50, 80, "Belos e Belas"),
        Rua("Rua das Lembranças", 350, 50, 300, 100, 80, "Belos e Belas"),
        Rua("Rua da Felicidade", 350, 50, 350, 150, 80, "Belos e Belas"),
        Rua("Rua das Virtudes", 300, 150, 400, 150, 80, "Belos e Belas"),
        Rua("Rua dos Anjos", 300, 0, 300, 50, 80, "Belos e Belas"),
        Rua("Rua das Inocências", 400, 50, 600, 50, 80, "La Casa Rosa"),
        Rua("Alameda dos Instantes", 500, 50, 500, 200, 80, "La Casa Rosa"),
        Rua("Travessa das Iluminuras", 450, 50, 400, 150, 80, "La Casa Rosa"),
        Rua("Rua das Íris", 450, 50, 450, 150, 80, "La Casa Rosa"),
        Rua("Alameda das Imagens", 450, 150, 400, 150, 80, "La Casa Rosa"),
        Rua("Travessa dos Jardins Secretos", 450, 150, 500, 200, 80, "La Casa Rosa"),
        Rua("Rua das Janelas", 450, 100, 500, 100, 80, "La Casa Rosa"),
        Rua("Alameda dos Júbilos", 500, 100, 600, 100, 80, "La Casa Rosa"),
        Rua("Rua das Melodias", 550, 100, 550, 200, 80, "La Casa Rosa"),
        Rua("Rua das Íris", 650, 0, 650, 200, 80, "Sucupira"),
        Rua("Alameda das Imagens", 600, 100, 650, 100, 80, "Sucupira"),
        Rua("Rua das Oliveiras", 650, 100, 725, 150, 80, "Sucupira"),
        Rua("Rua dos Pinheiros", 650, 100, 800, 100, 80, "Sucupira"),
        Rua("Travessa dos Tesouros", 800, 100, 725, 150, 80, "Sucupira"),
        Rua("Rua das Tradições", 650, 200, 725, 150, 80, "Sucupira"),
        Rua("Alameda dos Trilhos", 725, 150, 800, 200, 80, "Sucupira"),
        Rua("Travessa dos Ventos", 650, 50, 800, 50, 80, "Sucupira"),
        Rua("Rua das Virtudes", 700, 50, 700, 100, 80, "Sucupira"),
        Rua("Alameda dos Viajantes", 750, 50, 750, 100, 80, "Sucupira"),
        Rua("Travessa dos Vales Verdejantes", 150, 200, 150, 400, 80, "Lagoa Azul"),
        Rua("Rua das Verdades", 0, 250, 200, 250, 80, "Lagoa Azul"),
        Rua("Alameda dos Velhos Tempos", 150, 250, 0, 400, 80, "Lagoa Azul"),
        Rua("Travessa dos Vaga-lumes", 75, 325, 150, 400, 80, "Lagoa Azul"),
        Rua("Rua das Voltas", 75, 250, 75, 325, 80, "Lagoa Azul"),
        Rua("Travessa das Nuvens", 75, 250, 0, 325, 80, "Lagoa Azul"),
        Rua("Rua das Canções", 0, 325, 37.5, 362.5, 80, "Lagoa Azul"),
        Rua("Rua das Lembranças", 150, 350, 200, 350, 80, "Lagoa Azul"),
        Rua("Rua São Rodrigo", 200, 300, 400, 300, 80, "Monte Verde"),
        Rua("Rua São Luís", 300, 200, 300, 400, 80, "Monte Verde"),
        Rua("Rua São Diogo", 250, 300, 250, 400, 80, "Monte Verde"),
        Rua("Rua São Miguel", 250, 350, 300, 350, 80, "Monte Verde"),
        Rua("Rua da Felicidade", 300, 350, 400, 350, 80, "Monte Verde"),
        Rua("Travessa Amarela", 300, 350, 350, 300, 80, "Monte Verde"),
        Rua("Rua das Cruzes", 300, 350, 350, 400, 80, "Monte Verde"),
        Rua("Alameda das Pedras", 200, 250, 300, 250, 80, "Monte Verde"),
        Rua("Alameda dos Trilhos", 300, 250, 400, 250, 80, "Monte Verde"),
        Rua("Avenida dos Banhos", 400, 300, 600, 300, 80, "Fonte Serena"),
        Rua("Avenida Central", 500, 200, 500, 400, 80, "Fonte Serena"),
        Rua("Avenida D.João I", 400, 200, 600, 400, 80, "Fonte Serena"),
        Rua("Avenida Vermelha", 400, 400, 600, 200, 80, "Fonte Serena"),
        Rua("Rua das Acácias", 600, 300, 700, 200, 80, "Serra Dourada"),
        Rua("Avenida do Sol Nascente", 600, 400, 800, 200, 80, "Serra Dourada"),
        Rua("Travessa da Serenidade", 700, 400, 800, 300, 80, "Serra Dourada"),
        Rua("Alameda das Flores", 600, 300, 700, 400, 80, "Serra Dourada"),
        Rua("Praça das Artes", 600, 200, 800, 400, 80, "Serra Dourada"),
        Rua("Caminho da Liberdade", 700, 200, 800, 300, 80, "Serra Dourada"),
        Rua("Rua D.Pedro I", 100, 400, 100, 550, 80, "Nova Primavera"),
        Rua("Travessa dos Pedreiros", 0, 550, 200, 550, 80, "Nova Primavera"),
        Rua("Rua Francisco Sá Carneiro", 0, 400, 100, 500, 80, "Nova Primavera"),
        Rua("Rua Universidade do Minho", 0, 500, 100, 500, 80, "Nova Primavera"),
        Rua("Rua Eduardo Pereira", 50, 500, 50, 550, 80, "Nova Primavera"),
        Rua("Rua das Oliveiras", 50, 550, 50, 600, 80, "Nova Primavera"),
        Rua("Rua dos Pinheiros", 50, 450, 0, 450, 80, "Nova Primavera"),
        Rua("Travessa dos Tesouros", 100, 450, 200, 450, 80, "Nova Primavera"),
        Rua("Travessa do Parque Agradável", 150, 450, 150, 550, 80, "Nova Primavera"),
        Rua("Rua da Paz", 350, 400, 350, 600, 80, "Belo Horizonte"),
        Rua("Avenida das Flores", 250, 400, 250, 600, 80, "Belo Horizonte"),
        Rua("Travessa dos Pássaros", 200, 450, 400, 450, 80, "Belo Horizonte"),
        Rua("Caminho da Esperança", 200, 550, 400, 550, 80, "Belo Horizonte"),
        Rua("Alameda do Sol", 250, 500, 300, 500, 80, "Belo Horizonte"),
        Rua("Passagem da Harmonia", 300, 450, 300, 500, 80, "Belo Horizonte"),
        Rua("Estrada da Serenidade", 300, 500, 300, 550, 80, "Belo Horizonte"),
        Rua("Caminho das Estrelas", 300, 500, 350, 500, 80, "Belo Horizonte"),
        Rua("Travessa do Bosque", 400, 500, 600, 500, 80, "Sol Nascente"),
        Rua("Rua das Rosas", 450, 500, 450, 400, 80, "Sol Nascente"),
        Rua("Alameda da Lua", 400, 450, 450, 450, 80, "Sol Nascente"),
        Rua("Estrada do Horizonte", 500, 500, 500, 600, 80, "Sol Nascente"),
        Rua("Caminho do Silêncio", 500, 500, 400, 600, 80, "Sol Nascente"),
        Rua("Caminho das Maravilhas", 500, 500, 600, 600, 80, "Sol Nascente"),
        Rua("Passagem da Montanha", 450, 550, 550, 550, 80, "Sol Nascente"),
        Rua("Avenida da Alegria", 550, 550, 550, 500, 80, "Sol Nascente"),
        Rua("Rua do Riacho", 550, 500, 550, 450, 80, "Sol Nascente"),
        Rua("Travessa da Amizade", 550, 450, 500, 450, 80, "Sol Nascente"),
        Rua("Estrada do Crepúsculo", 500, 450, 450, 500, 80, "Sol Nascente"),
        Rua("Rua das Lembranças", 450, 450, 500, 450, 80, "Sol Nascente"),
        Rua("Rua da Aurora", 600, 450, 800, 450, 80, "Porto do Sol"),
        Rua("Avenida do Crepúsculo", 600, 500, 800, 500, 80, "Porto do Sol"),
        Rua("Travessa do Jardim", 600, 550, 800, 550, 80, "Porto do Sol"),
        Rua("Alameda da Sombra", 650, 400, 650, 600, 80, "Porto do Sol"),
        Rua("Caminho da Solidariedade", 700, 400, 700, 600, 80, "Porto do Sol"),
        Rua("Passagem da Tranquilidade", 750, 400, 750, 600, 80, "Porto do Sol"),
        Rua("Rua Infante Dom Henrique", 100, 600, 100, 800, 80, "Pedras do Mar"),
        Rua("Travessa Vasco da Gama", 100, 750, 50, 800, 80, "Pedras do Mar"),
        Rua("Rua Luís de Camões", 100, 750, 150, 800, 80, "Pedras do Mar"),
        Rua("Alameda Amália Rodrigues", 0, 700, 200, 700, 80, "Pedras do Mar"),
        Rua("Caminho Fernando Pessoa", 150, 650, 150, 700, 80, "Pedras do Mar"),
        Rua("Passagem Salgueiro Maia", 150, 700, 150, 750, 80, "Pedras do Mar"),
        Rua("Estrada Marquês de Pombal", 150, 650, 200, 650, 80, "Pedras do Mar"),
        Rua("Rua Sophia de Mello Breyner", 150, 750, 200, 750, 80, "Pedras do Mar"),
        Rua("Avenida José Saramago", 50, 600, 50, 800, 80, "Pedras do Mar"),
        Rua("Avenida Dom Afonso Henriques", 200, 700, 250, 700, 80, "Terras da Aurora"),
        Rua("Travessa Inês de Castro", 250, 650, 250, 750, 80, "Terras da Aurora"),
        Rua("Rua Fernão Mendes Pinto", 250, 650, 350, 650, 80, "Terras da Aurora"),
        Rua("Alameda Egas Moniz", 350, 650, 350, 750, 80, "Terras da Aurora"),
        Rua("Caminho D. Dinis", 250, 750, 350, 750, 80, "Terras da Aurora"),
        Rua("Passagem Pedro Álvares Cabral", 350, 700, 400, 700, 80, "Terras da Aurora"),
        Rua("Estrada Maria de Lourdes Pintasilgo", 300, 650, 300, 750, 80, "Terras da Aurora"),
        Rua("Rua Aristides de Sousa Mendes", 300, 750, 250, 800, 80, "Terras da Aurora"),
        Rua("Avenida António de Oliveira Salazar", 300, 750, 350, 800, 80, "Terras da Aurora"),
        Rua("Rua Viriato", 300, 650, 250, 600, 80, "Terras da Aurora"),
        Rua("Travessa Florbela Espanca", 300, 650, 350, 600, 80, "Terras da Aurora"),
        Rua("Avenida do Riso Fácil", 500, 600, 500, 800, 80, "Jardim da Lua"),
        Rua("Travessa das Piadas Infinitas", 500, 700, 400, 700, 80, "Jardim da Lua"),
        Rua("Rua do Trocadilho Feliz", 500, 650, 600, 650, 80, "Jardim da Lua"),
        Rua("Alameda do Humor Sutil", 500, 750, 600, 750, 80, "Jardim da Lua"),
        Rua("Caminho da Gargalhada Eterna", 500, 650, 450, 650, 80, "Jardim da Lua"),
        Rua("Passagem das Anedotas Alegres", 500, 750, 450, 750, 80, "Jardim da Lua"),
        Rua("Estrada da Zona Cómica", 450, 600, 450, 800, 80, "Jardim da Lua"),
        Rua("Rua do Sorriso Contagiante", 550, 650, 550, 750, 80, "Jardim da Lua"),
        Rua("Avenida da Seriedade", 600, 700, 700, 600, 80, "Vale da Paz"),
        Rua("Travessa da Responsabilidade", 600, 700, 700, 800, 80, "Vale da Paz"),
        Rua("Rua da Disciplina", 700, 600, 800, 700, 80, "Vale da Paz"),
        Rua("Alameda do Compromisso", 700, 800, 800, 700, 80, "Vale da Paz"),
        Rua("Caminho da Ética", 650, 650, 750, 750, 80, "Vale da Paz"),
        Rua("Passagem da Integridade", 650, 750, 750, 650, 80, "Vale da Paz"),
        Rua("Estrada da Dedicação", 650, 600, 650, 800, 80, "Vale da Paz"),
        Rua("Rua da Resiliência", 750, 600, 750, 800, 80, "Vale da Paz")
    ]

    mapa = Mapa("Cidade dos Belos", ruas)

    return mapa


def adicionar_barra_pesquisa(root, mapa, canvas, menu):
    def morada_selecionada(event, moradas):
        global linha_anterior
        morada = combobox.get()
        nome, freguesia = morada.split(', ')
        linha_selecionada = "aa" + obter_tag_morada(nome, freguesia, moradas)


        if linha_anterior is not None:
            canvas.itemconfig(linha_anterior, fill="black")

        if linha_selecionada is not None:
            canvas.itemconfig(linha_selecionada, fill="red")

        linha_anterior = linha_selecionada

    titulo = tk.Label(root, text="HEALTH PLANET", font=("Helvetica", 40, "bold"), bg="white")
    titulo.configure(highlightthickness=0, bg="white")
    titulo.place(x=60, y=20)

    label = tk.Label(root, text="Moradas da Cidade dos Belos:")
    label.configure(highlightthickness=0, bg="white")
    label.place(x=200, y=200)

    combobox_var = tk.StringVar()
    combobox = ttk.Combobox(root, width=65, textvariable=combobox_var)

    moradas = mapa.get_ruas()

    combobox['values'] = [f'{morada.get_nome()}, {morada.get_freguesia()}' for morada in moradas]
    combobox.place(x=80, y=300)

    combobox.bind("<<ComboboxSelected>>", lambda event: morada_selecionada(event, moradas))

def desenha_mapa(mapa, canvas):
    ruas = mapa.get_ruas()

    for rua in ruas:
        velocidade = rua.get_velocidade_maxima()
        if velocidade == 120:
            largura = 5
        else:
            largura = 3

        y1 = rua.gety1() + 25
        x1 = rua.getx1() + 40
        y2 = rua.gety2() + 25
        x2 = rua.getx2() + 40

        canvas.create_line(x1, y1, x2, y2, width=largura, tags="aa" + str(y1) + str(x1) + str(y2) + str(x2))


def mapa_info(mapa, root, menu):

    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=1000, height=1000, bg="white", highlightthickness=0)
    canvas.pack(side="right", padx=10)

    desenha_mapa(mapa, canvas)

    adicionar_barra_pesquisa(root, mapa, canvas, menu)

    botao_voltar = tk.Button(root, text="Voltar ao Menu Anterior", command=lambda: menu.abrir_menu("Encomendas"))
    botao_voltar.place(x=210, y=600)


def desenha_caminho(mapa, root, encomenda, menu):

    for widget in root.winfo_children():
        widget.destroy()

    titulo = tk.Label(root, text="HEALTH PLANET", font=("Helvetica", 40, "bold"), bg="white")
    titulo.configure(highlightthickness=0, bg="white")
    titulo.place(x=60, y=20)

    canvas = tk.Canvas(root, width=1000, height=1000, bg="white", highlightthickness=0)
    canvas.pack(side="right", padx=5)

    desenha_mapa(mapa, canvas)

    botao_voltar = tk.Button(root, text="Voltar ao Menu Anterior", command=lambda: menu.abrir_menu("Encomendas"))
    botao_voltar.place(x=200, y=750)

    botao_mapa = tk.Button(root, text="Visualizar Mapa da Cidade", command=lambda: mapa_info(mapa, root, menu))
    botao_mapa.place(x=200, y=500)

    botao_dfs = tk.Button(root, text="Visualizar Caminho DFS", command=lambda: desenha_caminho_dfs(mapa, root, encomenda, menu))
    botao_dfs.place(x=200, y=550)

    botao_bfs = tk.Button(root, text="Visualizar Caminho BFS", command=lambda: desenha_caminho_bfs(mapa, root, encomenda, menu))
    botao_bfs.place(x=200, y=600)

    botao_estrela = tk.Button(root, text="Visualizar Caminho A*", command=lambda: desenha_caminho(mapa, root, encomenda, menu))
    botao_estrela.place(x=200, y=650)

    

    caminho = encomenda.get_caminho()
    pontos = []

    for i, ponto in enumerate(caminho):
        coords_string = caminho[i]
        coords = coords_string.split('-')
        pontos.append(coords)

    for i in range(len(pontos) - 1):
        coord1 = pontos[i]
        x1 = float(coord1[0]) + 40
        y1 = float(coord1[1]) + 25

        coord2 = pontos[i + 1]
        x2 = float(coord2[0]) + 40
        y2 = float(coord2[1]) + 25

        canvas.create_line(x1, y1, x2, y2, width=3, fill="blue")

def desenha_caminho_dfs (mapa, root, encomenda, menu):

    for widget in root.winfo_children():
        widget.destroy()

    titulo = tk.Label(root, text="HEALTH PLANET", font=("Helvetica", 40, "bold"), bg="white")
    titulo.configure(highlightthickness=0, bg="white")
    titulo.place(x=60, y=20)

    canvas = tk.Canvas(root, width=1000, height=1000, bg="white", highlightthickness=0)
    canvas.pack(side="right", padx=5)

    desenha_mapa(mapa, canvas)

    botao_voltar = tk.Button(root, text="Voltar ao Menu Anterior", command=lambda: menu.abrir_menu("Encomendas"))
    botao_voltar.place(x=200, y=750)

    botao_mapa = tk.Button(root, text="Visualizar Mapa da Cidade", command=lambda: c.mapa_info(mapa, root, menu))
    botao_mapa.place(x=200, y=500)

    botao_dfs = tk.Button(root, text="Visualizar Caminho DFS", command=lambda: desenha_caminho_dfs(mapa, root, encomenda, menu))
    botao_dfs.place(x=200, y=550)

    botao_bfs = tk.Button(root, text="Visualizar Caminho BFS", command=lambda: desenha_caminho_bfs(mapa, root, encomenda, menu))
    botao_bfs.place(x=200, y=600)

    botao_estrela = tk.Button(root, text="Visualizar Caminho A*", command=lambda: desenha_caminho(mapa, root, encomenda, menu))
    botao_estrela.place(x=200, y=650)

    caminho = encomenda.get_caminho_dfs()
    pontos = []

    for i, ponto in enumerate(caminho):
        coords_string = caminho[i]
        coords = coords_string.split('-')
        pontos.append(coords)

    for i in range(len(pontos) - 1):
        coord1 = pontos[i]
        x1 = float(coord1[0]) + 40
        y1 = float(coord1[1]) + 25

        coord2 = pontos[i + 1]
        x2 = float(coord2[0]) + 40
        y2 = float(coord2[1]) + 25

        canvas.create_line(x1, y1, x2, y2, width=3, fill="blue")

def desenha_caminho_bfs (mapa, root, encomenda, menu):
    
        for widget in root.winfo_children():
            widget.destroy()
    
        titulo = tk.Label(root, text="HEALTH PLANET", font=("Helvetica", 40, "bold"), bg="white")
        titulo.configure(highlightthickness=0, bg="white")
        titulo.place(x=60, y=20)
    
        canvas = tk.Canvas(root, width=1000, height=1000, bg="white", highlightthickness=0)
        canvas.pack(side="right", padx=5)
    
        desenha_mapa(mapa, canvas)
    
        botao_voltar = tk.Button(root, text="Voltar ao Menu Anterior", command=lambda: menu.abrir_menu("Encomendas"))
        botao_voltar.place(x=200, y=750)

        botao_mapa = tk.Button(root, text="Visualizar Mapa da Cidade", command=lambda: mapa_info(mapa, root, menu))
        botao_mapa.place(x=200, y=500)

        botao_dfs = tk.Button(root, text="Visualizar Caminho DFS", command=lambda: desenha_caminho_dfs(mapa, root, encomenda, menu))
        botao_dfs.place(x=200, y=550)

        botao_bfs = tk.Button(root, text="Visualizar Caminho BFS", command=lambda: desenha_caminho_bfs(mapa, root, encomenda, menu))
        botao_bfs.place(x=200, y=600)

        botao_estrela = tk.Button(root, text="Visualizar Caminho A*", command=lambda: desenha_caminho(mapa, root, encomenda, menu))
        botao_estrela.place(x=200, y=650)

        caminho = encomenda.get_caminho_bfs()
        pontos = []
    
        for i, ponto in enumerate(caminho):
            coords_string = caminho[i]
            coords = coords_string.split('-')
            pontos.append(coords)
    
        for i in range(len(pontos) - 1):
            coord1 = pontos[i]
            x1 = float(coord1[0]) + 40
            y1 = float(coord1[1]) + 25
    
            coord2 = pontos[i + 1]
            x2 = float(coord2[0]) + 40
            y2 = float(coord2[1]) + 25
    
            canvas.create_line(x1, y1, x2, y2, width=3, fill="blue")

def desenha_caminho_estrela (mapa, root, encomenda, menu):
        
            for widget in root.winfo_children():
                widget.destroy()
        
            titulo = tk.Label(root, text="HEALTH PLANET", font=("Helvetica", 40, "bold"), bg="white")
            titulo.configure(highlightthickness=0, bg="white")
            titulo.place(x=60, y=20)
        
            canvas = tk.Canvas(root, width=1000, height=1000, bg="white", highlightthickness=0)
            canvas.pack(side="right", padx=5)
        
            desenha_mapa(mapa, canvas)
        
            botao_voltar = tk.Button(root, text="Voltar ao Menu Anterior", command=lambda: menu.abrir_menu("Encomendas"))
            botao_voltar.place(x=200, y=750)
    
            botao_mapa = tk.Button(root, text="Visualizar Mapa da Cidade", command=lambda: mapa_info(mapa, root, menu))
            botao_mapa.place(x=200, y=500)
    
            botao_dfs = tk.Button(root, text="Visualizar Caminho DFS", command=lambda: desenha_caminho_dfs(mapa, root, encomenda, menu))
            botao_dfs.place(x=200, y=550)
    
            botao_bfs = tk.Button(root, text="Visualizar Caminho BFS", command=lambda: desenha_caminho_bfs(mapa, root, encomenda, menu))
            botao_bfs.place(x=200, y=600)
    
            botao_estrela = tk.Button(root, text="Visualizar Caminho A*", command=lambda: desenha_caminho(mapa, root, encomenda, menu))
            botao_estrela.place(x=200, y=650)
    
            caminho = encomenda.get_caminho()
            pontos = []
        
            for i, ponto in enumerate(caminho):
                coords_string = caminho[i]
                coords = coords_string.split('-')
                pontos.append(coords)
        
            for i in range(len(pontos) - 1):
                coord1 = pontos[i]
                x1 = float(coord1[0]) + 40
                y1 = float(coord1[1]) + 25
        
                coord2 = pontos[i + 1]
                x2 = float(coord2[0]) + 40
