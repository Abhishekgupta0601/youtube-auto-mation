from tkinter import END
import google.auth.transport.requests
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import gui_logic

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

#Verify Youtube token
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_youtube_service():
    creds = None

    # 1️⃣ Load saved token
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # 2️⃣ If token expired, refresh
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # 3️⃣ If no token → login ONCE
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json",
            SCOPES
        )
        creds = flow.run_local_server(port=0)

        # 💾 SAVE TOKEN
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)


#Upload Video to Youtube
def upload_youtube_video(video_path,chat_window):
    if not video_path:
        chat_window.config(state="normal")
        chat_window.insert(
            END,
            "❌ Please select video path.\n\n",
            "bot"
        )
        chat_window.config(state="disabled")
        return
    
    chat_window.config(state="normal")
    chat_window.insert(
        END,
        f"🎬 Uploading video using:\n{video_path}\n{video_path}\n\n",
        "bot"
    )
    # chat_window.config(state=tk.DISABLED)

    title="Second Video"
    description="My Second AI Generated Video"

    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES
    )
    credentials = flow.run_local_server(port=0)

    # youtube = build("youtube", "v3", credentials=credentials)
    youtube=get_youtube_service()

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["AI", "Automation", "Python", "Ollama"],
            "categoryId": "22"  # People & Blogs
        },
        "status": {
            "privacyStatus": "public"  # public | private | unlisted
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = request.execute()
    print("✅ Video uploaded successfully!")
    print("🎬 Video ID:", response["id"])
    chat_window.insert(
        END,
        f"🎬 Video Uploaded Successfully\n\n",
        "bot"
    )
    chat_window.config(state="disabled")





    


