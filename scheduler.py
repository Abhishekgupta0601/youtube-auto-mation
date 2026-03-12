import time
import threading
from datetime import datetime
from upload_video import upload_youtube_video

def schedule_upload(scheduled_time, upload_callback, chat_window):
    def task():
        delay = (scheduled_time - datetime.now()).total_seconds()

        if delay <= 0:
            chat_window.insert("end", "❌ Scheduled time is in the past\n")
            return

        chat_window.insert("end", f"⏳ Upload scheduled in {int(delay)} seconds\n")
        chat_window.yview("end")

        time.sleep(delay)  # background thread only

        chat_window.insert("end", "🚀 Upload started...\n")
        chat_window.yview("end")

        upload_callback(chat_window)  # call your upload function

    threading.Thread(target=task, daemon=True).start()
