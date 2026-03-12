import tkinter as tk
from tkinter import scrolledtext,filedialog

# Build GUI

def create_gui(callbacks):
    root = tk.Tk()
    root.title("💬 Ollama Chat")
    root.geometry("700x550")

    # Chat display

    chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 11))
    chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    chat_window.config(state=tk.DISABLED)
    chat_window.tag_config("user", foreground="#0078D7", font=("Segoe UI", 11, "bold"))
    chat_window.tag_config("bot", foreground="#2E8B57", font=("Segoe UI", 11))

    # Input area
    entry_box = tk.Text(root, height=3, font=("Segoe UI", 11))
    entry_box.pack(padx=10, pady=(0,5), fill=tk.X)
    entry_box.focus()  # focus the input box automatically

    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=(0,10))
    
    tk.Button(
        button_frame,
        text="Send",
        command=lambda: callbacks["send_message"](entry_box, chat_window),
        bg="#FF8C00",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        width=12
    ).pack(side=tk.LEFT, padx=5)
    
    tk.Button(
        button_frame,
        text="🎵 Select MP3",
        command=lambda:callbacks["select_mp3_file"](chat_window),
        bg="#FF8C00",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        width=12
    ).pack(side=tk.LEFT, padx=5)

    tk.Button(
        button_frame,
        text="🖼️ Select Image",
        command=lambda:callbacks["select_image_file"](chat_window),
        bg="#20B2AA",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        width=12
    ).pack(side=tk.LEFT, padx=5)

    tk.Button(
        button_frame, 
        text="🎬 Generate Video", 
        command=lambda:callbacks["generate_video_action"](chat_window),
        bg="#FF8C00", fg="white",
        font=("Segoe UI", 11, "bold"), width=16).pack(side=tk.LEFT, padx=5)

    tk.Button(
        button_frame,
        text="🖼️ Select Video File",
        command=lambda:callbacks["select_video_file"](chat_window),
        bg="#20B2AA",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        width=12
    ).pack(side=tk.LEFT, padx=5)

    tk.Button(
        button_frame, 
        text="🎬 Upload Video", 
        command=lambda:callbacks["upload_video_action"](chat_window),
        bg="#FF8C00", fg="white",
        font=("Segoe UI", 11, "bold"), width=16).pack(side=tk.LEFT, padx=5)
    
    # -----------------------------
    # Button to open scheduler
    # -----------------------------
    tk.Button(
        root,
        text="📅 Schedule Upload",
        font=("Segoe UI", 11, "bold"),
        bg="#0078D7",
        fg="white",
        width=20,
        command=lambda:callbacks["open_schdeuler"](chat_window)
    ).pack(pady=20)
    
    #Confirm button to Schedule

   
    return root, chat_window


