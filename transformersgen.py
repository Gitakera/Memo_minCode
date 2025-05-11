# pip install transformers
# pip install torch

from transformers import pipeline

# condition = pipeline("summarization")  //run but no recommended
condition = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")
# texte = input("Saisir une histoire : ")
texte = "Après une journée bien remplie vient le moment d’aller au lit."
texte +="Mais votre petit, summarizationlui, n’en a pas forcément très envie."
texte +="Il fait même parfois durer ce moment un peu plus longtemps que prévu, et vous pouvez vous sentir agacé ou démuni."
texte +="Alors... comment gérer au mieux le coucher ? Même s’il n’existe pas de recette magique, quelques repères et quelques clés peuvent cependant vous accompagner. Un enfant est un être en pleine construction avec des besoins qui changent. Il y a des périodes où lui aussi, tout comme vous, peut avoir du mal à s’endormir."
texte +="Cela peut être lié à des événements particuliers (rentrée à l’école, naissance, déménagement, problèmes familiaux...) et aussi parce qu’il grandit, passe des caps. Dans cette évolution permanente, certains besoins doivent être respectés : • Le rythme Bien avant le coucher : - votre enfant et vous avez eu une journée remplie d’émotions, d’expériences diverses."
texte +="En rentrant à la maison, votre enfant peut avoir besoin de se défouler. S’il est encore tôt, il est possible d’aller jouer dehors, au parc, ou bien de jouer à cache cache, à chat perché à l’intérieur de votre maison ou de votre appartement. - Ensuite, le retour au calme doit s’amorcer par un jeu plus calme si vous avez le temps, sinon le bain, le repas, puis un coloriage."


summary = condition(texte, max_length = 100, min_length = 50, do_sample = False)

print("\n================================")
print("Texte original:"+str(texte))

print("\n================================")

print("\n================================RESUME =================================")
print(summary[0]['summary_text'])
print("\n================================ RESUME =================================")

