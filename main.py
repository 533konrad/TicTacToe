import pygame

#drukowane, bo to stałe wartości
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

TLO = (255,255,255)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

pygame.display.set_caption("Tic Tac Toe!")

def draw_window():
    WIN.fill(TLO)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

import tkinter as tk

class Aplikacja(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.przykladowaEtykieta = tk.Label(self, text='Witaj Świecie')
        self.przykladowaEtykieta.config(bg="#00ffff")
        self.przykladowaEtykieta.grid()
        self.quitButton = tk.Button(self, text='Zakończ', command=self.quit)
        self.quitButton.grid()

app = Aplikacja()
app.master.title('Przykładowa Aplikacja')
app.mainloop()