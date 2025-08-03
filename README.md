# Azure AI Avatar Video Generator

This is a simple Streamlit-based app that lets users generate avatar videos using **Azure's Talking Avatar API**. Users can input any text, and the app will synthesize an AI avatar video where the character (Lisa) speaks the input.

---

## 🚀 Features

- 🎤 Generate talking avatar videos from custom text.
- 🌐 Uses Azure Cognitive Services – Speech and Avatar APIs.
- 🧠 Customizable voice, character, and video settings.
- 🕓 Monitors generation status with polling.
- 🧪 Clean, interactive UI built with Streamlit.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** – UI rendering
- **Azure Cognitive Services** – Text-to-avatar video
- **Requests** – For API interaction
- **Logging** – For real-time job tracking

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/azure-avatar-video-generator.git
cd azure-avatar-video-generator
```
## 🧰 Configurable Options

You can modify the following inside `submit_synthesis()` in `app.py`:
```
| Setting                 | Default Value                 |
|-------------------------|-------------------------------|
| `voice`                | `en-US-AvaMultilingualNeural` |
| `talkingAvatarCharacter` | `Lisa`                       |
| `talkingAvatarStyle`   | `casual-sitting`              |
| `videoFormat`          | `mp4`                         |
| `subtitleType`         | `soft_embedded`               |
| `videoCodec`           | `h264`                        |
| `backgroundColor`      | `#FFFFFFFF`                   |

```
## 🧵 Future Improvements (optional)
✅ Multi-avatar support

🎙️ Voice preview per avatar