import os
import shutil

def move_jpg_to_folder(input_folder, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有 JPG 图片
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".txt"):
            source_path = os.path.join(input_folder, filename)
            destination_path = os.path.join(output_folder, filename)
            shutil.move(source_path, destination_path)

if __name__ == "__main__":
    input_folder = "/root/jsai_data/jsai_data/"    # 替换为包含 JPG 图片的文件夹的路径
    output_folder = "/root/jsai_data/jsai_data/txts"         # 替换为保存 JPG 图片的文件夹的路径

    move_jpg_to_folder(input_folder, output_folder)