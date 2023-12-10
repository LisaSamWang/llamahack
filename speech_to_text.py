from dotenv import load_dotenv
import assemblyai as aai
import os

load_dotenv()

# load API key from dot_env file
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

config = aai.TranscriptionConfig(
	speaker_labels=True,
	iab_categories=True,
)


def convert_speech_to_text():
	transcript = aai.Transcriber().transcribe(audioFile, config)
	for utterance in transcript.utterances:
		print(f"Speaker {utterance.speaker}: {utterance.text}")
	sentences = transcript.get_sentences()
	for sentence in sentences:
		print(f"'{sentence.text}', Start: {sentence.start} ms, End: {sentence.end} ms")
	return transcript.utterances
