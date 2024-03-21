import tkinter as tk
from tkinter import ttk

import game

class Launcher(tk.Tk):
	def __init__(self, title: str, width: int, height: int):
		super().__init__()

		self.title(title)
		self.geometry(f'{width}x{height}')
		self.resizable(tk.FALSE, tk.FALSE)

		self.launch = ttk.Button(self, text='Launch', command=lambda: game.run())
		self.launch.pack()


if __name__ == '__main__':
	launcher = Launcher('Game launcher', 512, 512)
	launcher.mainloop()
