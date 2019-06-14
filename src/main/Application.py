# coding:utf-8
import tkinter as tk

from src.main import config
from src.main.config import config


class Application(tk.Frame):
    """
    创建窗体及绘制UI
    """

    def __init__(self, master=None, canvas_config=None):
        super().__init__(master)
        self.master = master
        self.canvas_config = config.cnf
        self.create_widgets()

    def create_widgets(self):
        """
        创建UI控件
        """

        self.start_or_pause_button = tk.Button(self.master, text='start')
        self.clear_button = tk.Button(self.master, text='clear')
        self.random_buttoon = tk.Button(self.master, text='random')
        self.canvas = tk.Canvas(self.master, cnf=self.canvas_config, bg='white')
        self.save_button = tk.Button(self.master, text='save')
        self.load_button = tk.Button(self.master, text='load')

        def handle_speed_change(delay):
            config.time_frame = delay

        self.speed_scale = tk.Scale(self.master, from_=100, to=5000, orient="horizontal",
                                    command=handle_speed_change)

        self.start_or_pause_button.grid(row=0, column=0)
        self.random_buttoon.grid(row=0, column=1)
        self.clear_button.grid(row=0, column=2)
        self.load_button.grid(row=1, column=3)
        self.save_button.grid(row=1, column=4)
        self.speed_scale.grid(row=0, column=3)
        self.canvas.grid(row=1, columnspan=3, rowspan=4,
                         sticky=tk.W + tk.E + tk.S)
