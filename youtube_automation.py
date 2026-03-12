import tkinter as tk
from tkinter import scrolledtext,filedialog
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip
import pyttsx3
from gui import create_gui
import gui_logic,upload_video

# ---------------- TTS Engine ----------------
engine = pyttsx3.init()

callbacks = {
    "send_message": gui_logic.send_message,
    "select_mp3_file": gui_logic.select_mp3_file,
    "select_image_file": gui_logic.select_image_file,
    "select_video_file": gui_logic.select_video_file,
    "upload_video_action": gui_logic.upload_video_action,
    "generate_video_action":gui_logic.generate_video_action,
    "open_schdeuler":gui_logic.open_scheduler,
}

root, chat_window = create_gui(callbacks)
root.mainloop()

