import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip

class AudioExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("视频音频提取工具")
        self.root.geometry("400x100")

        # 创建按钮
        self.select_video_button = tk.Button(root, text="选择视频文件", command=self.select_video)
        self.select_video_button.pack(pady=2)

        self.select_audio_button = tk.Button(root, text="选择音频存放路径", command=self.select_audio)
        self.select_audio_button.pack(pady=2)

        self.start_button = tk.Button(root, text="开始提取", command=self.extract_audio)
        self.start_button.pack(pady=2)

    def select_video(self):
        self.video_path = filedialog.askopenfilename(title="选择视频文件", filetypes=[("视频文件", "*.mp4;*.avi;*.mkv")])

    def select_audio(self):
        self.audio_output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("音频文件", "*.mp3")])

    def extract_audio(self):
        if hasattr(self, 'video_path') and hasattr(self, 'audio_output_path'):
            video_clip = VideoFileClip(self.video_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(self.audio_output_path)
            audio_clip.close()
            video_clip.close()
            messagebox.showinfo("完成", "音频提取完成！")
        else:
            messagebox.showerror("错误", "请选择视频文件和音频存放路径")

# 创建主窗口
root = tk.Tk()
app = AudioExtractorApp(root)

# 启动主循环
root.mainloop()
