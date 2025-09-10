import requests
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('MONSTER_API_KEY')

def transcribe_audio(audio_file_path):
    """Transcribes an audio file to text using MonsterAPI's Whisper model."""
    headers = {'Authorization': f'Bearer {api_key}'}
    # ... (rest of the function is the same)
    data = {'model': 'whisper', 'input': {'file': audio_file_path}}
    response = requests.post('https://api.monsterapi.ai/v1/generate', headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['result']['text']
    else:
        print(f"Error in transcription: {response.text}")
        return None

def generate_image(prompt):
    """Generates an image from a text prompt using MonsterAPI's Stable Diffusion XL model."""
    headers = {'Authorization': f'Bearer {api_key}'}
    # ... (rest of the function is the same)
    data = {'model': 'sdxl', 'input': {'prompt': prompt}}
    response = requests.post('https://api.monsterapi.ai/v1/generate', headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['result']['output'][0]
    else:
        print(f"Error in image generation: {response.text}")
        return None

def speech_to_image(audio_file_path):
    """Main function to orchestrate the speech-to-image process."""
    if not api_key:
        print("API key not found. Please set MONSTER_API_KEY in your .env file.")
        return

    print("Transcribing audio...")
    transcribed_text = transcribe_audio(audio_file_path)

    if transcribed_text:
        print(f"Transcription complete: '{transcribed_text}'")
        print("Generating image from text...")
        image_url = generate_image(transcribed_text)
        
        if image_url:
            print(f"Image generated successfully! URL: {image_url}")
        else:
            print("Image generation failed.")
    else:
        print("Transcription failed.")

# Example usage:
# speech_to_image('path/to/your/audio.wav')