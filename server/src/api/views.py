from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Article
from .pagination import CustomPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import ArticleSerializer

class StandardResultsSetPagination(CustomPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by("-id")
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly, )

    def retrieve(self, request, pk):
        article = self.queryset.get(pk=pk)
        article.count_reads += 1
        article.save()
        serializer = self.get_serializer(article)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def comments(self, request, pk=None, *args, **kwargs):
        comments = list(Comment.objects.filter(article=pk).order_by("-created_at"))
        answers = CommentSerializer(comments, context={"request": request}, many=True)

        return Response(answers.data)


class UserArticleView(mixins.ListModelMixin, GenericViewSet):
    queryset = Article.objects.all().order_by("-id")
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination

    def list(self, request, pk):
        queryset = self.filter_queryset(self.get_queryset().filter(author=pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
