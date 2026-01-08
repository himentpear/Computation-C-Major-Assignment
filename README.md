# LitePixel 图像编辑器

LitePixel 是一个使用Python Tkinter开发的轻量级图像编辑器，具有以下功能：

## 功能特性
- 打开和保存多种图片格式（JPG, PNG, BMP, WEBP等）
- 实时调整亮度、对比度、饱和度、锐化
- 高斯模糊效果
- 旋转、翻转、裁剪功能
- 黑白/灰度模式
- 一键美化功能

## 打包说明

要重新打包exe文件，请运行：

```
python build.py
```

打包后的exe文件将位于 `dist/LitePixel.exe`

## 依赖库
- Pillow
- tkinter (内置)
- platform (内置)

## 运行环境
- Python 3.x
- Windows系统