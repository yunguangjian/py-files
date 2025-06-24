# -*- coding: utf-8 -*-
from rembg import remove
from PIL import Image, ImageOps
import os

# 输入图片所在文件夹（把你的8张图片放此文件夹）
input_folder = r"C:\Users\Administrator\Desktop\123"
# 输出图片保存文件夹
output_folder = r"C:\Users\Administrator\Desktop\456"
# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的图片文件
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 打开图片
        with Image.open(input_path) as img:
            # 移除背景，包括阴影等
            output = remove(img)

            # 创建纯白色背景，尺寸与原图一致
            bg = Image.new('RGBA', output.size, (255, 255, 255, 255))
            # 将去除背景后的图片粘贴到白色背景上（确保边缘融合自然）
            bg.paste(output, (0, 0), output)

            # 转换为 RGB 模式（避免后续保存可能的问题）
            result = bg.convert('RGB')

            # 设置分辨率为 300dpi
            result.info['dpi'] = (300, 300)

            # 保存处理后的图片
            result.save(output_path)
            print(f"已处理 {filename} 并保存到 {output_path}")