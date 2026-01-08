# build.py - 打包LitePixel应用为exe文件
import os
import sys

def build_executable():
    """使用PyInstaller构建可执行文件"""
    # 构建命令
    cmd = [
        "pyinstaller",
        "--onefile",           # 打包成单个exe文件
        "--windowed",          # 不显示控制台窗口
        "--name=LitePixel",    # 可执行文件名
        "--hidden-import=PIL", # 隐式导入PIL模块
        "--hidden-import=PIL.Image", 
        "--hidden-import=PIL.ImageTk",
        "--hidden-import=PIL.ImageEnhance",
        "--hidden-import=PIL.ImageFilter",
        "--hidden-import=PIL.ImageOps",
        "--hidden-import=tkinter.colorchooser",
        "demo.py"
    ]
    
    # 组合命令字符串
    cmd_str = " ".join(cmd)
    print(f"执行打包命令: {cmd_str}")
    
    # 执行打包命令
    os.system(cmd_str)
    
    print("打包完成！请在dist文件夹中查找LitePixel.exe文件。")

if __name__ == "__main__":
    build_executable()