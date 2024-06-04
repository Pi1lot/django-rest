from rest_framework import serializers
from .models import Commentaire

# Equivalent du forms.py mais pour l'API
class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ["titre","commentaire", "date_publication"]
