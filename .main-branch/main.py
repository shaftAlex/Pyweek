import tkinter as tk
from tkinter import ttk

import globals as g
import game

class Launcher(tk.Tk):
	def __init__(self, title: str, width: int, height: int):
		super().__init__()

		self.title(title)
		self.geometry(f'{width}x{height}')
		self.resizable(tk.FALSE, tk.FALSE)

		self.launch = ttk.Button(self, text='Launch', command=lambda: self.run())
		self.launch.pack()

	def run(self):
		g.LAUNCHER.destroy()
		game.run()

if __name__ == '__main__':
	g.LAUNCHER = Launcher('Game launcher', 512, 512)
	g.LAUNCHER.mainloop()
