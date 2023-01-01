from rest_framework import serializers
from article.models import Article
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
        ]
        read_only_fields = ['author']
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'