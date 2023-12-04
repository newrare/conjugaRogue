import random



class Aller():
    name        = "Arri"
    description = "Armand Arriver, surnommé 'Arri' a un incroyable  talent de jonglage. Sa technique est hilarante toutefois il arrive toujours à impressionner"



    def __str__(self):
        return self.name



    def present():
        sentences = [
            "Tu arrives à point nommé, mais que se passera-t-il quand les choses deviendront sérieuses ?",
            "Regarde bien, car quelque chose d'inattendu va arriver lors de notre rencontre !",
            "Les moments les plus drôles arrivent toujours quand Armand Arriver entre en scène !",
            "Sais-tu ce qui va arriver si tu sous-estimes mes talents ?",
            "Crois-moi, tu ne devineras jamais ce qui arrive quand j'entre en action !",
            "Les surprises désagréables arrivent chaque fois qu'Arri est impliqué !",
            "Prépare-toi, car c'est là que l'excitation va vraiment arriver, mon ami !",
            "Mes opportunités de succès continuent d'arriver tant que tu restes à mes côtés !",
            "Attends-toi à l'inattendu, car tu ne sais jamais ce qui va arriver avec ma technique personnelle !",
            "Les réussites vont arriver à ceux qui osent relever le défi avec détermination !",
            "Des perspectives nouvelles vont arriver si tu es prêt à les explorer avec moi !",
            "Des défis inattendus vont arriver, mais c'est ce qui rend la vie palpitante !",
            "Des moments époustouflants vont arriver, alors prépare-toi à être émerveillé !",
            "Les acclamations vont arriver quand Armand Arriver remportera cette victoire !",
            "Les changements positifs vont arriver quand tu accepteras le défi avec enthousiasme !",
            "Des découvertes incroyables vont arriver si tu oses t'aventurer dans l'inconnu !",
            "Attends-toi à des retournements de situation, car ils vont arriver sans crier gare !",
            "Des opportunités uniques vont arriver si tu te tiens à mes côtés, prêt à les saisir !",
            "Les moments mémorables vont arriver, et tu en feras partie intégrante !",
            "Des résultats exceptionnels vont arriver seulement si tu oses affronter le défi en face !"
        ]

        return random.choice(sentences)
