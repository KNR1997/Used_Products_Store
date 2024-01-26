from rest_framework.serializers import ModelSerializer
from base.models import book
from base.models import review

class booksSerilizer(ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'

class reviewsSerilizer(ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'