from tkinter import END
import subprocess

#Create Video
def create_video(image_path, audio_path,chat_window):
    if not image_path or not audio_path:
        chat_window.config(state="normal")
        chat_window.insert(
            END,
            "❌ Please select both image and audio first.\n\n",
            "bot"
        )
        chat_window.config(state="disabled")
        return

    chat_window.config(state="normal")
    chat_window.insert(
        END,
        f"🎬 Creating video using:\n{image_path}\n{audio_path}\n\n",
        "bot"
    )
    FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

    subprocess.run([
    FFMPEG_PATH,
    "-y",
    "-loop", "1",
    "-i", image_path,
    "-i", audio_path,
    "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
    "-c:v", "libx264",
    "-tune", "stillimage",
    "-c:a", "aac",
    "-b:a", "192k",
    "-pix_fmt", "yuv420p",
    "-shortest",
    "final_video.mp4"
    ], check=True)
    print("✅ Video created WITH audio")
    chat_window.config(state="disabled")

    


