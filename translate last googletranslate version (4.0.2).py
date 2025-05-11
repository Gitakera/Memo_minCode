# pip install googletrans

import asyncio
from googletrans import Translator

async def translate_text(text, dest_language):
    translator = Translator()
    translation = await translator.translate(text, dest=dest_language)
    return translation.text, translation.src

if __name__ == '__main__':
    text_to_translate = input("Saisir votre texte: ")
    destination_language = input("Traduire en : ")

    translated_text, detected_lang = asyncio.run(
        translate_text(text_to_translate, destination_language)
    )

    print(f"Langue détectée : {detected_lang}")
    print(f"Texte traduit : {translated_text}")
