from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Article
from .pagination import CustomPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import ArticleSerializer







class TopArticlesView(mixins.ListModelMixin, GenericViewSet):
    authentication_classes = ()
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request):
        article = Article.objects.all().order_by("-count_reads")[::3]
        serializer = ArticleSerializer(article, many=True, context={"request": request})
        return Response(serializer.data)


class ReadArticlesView(mixins.ListModelMixin, GenericViewSet):
    authentication_classes = ()
    serializer_class = ArticleSerializer

    def list(self, request):
        article = Article.objects.all().order_by("-id")[::3]
        serializer = ArticleSerializer(article, many=True, context={"request": request})
        return Response(serializer.data)


class CountUserArticleView(mixins.ListModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = ArticleSerializer

    def list(self, request, pk):
        article = Article.objects.all().filter(author=pk).count()
        return Response(article)
