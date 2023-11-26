import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def get_next_filename(output_folder, base_name):
    i = 1
    while True:
        filename = os.path.join(output_folder, f"{base_name}{i}.pdf")
        if not os.path.exists(filename):
            return filename
        i += 1

def convert_images_to_pdf(input_folder, output_file):
    images = [f for f in os.listdir(input_folder) if f.lower().endswith(('.webp', '.png', '.jpg', '.jpeg'))]

    if not images:
        print("指定文件夹中没有找到图片文件。")
        return

    images.sort()

    img_list = []
    for img_name in images:
        img_path = os.path.join(input_folder, img_name)
        img = Image.open(img_path)
        img_list.append(img)

    first_image = img_list[0]
    img_list.pop(0)

    first_image.save(output_file, save_all=True, append_images=img_list)

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)

def browse_output_folder():
    output_folder = filedialog.askdirectory()
    output_var.set(output_folder)

def convert():
    input_folder = folder_var.get()
    output_folder = output_var.get()
    custom_base_name = base_name_var.get()

    if custom_base_name:
        base_name = custom_base_name
    else:
        base_name = "sv"

    output_file = get_next_filename(output_folder, base_name)

    convert_images_to_pdf(input_folder, output_file)
    status_label.config(text="转换完成。")

root = tk.Tk()
root.title("SV Convert")
root.geometry("510x160")

folder_label = tk.Label(root, text="选择文件夹：")
folder_var = tk.StringVar()
folder_entry = tk.Entry(root, textvariable=folder_var, width=50, state='readonly')
browse_button = tk.Button(root, text="浏览", command=browse_folder)

folder_label.grid(row=0, column=0, sticky="w")
folder_entry.grid(row=0, column=1, columnspan=2, padx=5, sticky="w")
browse_button.grid(row=0, column=3)

output_label = tk.Label(root, text="输出文件夹：")
output_var = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_var, width=50, state='readonly')
browse_output_button = tk.Button(root, text="浏览", command=browse_output_folder)

output_label.grid(row=1, column=0, sticky="w")
output_entry.grid(row=1, column=1, columnspan=2, padx=5, sticky="w")
browse_output_button.grid(row=1, column=3)

base_name_label = tk.Label(root, text="自定义基本名称：")
base_name_var = tk.StringVar()
base_name_entry = tk.Entry(root, textvariable=base_name_var, width=30)

base_name_label.grid(row=2, column=0, sticky="w")
base_name_entry.grid(row=2, column=1, padx=5, sticky="w")

convert_button = tk.Button(root, text="开始转换", command=convert)
convert_button.grid(row=3, columnspan=4, pady=10)

status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=4, columnspan=4)

root.mainloop()
