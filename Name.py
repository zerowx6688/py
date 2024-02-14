import os
import tkinter as tk
from tkinter import filedialog


def rename_files():
    # 选择文件夹或多选文件
    file_paths = filedialog.askopenfilenames()

    # 待重命名文件列表
    files_to_rename = list(file_paths)

    # 待重命名文件个数
    num_files = len(files_to_rename)

    for index, file_path in enumerate(files_to_rename):
        # 获取文件名和文件扩展名
        file_name, file_extension = os.path.splitext(file_path)

        # 检查是否自定义了文件名
        if file_name.endswith('_'):
            # 使用自定义命名
            new_file_name = file_name[:-1] + f" {index + 1}{file_extension}"
        else:
            # 使用默认的数字编号命名
            new_file_name = f"{index + 1}{file_extension}"

        # 重命名文件
        os.rename(file_path, os.path.join(os.path.dirname(file_path), new_file_name))

    print(f"{num_files}个文件重命名完成！")


# 创建主窗口
root = tk.Tk()
root.title("文件重命名工具")

# 添加按钮
button = tk.Button(root, text="选择文件夹或多选文件", command=rename_files)
button.pack()

# 运行主循环
root.mainloop()
