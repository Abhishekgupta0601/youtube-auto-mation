from tkinter import filedialog, END
import threading
import ai_model
from ai_model import generate_response
import upload_video,generate_video
from tkcalendar import Calendar
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import scheduler,upload_video
from scheduler import schedule_upload
from upload_video import upload_youtube_video


#Global Variable
selected_audio_path = None
selected_image_path = None
selected_video_path= None
selected_datetime = None

#Send Prompt
def send_message(entry_box,chat_window):
    prompt = entry_box.get("1.0", END).strip()
    if not prompt:
        return

    # Display user message
    chat_window.config(state="normal")
    chat_window.insert(END, f"You: {prompt}\n", "user")
    chat_window.config(state="disabled")
    chat_window.yview(END)
    entry_box.delete("1.0", END)

    # Fetch model response in a background thread
    threading.Thread(target=ai_model.generate_response, args=(prompt,chat_window)).start()


# Select Audio File
def select_mp3_file(chat_window):
    global selected_audio_path
    selected_audio_path = filedialog.askopenfilename(
        title="Select an MP3 file",
        filetypes=[("MP3 Audio Files", "*.mp3")]
    )

    if selected_audio_path:
        chat_window.config(state="normal")
        chat_window.insert(END, f"🎵 Selected MP3:\n{selected_audio_path}\n\n", "bot")
        chat_window.config(state="disabled")
        chat_window.yview(END)
 
#Select Image File
def select_image_file(chat_window):
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp")
        ]
    )

    if selected_image_path:
        chat_window.config(state="normal")
        chat_window.insert(END, f"🖼️ Selected Image:\n{selected_image_path}\n\n", "bot")
        chat_window.config(state="disabled")
        chat_window.yview(END)

 #Select Video File
def select_video_file(chat_window):
    global selected_video_path
    selected_video_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Video Files", "*.mp4*")
        ]
    )

    if selected_video_path:
        chat_window.config(state="normal")
        chat_window.insert(END, f"🖼️ Selected Image:\n{selected_video_path}\n\n", "bot")
        chat_window.config(state="disabled")
        chat_window.yview(END)

#Generate Video
def generate_video_action(chat_window):
    generate_video.create_video(selected_image_path, selected_audio_path,chat_window)


#Upload video action 
def upload_video_action(chat_window):
    upload_video.upload_youtube_video(selected_video_path,chat_window)


#Scheduler
def open_scheduler(chat_window):
    popup = tk.Toplevel(chat_window)
    popup.title("Select Date & Time")
    popup.geometry("300x350")

    # Calendar
    cal = Calendar(popup, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=10)

    # Time selectors
    time_frame = tk.Frame(popup)
    time_frame.pack(pady=10)

    tk.Label(time_frame, text="Hour").grid(row=0, column=0)
    tk.Label(time_frame, text="Minute").grid(row=0, column=1)

    hour_var = tk.StringVar(value="12")
    minute_var = tk.StringVar(value="00")

    hour_spin = ttk.Spinbox(
        time_frame, from_=0, to=23, width=5, textvariable=hour_var, format="%02.0f"
    )
    minute_spin = ttk.Spinbox(
        time_frame, from_=0, to=59, width=5, textvariable=minute_var, format="%02.0f"
    )

    hour_spin.grid(row=1, column=0, padx=5)
    minute_spin.grid(row=1, column=1, padx=5)

    result_label = tk.Label(popup, text="")
    result_label.pack(pady=10)

    def confirm_schedule():
        global selected_datetime
        selected_datetime = f"{cal.get_date()} {hour_var.get()}:{minute_var.get()}"
        scheduled_time = datetime.strptime(selected_datetime, "%Y-%m-%d %H:%M")
        chat_window.config(state="normal")
        chat_window.insert(END, f"📅 Scheduled upload at: {selected_datetime}\n\n", "bot")
        chat_window.config(state="disabled")
        chat_window.yview(END)

        schedule_upload(
        scheduled_time=scheduled_time,
        upload_callback=lambda chat_window: upload_youtube_video(selected_video_path,chat_window),
        chat_window=chat_window
        )
        popup.destroy()

    tk.Button(
        popup,
        text="Confirm",
        bg="#28a745",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        command=confirm_schedule
    ).pack(pady=15)


