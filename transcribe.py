import subprocess
import whisper

def video_to_audio(video_path, audio_output_path):
    # Construct the FFmpeg command to extract audio from the video
    command = [
        'ffmpeg',     # The command to run FFmpeg
        '-i', video_path,   # Input file path (video)
        '-q:a', '0',   # Set the audio quality (0 is the highest)
        '-map', 'a',   # Select the audio stream
        audio_output_path  # Output file path (audio)
    ]
    # Run the command
    subprocess.run(command)

def transcribe_audio(audio_path):
    # Load the Whisper model
    model = whisper.load_model("tiny")
    # Transcribe the audio file
    result = model.transcribe(audio_path)
    # Return the transcribed text
    return result['text']

def save_transcription_to_file(transcription, file_path):
    # Save the transcription to a text file
    with open(file_path, 'w') as file:
        file.write(transcription)

# Example usage
video_path =  'Input.mp4'
audio_output_path = 'output.mp3'
transcription_output_path = 'text.txt'

# Convert video to audio
video_to_audio(video_path, audio_output_path)

# Transcribe audio to text
transcription = transcribe_audio(audio_output_path)

# Save transcription to a file
save_transcription_to_file(transcription, transcription_output_path)

print("Transcription saved to:", transcription_output_path)
