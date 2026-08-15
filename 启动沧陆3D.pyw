# -*- coding: utf-8 -*-
"""沧陆世界 · 本地 3D 互动地图（独立窗口，离线运行，单实例）"""
import ctypes
import sys
import webview

# 单实例锁：重复双击不会开第二个窗口
MUTEX = ctypes.windll.kernel32.CreateMutexW(None, False, 'CangLu3D_SingleInstance')
if ctypes.windll.kernel32.GetLastError() == 183:  # ERROR_ALREADY_EXISTS
    sys.exit(0)

URL = 'file:///C:/Users/1/Desktop/沧陆/沧陆世界/index.html'

webview.create_window(
    '沧陆世界 · 3D 互动地图',
    URL,
    width=1600,
    height=900,
    resizable=True,
    min_size=(900, 600),
    background_color='#070a10',
)
webview.start()
