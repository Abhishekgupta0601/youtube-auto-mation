from tkinter import filedialog, END
from gtts import gTTS
import json
import subprocess
import requests

MODEL = "llama3"
OLLAMA_URL = "http://localhost:11434/api/generate"

#Generate Ollama Response
def generate_response(prompt,chat_window):
 
    response = ask_local(prompt)

    if not response or not response.strip():
        print("❌ Empty response from Ollama")
        return
    
    chat_window.config(state="normal")
    chat_window.insert(END, f"Ollama: {response}\n\n", "bot")
    chat_window.config(state="disabled")
    chat_window.yview(END)
    
    text = response
    language = "en"

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")

    print("Audio file saved as output.mp3")
    
   


    FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

    subprocess.run([
    FFMPEG_PATH,
    "-y",
    "-loop", "1",
    "-i", "image.jpg",
    "-i", "output.mp3",
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



def ask_local(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt},
            stream=True,
            timeout=120
        )

        result = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    if "response" in data:
                        result += data["response"]
                except json.JSONDecodeError:
                    continue
        return result.strip() if result else "[No response]"
    except Exception as e:
        return f"[Error contacting Ollama] {e}"


# # Enter key binding
# def on_enter(event):
#     send_message()
#     return "break"

# entry_box.bind("<Return>", on_enter)
