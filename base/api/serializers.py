from rest_framework.serializers import ModelSerializer
from base.models import book

class booksSerilizer(ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'