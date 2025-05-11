# please, remove newer version of googletrans and use below (or use translate last googletranslate version (4.0.2).py)
# pip install googletrans==4.0.0-rc1

from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

if __name__ == '__main__':
    text_to_translate = input("Saisir votre texte: ")
    destination_language = input("Tranduire en :")
    
    translated_text = translate_text(text_to_translate, destination_language)
    print(f"Texte traduit: {translated_text}")
    
