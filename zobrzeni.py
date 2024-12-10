import tkinter as tk


class BludisteRenderer:
    def __init__(self, bludiste, velikost_bunky=50):
        """
        Inicializace třídy pro zobrazení bludiště pomocí tkinter Canvas.

        :param bludiste: Instance třídy Bludiste
        :param velikost_bunky: Velikost jedné buňky v pixelech
        """
        self.bludiste = bludiste
        self.velikost_bunky = velikost_bunky
        self.okno = tk.Tk()
        self.canvas = tk.Canvas(self.okno,
                                width=self.bludiste.sirka * velikost_bunky,
                                height=self.bludiste.vyska * velikost_bunky)
        self.canvas.pack()

    def vykresli(self):
        """
        Vykreslení bludiště na canvas.
        """
        self.canvas.delete("all")
        for y, radek in enumerate(self.bludiste.mapa):
            for x, bunka in enumerate(radek):
                x1, y1 = x * self.velikost_bunky, y * self.velikost_bunky
                x2, y2 = x1 + self.velikost_bunky, y1 + self.velikost_bunky

                barva = "white"
                if bunka == 1:
                    barva = "black"
                elif bunka == 'E':
                    barva = "green"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=barva)

        # Vykreslení robota
        x_robot, y_robot = self.bludiste.pozice
        x1, y1 = x_robot * self.velikost_bunky, y_robot * self.velikost_bunky
        x2, y2 = x1 + self.velikost_bunky, y1 + self.velikost_bunky
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")

    def aktualizuj(self, nova_pozice):
        """
        Aktualizace pozice robota a překreslení bludiště.

        :param nova_pozice: Nová pozice robota (x, y)
        """
        if self.bludiste.pohnout(nova_pozice):
            self.vykresli()
        else:
            print("Pohyb se nezdařil - narazil do zdi nebo mimo mapu.")

    def spust(self):
        """
        Spuštění aplikace.
        """
        self.vykresli()
        self.okno.mainloop()
