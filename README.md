# 生命游戏


## 界面展示

## 功能

1. 画图
2. 游戏状态保存与载入
3. 动画速度调整

## 技术栈

Python

## 三方库

tkinter
easygui
numpy

## 亮点

1. 画布的局部更新。差集做更新，绘制效率提升。

```python

class CellView:
    def show_detail(self, cells: CellModel.cell):
        """
        根据给定的细胞视图更新视图
        :param cells: 给定的细胞视图
        """
        handle = self.handle
        # 当 grid_ids 和 last_cells 和 cells 的形状相同
        # 说明可以复用之前的绘制图形
        if self.grid_ids is not None:
            diff_before = self.last_cells == cells
            self._draw_canvas(handle, cells, diff_before)
        else:
            # 不能复用之前的图形，需要全部重新绘制
            self.grid_ids = np.zeros_like(cells)
            self._draw_canvas(handle, cells)
        self.last_cells = cells.copy()
```

2. python类型注解。新的语言特性，帮助IDE进行类型检查。

3. numpy加速矩阵运算。python的科学计算的C拓展，比原生list运行更快。

4. MVC设计模式。让代码具有层次性，更加清楚各层的职责

> Model 将存储数据的部分从业务代码中分离

> View 视图层，绘制可视化

> Controller 负责与用户交互的部分

## 项目目录

```
src
├── main
│   ├── Application.py      # 主窗体
│   ├── config.py           # 存放配置文件
│   ├── controller.py       # 细胞的控制器。控制数据流向模型对象，在数据变化时更新视图
│   ├── main.py             # 主程序，组装、调用Controller
│   ├── matrix_iteration.py # 算法部分，获取下一时刻的细胞状态
│   ├── model.py            # 细胞模型定义
│   ├── resource            
│   │   └── map.npy         # 保存的游戏状态
│   ├── state.py            # 游戏状态枚举
│   ├── util.py             # 工具类，（方块的大小、序列化文件）
│   └── view.py             # 细胞底层数据的可视化
└── test
    └── main_test.py        # 算法测试
```
