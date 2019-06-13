# coding:utf-8
import tkinter as tk

from src.main import config
from src.main.config import Config


class Application(tk.Frame):
    """
    创建窗体及绘制UI
    """

    def __init__(self, master=None, canvas_config=None):
        super().__init__(master)
        self.master = master
        self.canvas_config = config.Config.cnf
        self.create_widgets()

    def create_widgets(self):
        """
        创建UI控件
        """

        self.start_or_pause_button = tk.Button(self.master, text='start')
        self.clear_button = tk.Button(self.master, text='clear')
        self.edit_button = tk.Button(self.master, text='edit')
        self.canvas = tk.Canvas(self.master, cnf=self.canvas_config, bg='white')

        def handle_speed_change(delay):
            Config.time_frame = delay

        self.speed_scale = tk.Scale(self.master, from_=100, to=1000, orient="horizontal",
                                    command=handle_speed_change)

        self.start_or_pause_button.grid(row=0, column=0)
        self.clear_button.grid(row=0, column=1)
        self.edit_button.grid(row=0, column=2)
        self.speed_scale.grid(row=0, column=3)
        self.canvas.grid(row=1, columnspan=4, rowspan=4,
                         sticky=tk.W + tk.E + tk.S)
