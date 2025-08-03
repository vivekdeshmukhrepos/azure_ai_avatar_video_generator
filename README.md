# Azure AI Avatar Video Generator

This is a simple Streamlit-based app that lets users generate avatar videos using **Azure's Talking Avatar API**. Users can input any text, and the app will synthesize an AI avatar video where the character (Lisa) speaks the input.

---

## 🚀 Features

- 🎤 Generate talking avatar videos from custom text.
- 🌐 Uses Azure Cognitive Services – Speech and Avatar APIs.
- 🧠 Customizable voice, character, and video settings.
- 🕓 Monitors generation status with polling.
---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** – UI rendering
- **Azure Cognitive Services** – Text-to-avatar video
- **Requests** – For API interaction
- **Logging** – For real-time job tracking

---

## 📦 Installation

### 1. Clone repository and run the application

```bash
git clone https://github.com/vivekdeshmukhrepos/azure_ai_avatar_video_generator.git
cd azure-avatar-video-generator
pip install -r requirements.txt
streamlit run app.py
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
## 🧵 Scalability
## 💰 Fintech

1. **Virtual Financial Advisors**  
   - Avatar explains investment products or financial plans to clients in plain language.  
   - Personalized video messages for onboarding or periodic portfolio updates.

2. **Compliance Training**  
   - AI avatars deliver mandatory compliance or regulatory training with a human face, improving engagement.

3. **Customer Service Automation**  
   - Front-facing avatars handle FAQs or explain procedures like loan applications, KYC, or credit scoring.

4. **Internal Communication**  
   - CEOs or team leads can send synthesized video messages to teams at scale using custom avatars.

---

## 🎓 E-Learning / EdTech

1. **Personalized Teaching Assistants**  
   - AI tutors teach concepts in math, science, or language learning, in multiple languages or voices.

2. **Course Narration**  
   - Convert textbook or presentation content into engaging video lectures using avatars.

3. **Student Engagement**  
   - Use characters (e.g., Lisa or custom avatars) to simulate interviews, oral exams, or storytelling.

4. **Accessibility**  
   - Video avatars can deliver content to users with visual or auditory impairments (with subtitles and expressive avatars).

---

## 🧑‍💼 HR & Recruitment

1. **Interview Simulation**  
   - Candidates can practice interviews with an AI avatar that asks and evaluates responses.

2. **Onboarding Guides**  
   - New hires receive orientation videos from virtual avatars—scalable and multilingual.

3. **Policy Communication**  
   - Convert HR documents into digestible video summaries with avatars.

---

## 🛒 Retail & Customer Support

1. **Product Demonstrations**  
   - Avatars can explain product features or how-to guides visually on e-commerce sites.

2. **Customer Service Bots**  
   - Front-line AI avatars can triage customer queries and route them to support channels.

---

## 🏥 Healthcare

1. **Patient Education**  
   - Explain medical conditions, treatments, or post-operative care using friendly avatar videos.

2. **Multilingual Healthcare Assistants**  
   - Deliver instructions in native languages for global patient bases, improving health literacy.

---

## 📈 Marketing & Communications

1. **Personalized Video Campaigns**  
   - Generate mass-scale, personalized avatar videos for outreach, leads, and retention.

2. **Dynamic Social Content**  
   - Turn blog posts, press releases, or announcements into engaging short videos.

 ## Resources
 https://speech.microsoft.com/portal/d0a5135b87df4e7e841a11a7a0600c83/livechat