import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import Cidade as c


class Menu:

    def __init__(self, root, mapa):
        root.attributes('-fullscreen', True)
        root.configure(bg="white")
        self.root = root
        self.mapa = mapa
        self.giflabel = None
        self.conta = 0
        self.showanimacao = None
        self.frames = 0
        self.framesimagem = None
        self.frame_encomendas = None
        self.scroll_encomendas = None
        self.tabela_encomendas = None
        self.frame_estafetas = None
        self.scroll_estafetas = None
        self.tabela_estafetas = None
        self.menus = {}

    # Método que adiciona um menu ao programa
    def adicionar_menu(self, nome, menu_function):
        self.menus[nome] = menu_function

    # Método para abrir um determinado menu
    def abrir_menu(self, nome):
        menu = self.menus.get(nome)
        if menu:
            menu()

    # Método para limpar todos os objetos criados anteriormente na janela
    def limpa_janela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Método para aplicar a animação do gif
    def animacao(self, menu):
        novaimagem = self.framesimagem[self.conta]

        if self.giflabel.winfo_exists():
            self.giflabel.configure(image=novaimagem)
            self.conta += 1
            if self.conta == self.frames:
                self.conta = 0
            self.showanimacao = self.root.after(350, lambda: menu.animacao(menu))

    # Método que inicializa todas as variaveis necessárias para a implementação do gif
    def inicializa_gif(self, menu):
        imagem = Image.open("giphy.gif")
        self.frames = imagem.n_frames
        self.framesimagem = [tk.PhotoImage(file="giphy.gif", format=f"gif -index {i}") for i in range(self.frames)]

        self.conta = 0
        self.giflabel = tk.Label(self.root, image="", bg="white", borderwidth=0)
        self.giflabel.place(x=580, y=420, width=400, height=400)

        menu.animacao(menu)

    # Método que é acionado quando o utilizador faz duplo clique numa linha da tabela de encomendas
    def duplo_clique(self, event, encomendas, menu, mapa):
        item = self.tabela_encomendas.selection()[0]
        index = int(self.tabela_encomendas.index(item))
        encomenda_selecionada = encomendas[index]

        c.desenha_caminho(mapa, self.root, encomenda_selecionada, menu)

        botao_mapa = tk.Button(self.root, text="Visualizar Mapa da Cidade", command=lambda: c.mapa_info(mapa, self.root, menu))
        botao_mapa.place(x=200, y=500)

        botao_dfs = tk.Button(self.root, text="Visualizar Caminho DFS", command=lambda: c.desenha_caminho_dfs(mapa, self.root, encomenda_selecionada, menu))
        botao_dfs.place(x=200, y=550)

        botao_bfs = tk.Button(self.root, text="Visualizar Caminho BFS", command=lambda: c.desenha_caminho_bfs(mapa, self.root, encomenda_selecionada, menu))
        botao_bfs.place(x=200, y=600)

        botao_estrela = tk.Button(self.root, text="Visualizar Caminho A*", command=lambda: c.desenha_caminho(mapa, self.root, encomenda_selecionada, menu))
        botao_estrela.place(x=200, y=650)

        botao_greedy = tk.Button(self.root, text="Visualizar Caminho Greedy", command=lambda: c.desenha_caminho_greedy(mapa, self.root, encomenda_selecionada, menu))
        botao_greedy.place(x=200, y=700)
        
    # Menu que mostra todas as encomendas realizadas ao longo do programa
    def encomendas_info(self, mapa, menu, encomendas):

        menu.limpa_janela()

        # Insere o título na janela
        titulo = tk.Label(self.root, text="HEALTH PLANET", font=("Helvetica", 40, "bold"), bg="white")
        titulo.configure(highlightthickness=0, bg="white")
        titulo.pack(pady=50)

        # Variáveis necessárias para a criação da tabela
        self.frame_encomendas = tk.Frame(self.root)
        self.frame_encomendas.place(x=350, y=180)
        self.scroll_encomendas = tk.Scrollbar(self.frame_encomendas)
        self.scroll_encomendas.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabela_encomendas = ttk.Treeview(self.frame_encomendas, yscrollcommand=self.scroll_encomendas.set)
        self.tabela_encomendas.pack()
        self.scroll_encomendas.config(command=self.tabela_encomendas.yview)

        self.tabela_encomendas['columns'] = ('ID', 'Peso', 'Morada', 'Estafeta')

        # Formatar as colunas
        self.tabela_encomendas.column("#0", width=0, stretch=tk.NO)
        self.tabela_encomendas.column("ID", anchor=tk.CENTER, width=250)
        self.tabela_encomendas.column("Peso", anchor=tk.CENTER, width=60)
        self.tabela_encomendas.column("Morada", anchor=tk.CENTER, width=400)
        self.tabela_encomendas.column("Estafeta", anchor=tk.CENTER, width=120)

        # Cria os cabeçalhos para cada coluna
        self.tabela_encomendas.heading("#0", text="", anchor=tk.CENTER)
        self.tabela_encomendas.heading("ID", text="ID", anchor=tk.CENTER)
        self.tabela_encomendas.heading("Peso", text="Peso", anchor=tk.CENTER)
        self.tabela_encomendas.heading("Morada", text="Morada", anchor=tk.CENTER)
        self.tabela_encomendas.heading("Estafeta", text="Estafeta", anchor=tk.CENTER)

        for i, encomenda in enumerate(encomendas):
            id = encomenda.get_id()
            peso = encomenda.get_peso()
            morada = encomenda.get_morada()
            rua = morada.__str__()
            estafeta = encomenda.get_estafeta()
            nome_estafeta = estafeta.getnome()
            self.tabela_encomendas.insert(parent='', index='end', iid=i, text='', values=(id, peso, rua, nome_estafeta))

        self.tabela_encomendas.bind('<Double-1>', lambda event: menu.duplo_clique(event, encomendas, menu, mapa))

        self.tabela_encomendas.configure(height=20)
        self.tabela_encomendas.pack()

        botao_voltar = tk.Button(self.root, text="Voltar ao Menu Anterior", command=lambda: menu.abrir_menu("App"))
        botao_voltar.place(x=700, y=650)

    def ordenar_tabela(self, coluna):
        itens = [(float(self.tabela_estafetas.set(item, coluna)), item) for item in self.tabela_estafetas.get_children('')]

        # Ordena os itens com base na coluna clicada
        itens.sort(reverse=True)

        # Move os itens ordenados para a tabela
        for index, (valor, item) in enumerate(itens):
            self.tabela_estafetas.move(item, '', index)

    # Menu que mostra as estatísticas de todos os estafetas
    def estafetas_info(self, menu, estafetas):

        menu.limpa_janela()

        titulo = tk.Label(self.root, text="HEALTH PLANET", font=("Helvetica", 40, "bold"), bg="white")
        titulo.configure(highlightthickness=0, bg="white")
        titulo.pack(pady=50)

        # Variáveis necessárias para a criação da tabela
        self.frame_estafetas = tk.Frame(self.root)
        self.frame_estafetas.place(x=440, y=150)
        self.scroll_estafetas = tk.Scrollbar(self.frame_estafetas)
        self.scroll_estafetas.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabela_estafetas = ttk.Treeview(self.frame_estafetas, yscrollcommand=self.scroll_estafetas.set)
        self.tabela_estafetas.pack()
        self.scroll_estafetas.config(command=self.tabela_estafetas.yview)

        self.tabela_estafetas['columns'] = ('ID', 'Nome', 'Rating', 'Distancia')

        # Formatar as colunas
        self.tabela_estafetas.column("#0", width=0, stretch=tk.NO)
        self.tabela_estafetas.column("ID", anchor=tk.CENTER, width=100)
        self.tabela_estafetas.column("Nome", anchor=tk.CENTER, width=300)
        self.tabela_estafetas.column("Rating", anchor=tk.CENTER, width=120)
        self.tabela_estafetas.column("Distancia", anchor=tk.CENTER, width=120)

        # Cria os cabeçalhos para cada coluna
        self.tabela_estafetas.heading("#0", text="", anchor=tk.CENTER)
        self.tabela_estafetas.heading("ID", text="ID", anchor=tk.CENTER)
        self.tabela_estafetas.heading("Nome", text="Nome", anchor=tk.CENTER)
        self.tabela_estafetas.heading("Rating", text="Rating", anchor=tk.CENTER, command=lambda: self.ordenar_tabela("Rating"))
        self.tabela_estafetas.heading("Distancia", text="Distancia", anchor=tk.CENTER, command=lambda: self.ordenar_tabela("Distancia"))

        for i, estafeta in enumerate(estafetas):
            id = estafeta.getid()
            nome = estafeta.getnome()
            rating = estafeta.getrating()
            distancia = estafeta.get_distancia_percorrida()
            self.tabela_estafetas.insert(parent='', index='end', iid=i, text='', values=(id, nome, rating, distancia))

        self.tabela_estafetas.configure(height=30)
        self.tabela_estafetas.pack()

        botao_voltar = tk.Button(self.root, text="Voltar ao Menu Anterior", command=lambda: menu.abrir_menu("App"))
        botao_voltar.place(x=700, y=800)

    # Menu Principal da App que mostra todas as opções disponíveis no programa
    def app(self, menu):

        menu.limpa_janela()

        titulo = tk.Label(self.root, text="HEALTH PLANET", font=("Helvetica", 40, "bold"), bg="white")
        titulo.configure(highlightthickness=0, bg="white")
        titulo.pack(pady=50)

        botao_encomendas = tk.Button(self.root, text="Visualizar Encomendas", command=lambda: menu.abrir_menu("Encomendas"))
        botao_encomendas.pack(pady=20)

        botao_estafetas = tk.Button(self.root, text="Visualizar Estafetas", command=lambda: menu.abrir_menu("Estafetas"))
        botao_estafetas.pack(pady=20)

        botao_voltar = tk.Button(self.root, text="Voltar ao Menu Anterior", command=lambda: menu.abrir_menu("Principal"))
        botao_voltar.pack(pady=20)

        menu.inicializa_gif(menu)

    # Menu Inicial do Programa
    def principal(self, menu):

        menu.limpa_janela()

        titulo = tk.Label(self.root, text="HEALTH PLANET", font=("Helvetica", 40, "bold"), bg="white")
        titulo.configure(highlightthickness=0, bg="white")
        titulo.pack(pady=50)

        botao_app = tk.Button(self.root, text="Gestão App", command=lambda: menu.abrir_menu("App"))
        botao_app.pack(pady=20)

        botao_sair = tk.Button(self.root, text="Sair do Programa", command=self.root.destroy)
        botao_sair.pack(pady=10)

        imagem = Image.open("imagemprincipal.jpeg")
        imagem_redimensionada = imagem.resize((400, 400))
        imagem = ImageTk.PhotoImage(imagem_redimensionada)

        canvas = tk.Canvas(self.root, width=400, height=400)
        canvas.create_image(0, 0, anchor=tk.NW, image=imagem)
        canvas.pack(pady=100)

        canvas.imagem = imagem
