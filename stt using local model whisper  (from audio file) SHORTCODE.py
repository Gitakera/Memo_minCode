# pip install transformers torchaudio librosa


from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import torch

# Charger le modèle et le processeur
processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")

# Charger l'audio (converti à 16kHz)
audio, sr = librosa.load("tempsaparis.mp3", sr=16000)

# Préparer l'entrée
inputs = processor(audio, sampling_rate=16000, return_tensors="pt")

# Forcer la traduction vers l'anglais (ou utilise "transcribe" pour rester dans la langue d'origine)
model.config.forced_decoder_ids = processor.get_decoder_prompt_ids(language="fr", task="translate")

# Générer et décoder
with torch.no_grad():
    ids = model.generate(inputs.input_features)
    text = processor.batch_decode(ids, skip_special_tokens=True)[0]

print("📝 Résultat :", text)
