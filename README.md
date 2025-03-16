# 🦖 Dino Keep Online

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

懂的都懂😌~ 一个可爱的桌面挂机程序，让你的电脑保持在线状态！带有动态恐龙动画的界面让挂机变得有趣。

## ✨ 特性

- 🎮 模拟鼠标移动和键盘操作，保持系统活跃
- 🦕 可爱的像素风恐龙动画
- 🎯 置顶窗口，方便控制
- 🌈 简洁美观的深色主题界面
- 💫 半透明窗口效果
- 🔄 可拖拽的自定义窗口

## 🚀 安装

1. 克隆仓库
```bash
git clone https://github.com/yenyoong99/DinoKeepOnline.git
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

## 🎮 使用方法

1. 运行程序
```bash
python dino_keep_online.py
```

2. 点击 "START" 按钮开始挂机
3. 需要停止时点击 "STOP" 按钮
4. 点击右上角 "X" 退出程序

## 📦 打包方法

1. 安装PyInstaller
```bash
pip install pyinstaller
```

2. 执行打包命令
```bash
pyinstaller dino_keep_online.spec
```

3. 打包完成后，可执行文件位于 `dist` 文件夹中
- Windows用户可直接运行 `dist/dino_keep_online.exe`
- 支持单文件运行，无需安装Python环境

## 🛠️ 技术栈

- Python 3.6+
- tkinter - GUI界面
- pyautogui - 鼠标键盘模拟
- threading - 多线程处理

## 📷 截图

![alt text](image.png)

## 🤝 贡献

欢迎提交 issues 和 pull requests 来帮助改进这个项目！

## 📝 许可证

本项目采用 MIT 许可证 - 详情请查看 [LICENSE](LICENSE) 文件

---
⭐ 如果这个项目对你有帮助，欢迎给它一个star！
