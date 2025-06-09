# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib_inline import backend_inline
# from d2l import torch as d2l  # 正确导入d2l

# def use_svg_display():
#     """设置绘图格式为 SVG（或 PNG）"""
#     backend_inline.set_matplotlib_formats('svg')  # 或 'png'

# #@save
# def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
#     """设置坐标轴属性"""
#     axes.set_xlabel(xlabel)
#     axes.set_ylabel(ylabel)
#     axes.set_xscale(xscale)
#     axes.set_yscale(yscale)
#     axes.set_xlim(xlim)
#     axes.set_ylim(ylim)
#     if legend:
#         axes.legend(legend)
#     axes.grid()

# #@save
# def plot(X, Y=None, xlabel=None, ylabel=None, legend=None, xlim=None,
#          ylim=None, xscale='linear', yscale='linear',
#          fmts=('-', 'm--', 'g-.', 'r:'), figsize=(3.5, 2.5), axes=None):
#     """通用绘图函数"""
#     if legend is None:
#         legend = []
#     # 设置图形大小（替代d2l.set_figsize）
#     plt.figure(figsize=figsize)
#     axes = axes if axes else plt.gca()  # 获取当前坐标轴

#     def has_one_axis(X):
#         return (hasattr(X, "ndim") and X.ndim == 1 or 
#                 isinstance(X, list) and not hasattr(X[0], "__len__"))

#     if has_one_axis(X):
#         X = [X]
#     if Y is None:
#         X, Y = [[]] * len(X), X
#     elif has_one_axis(Y):
#         Y = [Y]
#     if len(X) != len(Y):
#         X = X * len(Y)
#     axes.cla()
#     for x, y, fmt in zip(X, Y, fmts):
#         if len(x) and len(y):
#             axes.plot(x, y, fmt)
#         else:
#             axes.plot(y, fmt)
#     set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)

# def f(x):
#     return 3 * x ** 2 - 4 * x

# # 调用use_svg_display设置绘图格式
# use_svg_display()

# # x = np.arange(0, 3, 0.1)
# # plot(x, [f(x), 2 * x - 3], 
# #      xlabel='x', 
# #      ylabel='f(x)', 
# #      legend=['f(x)', 'Tangent line (x=1)'],
# #      xlim=[0, 3], 
# #      ylim=[-5, 15])  # 添加显式坐标范围

# # 显式显示图像（VSCode 必须）
# # plt.show()
new line