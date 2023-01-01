
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse,HttpResponse
from article.models import Article
from article.serializers import ArticleListSerializer
from article.serializers import ArticleDetailSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import mixins #DRE中可以实现增删改查多继承的模块
from rest_framework import generics #DRE中可以实现增删改查多继承的模块
from rest_framework.permissions import IsAdminUser
from article.permissions import IsAdminUserOrReadOnly
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)#它在序列化数据真正保存之前调用
@api_view(['GET',"POST"])
def article_list(request):
    if request.method=="GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)#, safe=False)#, HttpResponse("Hello World!")\
    elif request.method=="POST":
        serializer=ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

