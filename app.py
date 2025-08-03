import streamlit as st
import json
import logging
import os
import sys
import time
import uuid
import requests
from azure.identity import DefaultAzureCredential

# Logging setup
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
        format="[%(asctime)s] %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p %Z")
logger = logging.getLogger(__name__)

# Azure Speech config
SPEECH_ENDPOINT = os.getenv('SPEECH_ENDPOINT', "https://eastus2.api.cognitive.microsoft.com")
PASSWORDLESS_AUTHENTICATION = False
API_VERSION = "2024-04-15-preview"

def _create_job_id():
    return str(uuid.uuid4())

def _authenticate():
    if PASSWORDLESS_AUTHENTICATION:
        credential = DefaultAzureCredential()
        token = credential.get_token('https://cognitiveservices.azure.com/.default')
        return {'Authorization': f'Bearer {token.token}'}
    else:
        SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY", 'your-subscription-key-here')
        return {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

def submit_synthesis(job_id: str, text: str):
    url = f'{SPEECH_ENDPOINT}/avatar/batchsyntheses/{job_id}?api-version={API_VERSION}'
    header = {
        'Content-Type': 'application/json'
    }
    header.update(_authenticate())
    isCustomized = False

    payload = {
        'synthesisConfig': {
            "voice": 'en-US-AvaMultilingualNeural',
        },
        "inputKind": "plainText",
        "inputs": [
            {
                "content": text,
            },
        ],
        "avatarConfig":
            {
                "customized": isCustomized,
                "talkingAvatarCharacter": 'Lisa',
                "talkingAvatarStyle": 'casual-sitting',
                "videoFormat": "mp4",
                "videoCodec": "h264",
                "subtitleType": "soft_embedded",
                "backgroundColor": "#FFFFFFFF",
            }
    }

    response = requests.put(url, json.dumps(payload), headers=header)
    if response.status_code < 400:
        logger.info('Batch avatar synthesis job submitted successfully')
        logger.info(f'Job ID: {response.json()["id"]}')
        return True
    else:
        logger.error(f'Failed to submit batch avatar synthesis job: [{response.status_code}], {response.text}')
        return False

def get_synthesis(job_id):
    url = f'{SPEECH_ENDPOINT}/avatar/batchsyntheses/{job_id}?api-version={API_VERSION}'
    header = _authenticate()
    response = requests.get(url, headers=header)
    if response.status_code < 400:
        result = response.json()
        if result['status'] == 'Succeeded':
            return result["outputs"]["result"]
        return None
    else:
        logger.error(f'Failed to get batch synthesis job: {response.text}')
        return None

# --- Streamlit UI ---
st.title("Azure AI Avatar Video Generator")

user_text = st.text_area("Enter text for Lisa to speak:", "Hi, I'm Lisa, your AI interviewer!")
if st.button("Generate Video"):
    with st.spinner("Generating video..."):
        job_id = _create_job_id()
        if submit_synthesis(job_id, user_text):
            st.info("Video generation started. Waiting for completion...")
            video_url = None
            for _ in range(30):  # Wait up to ~2.5 minutes
                video_url = get_synthesis(job_id)
                if video_url:
                    break
                time.sleep(5)
            if video_url:
                st.success("Video is ready!")
                st.video(video_url)
            else:
                st.error("Video generation timed out. Please try again later.")
        else:
            st.error("Failed to submit video generation job. Check your Azure config.")

