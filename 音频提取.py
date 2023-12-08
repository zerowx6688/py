import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
from tkinter import ttk
import threading

class AudioExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("视频音频提取工具")
        self.root.geometry("600x220")  # 修改此行

        # 创建变量用于存储文件名和路径
        self.video_filename_var = tk.StringVar()
        self.audio_filename_var = tk.StringVar()

        # 创建按钮
        self.select_video_button = tk.Button(root, text="选择视频文件", command=self.select_video)
        self.select_video_button.pack(pady=1, padx=1)  # Moved to the right by 10 pixels

        # 显示所选视频文件名
        self.video_filename_label = tk.Label(root, textvariable=self.video_filename_var)
        self.video_filename_label.pack(pady=1)

        self.select_audio_button = tk.Button(root, text="选择音频存放路径", command=self.select_audio)
        self.select_audio_button.pack(pady=1)

        # 显示所选音频存放路径
        self.audio_filename_label = tk.Label(root, textvariable=self.audio_filename_var)
        self.audio_filename_label.pack(pady=1)

        self.start_button = tk.Button(root, text="开始提取", command=self.extract_audio)
        self.start_button.pack(pady=1)

        # 创建进度信息的标签
        self.progress_label = tk.Label(root, text="")
        self.progress_label.pack(pady=10)

        # 创建进度条
        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=1)

    def select_video(self):
        self.video_path = filedialog.askopenfilename(title="选择视频文件", filetypes=[("视频文件", "*.mp4;*.avi;*.mkv")])

        # 更新视频文件名和路径
        self.video_filename_var.set(f"所选文件: {self.get_filename(self.video_path)}")
        self.audio_filename_var.set("")

    def select_audio(self):
        self.audio_output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("音频文件", "*.mp3")])

        # 更新音频存放路径
        self.audio_filename_var.set(f"存放路径: {self.audio_output_path}")
    
    def get_filename(self, path):
        # 从路径中提取文件名
        return path.split("/")[-1] if "/" in path else path.split("\\")[-1]

    def update_progress(self, current, total):
        progress_percentage = (current / total) * 100
        self.progress_label.config(text=f"处理中... {current}/{total}")
        self.progress_bar["value"] = progress_percentage
        self.root.update_idletasks()

    def extract_audio_thread(self):
        video_clip = VideoFileClip(self.video_path)
        audio_clip = video_clip.audio

        total_frames = int(audio_clip.fps * audio_clip.duration)
        current_frame = 0

        # 模拟处理每个音频块
        for chunk in audio_clip.iter_frames():
            current_frame += 1024
            self.update_progress(current_frame, total_frames)

        audio_clip.write_audiofile(self.audio_output_path)
        audio_clip.close()
        video_clip.close()

        messagebox.showinfo("完成", "音频提取完成！")
        self.progress_label.config(text="")
        self.progress_bar["value"] = 0

    def extract_audio(self):
        if hasattr(self, 'video_path') and hasattr(self, 'audio_output_path'):
            threading.Thread(target=self.extract_audio_thread).start()
            self.root.after(100, self.check_progress)
        else:
            messagebox.showerror("错误", "请选择视频文件和音频存放路径")

    def check_progress(self):
        # 检查进度并更新GUI
        if hasattr(self, 'video_path') and hasattr(self, 'audio_output_path'):
            video_clip = VideoFileClip(self.video_path)
            audio_clip = video_clip.audio

            total_frames = int(audio_clip.fps * audio_clip.duration)
            current_frame = min(1024, total_frames)

            self.update_progress(current_frame, total_frames)
            self.root.after(100, self.check_progress)

# 创建主窗口
root = tk.Tk()
app = AudioExtractorApp(root)

# 启动主循环
root.mainloop()
