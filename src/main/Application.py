# coding:utf-8
import tkinter as tk

from src.main import config


class Application(tk.Frame):
    """
    创建窗体及绘制UI
    """

    def __init__(self, master=None, canvas_config=None):
        super().__init__(master)
        self.master = master
        self.canvas_config = config.config.cnf
        self.create_widgets()

    def create_widgets(self):
        """
        创建UI控件
        """
        self.start_or_pause_button = tk.Button(self.master, text='start')
        self.clear_button = tk.Button(self.master, text='clear')
        self.edit_button = tk.Button(self.master, text='edit')
        self.canvas = tk.Canvas(master=self.master, cnf=self.canvas_config, bg='white')

        self.start_or_pause_button.pack()
        self.clear_button.pack()
        self.edit_button.pack()
        self.canvas.pack()
