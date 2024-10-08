from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Ensure that the publication_year is not in the future.
        """
        
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future')
        return value
    