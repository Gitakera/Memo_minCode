import warnings
warnings.filterwarnings("ignore", message=".*past_key_values.*")

import torch
import librosa
import numpy as np
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# 🔁 Paramètres utilisateur
FILE_PATH = "tempsaparis.mp3"
MODE = "auto"  # "transcribe", "translate", "auto"
CHUNK_DURATION = 30  # secondes

# ⚡️ GPU + precision
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# 🔧 Chargement du modèle
processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2").to(device).to(dtype)
model.eval()

# 🎧 Chargement audio complet
audio_array, sr = librosa.load(FILE_PATH, sr=16000)

# 🔪 Découpage en chunks de 30s
chunk_size = CHUNK_DURATION * sr
num_chunks = int(np.ceil(len(audio_array) / chunk_size))

transcription = ""

print(f"🔊 Audio total : {len(audio_array)/sr:.1f}s → {num_chunks} morceaux de {CHUNK_DURATION}s")

for i in range(num_chunks):
    start = i * chunk_size
    end = min((i + 1) * chunk_size, len(audio_array))
    chunk = audio_array[start:end]

    # 🎛️ Préparation
    inputs = processor(chunk, sampling_rate=16000, return_tensors="pt")
    input_features = inputs.input_features.to(device).to(dtype)

    # 🧠 Mode
    if MODE == "transcribe":
        forced_ids = processor.get_decoder_prompt_ids(task="transcribe")
    elif MODE == "translate":
        forced_ids = processor.get_decoder_prompt_ids(task="translate", language="en")
    else:
        forced_ids = None  # Auto : Whisper choisit

    # 📝 Inference
    with torch.no_grad():
        predicted_ids = model.generate(
            input_features,
            forced_decoder_ids=forced_ids,
            max_new_tokens=444
        )
        chunk_text = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        transcription += chunk_text.strip() + "\n"
        print(f"🧩 Chunk {i+1}/{num_chunks} OK")

# 💾 Résultat
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(transcription)

print("\n✅ Transcription terminée. Résultat sauvegardé dans transcription.txt")
