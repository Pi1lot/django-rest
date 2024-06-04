from django.db import models

# Create your models here.

class Commentaire(models.Model):
    titre = models.CharField(max_length=50)
    commentaire = models.CharField(max_length=256)
    date_publication = models.DateField(auto_now=True)

    def __repr__(self):
        return self.titre

    def __str__(self):
        return f"Le commentaire {self.titre} créé le {self.date_publication}"
