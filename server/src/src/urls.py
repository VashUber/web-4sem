"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api.views import (
    ArticleViewSet,
    CountUserArticleView,
    ReadArticlesView,
    TopArticlesView,
    UserArticleView,
)
from comments.views import CommentViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from users.views import (
    CurrentUserView,
    EmailVerifyView,
    RegistrationView,
    UserView,
)

router = DefaultRouter()
router.register(r"articles", ArticleViewSet, basename="articles")
router.register(r"comments", CommentViewSet, basename="comments")


urlpatterns = [
    path("auth", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    path('djoser/', include('djoser.urls')),
    path('djoser/', include('djoser.urls.jwt')),
    path('djoser/', include('djoser.social.urls')),
    path("articles/top",
         TopArticlesView.as_view({"get": "list"}), name="top-articles"),
    path(
        "articles/read", ReadArticlesView.as_view({"get": "list"}), name="read-articles"
    ),
    path("email-verify", EmailVerifyView.as_view(), name="email-verify"),
    path(
        "accounts/<int:pk>/article",
        UserArticleView.as_view({"get": "list"}),
        name="user-article",
    ),
    path("accounts/<int:pk>", UserView.as_view(), name="user"),
    path(
        "accounts/<int:pk>/count",
        CountUserArticleView.as_view({"get": "list"}),
        name="user",
    ),
    path("accounts/current", CurrentUserView.as_view(), name="current"),
    path("accounts/register", RegistrationView.as_view(), name="register"),
    path(
        "api_schema/",
        get_schema_view(title="API Schema",
                        description="Guide for the REST API"),
        name="api_schema",
    ),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="docs.html", extra_context={"schema_url": "api_schema"}
        ),
        name="swagger-ui",
    ),
    *router.urls,
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
