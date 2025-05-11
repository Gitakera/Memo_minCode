# usage : créer des sous-titre pour des vidéos, sortir du texte depuis un interview audio pour la rédaction
import warnings
warnings.filterwarnings("ignore", message=".*past_key_values.*")

import torch
import librosa
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# 🔁 Paramètres utilisateur
FILE_PATH = "tempsaparis.mp3"   # Remplace par ton fichier audio
MODE = "auto"                   # "transcribe", "translate", ou "auto"

# 🔧 Chargement du modèle
processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")

# 🎧 Chargement de l'audio avec attention mask
audio_array, sampling_rate = librosa.load(FILE_PATH, sr=16000)
inputs = processor(
    audio_array,
    sampling_rate=16000,
    return_tensors="pt",
    return_attention_mask=True
)

# 🧠 Détection de la langue via logits initiaux
with torch.no_grad():
    decoder_input_ids = torch.tensor([[model.config.decoder_start_token_id]])
    outputs = model(
        input_features=inputs.input_features,
        decoder_input_ids=decoder_input_ids
    )
    language_logits = outputs.logits[0, 0]
    language_token_id = torch.argmax(language_logits).item()
    language_token = processor.tokenizer.convert_ids_to_tokens([language_token_id])[0]
    language_code = language_token.replace("<|", "").replace("|>", "")

print(f"🌐 Langue détectée : {language_code}")

# 🎯 Choix du mode
if MODE == "transcribe":
    model.config.forced_decoder_ids = processor.get_decoder_prompt_ids(language=language_code, task="transcribe")
elif MODE == "translate":
    model.config.forced_decoder_ids = processor.get_decoder_prompt_ids(language="en", task="translate")
else:
    task = "transcribe" if language_code == "en" else "translate"
    lang_forced = "en" if task == "translate" else language_code
    model.config.forced_decoder_ids = processor.get_decoder_prompt_ids(language=lang_forced, task=task)
    print(f"🔄 Mode automatique : {task}")

# 📝 Génération du texte
with torch.no_grad():
    predicted_ids = model.generate(
        inputs.input_features,
        attention_mask=inputs.attention_mask
    )
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

print("📝 Résultat :", transcription)

# 💾 (Optionnel) Sauvegarde dans un fichier texte
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(transcription + "\n")
