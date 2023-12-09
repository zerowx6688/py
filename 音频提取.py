import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import os

class AudioExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("快速轻松地从视频中提取音频")
        self.root.geometry("400x200")
        self.root.configure(bg="#ffffff")

        # 初始化按钮
        self.select_video_button = tk.Button(root, text="选择视频", command=self.select_video)
        self.select_audio_button = tk.Button(root, text="选择音频文件夹", command=self.select_audio)
        self.start_button = tk.Button(root, text="开始提取", command=self.start_extraction)
        self.exit_button = tk.Button(root, text="退出", command=root.destroy)

        # 配置按钮样式
        button_style = {"bg": "#000000", "fg": "#ffffff"}
        self.select_video_button.configure(**button_style)
        self.select_audio_button.configure(**button_style)
        self.start_button.configure(**button_style)
        self.exit_button.configure(**button_style)

        # 将按钮添加到布局中
        self.select_video_button.pack(pady=5)
        self.select_audio_button.pack(pady=5)
        self.start_button.pack(pady=5)
        self.exit_button.pack(pady=5)

        # 添加帮助按钮
        self.help_button = tk.Button(root, text="帮助", command=self.show_help)
        self.help_button.pack(pady=5)

        # 初始化属性
        self.video_path = None
        self.audio_output_path = None

    def select_video(self):
        self.video_path = filedialog.askopenfilename(title="选择视频文件", filetypes=[("视频文件", "*.mp4;*.avi;*.mkv")])

    def select_audio(self):
        self.audio_output_path = filedialog.askdirectory(title="选择音频文件夹")

    def start_extraction(self):
        if self.video_path and self.audio_output_path:
            # 提取音频
            self.extract_audio()
        else:
            # 显示错误信息
            messagebox.showerror("错误", "请选择视频文件和音频存放路径")

    def extract_audio(self):
        video_clip = VideoFileClip(self.video_path)
        audio_clip = video_clip.audio

        # 获取视频文件的基本名称
        video_base_name = os.path.splitext(os.path.basename(self.video_path))[0]

        # 构建输出文件路径
        output_file_path = os.path.join(self.audio_output_path, f"{video_base_name}_Audio.mp3")

        # 提取音频
        audio_clip.write_audiofile(output_file_path)
        audio_clip.close()
        video_clip.close()

        # 显示提示信息
        messagebox.showinfo("完成", f"音频提取完成！\n保存在：{output_file_path}")

    def show_help(self):
        messagebox.showinfo("帮助", "快速轻松地从视频中提取音频\n\n1. 选择视频文件\n2. 选择音频存放路径\n3. 单击“开始提取”按钮\n\n音频提取完成后，将在指定的路径中生成音频文件")

# 创建主窗口
root = tk.Tk()
app = AudioExtractorApp(root)

# 启动主循环
root.mainloop()
