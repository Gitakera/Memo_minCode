# pip install language-tool-python

import language_tool_python

tool = language_tool_python.LanguageTool('fr-FR')
texte = "Mon texte à corrigier"
erreurs= tool.check(texte)
correction = tool.correct(texte)

print("Text à corriger : ", texte)
print("Erreurs détectées : ", erreurs)
print("Texte corrigé : ", correction)

