import tkinter as tk
import Estafeta as est
import Encomenda as enc
import Grafo as g
import Cidade as c
from Menu import Menu


def main():
    mapa = c.inicializa_mapa()
    encomendas = enc.inicializa_encomendas(mapa)
    grafo = g.Grafo()
    grafo.inicializa_grafo()
    estafetas = est.inicializa_estafetas()

    est.distribuir_encomendas(encomendas, estafetas)

    est.entrega(grafo.nodos, estafetas)

    root = tk.Tk()
    menu = Menu(root, mapa)

    menu.adicionar_menu("Principal", lambda: menu.principal(menu))
    menu.adicionar_menu("App", lambda: menu.app(menu))
    menu.adicionar_menu("Estafetas", lambda: menu.estafetas_info(menu, estafetas))
    menu.adicionar_menu("Encomendas", lambda: menu.encomendas_info(mapa, menu, encomendas))

    menu.abrir_menu("Principal")

    root.mainloop()


if __name__ == "__main__":
    main()
