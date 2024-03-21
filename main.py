import tkinter as tk
from tkinter import ttk

class Launcher(tk.Tk):
	def __init__(self, title: str, width: int, height: int):
		super().__init__()

		self.title(title)
		self.geometry(f'{width}x{height}')
		self.resizable(tk.FALSE, tk.FALSE)


if __name__ == '__main__':
	launcher = Launcher('Game launcher', 512, 512)
	launcher.mainloop()
