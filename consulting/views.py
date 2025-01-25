from rest_framework import generics

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import *


class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class GeneralView(generics.RetrieveAPIView):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer

    def get_object(self):
        return General.objects.first()


class TeamMemberListView(generics.ListAPIView):
    serializer_class = TeamMemberSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'main_page',
                openapi.IN_QUERY,
                description="If true, return the last 4 team members",
                type=openapi.TYPE_BOOLEAN
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = TeamMember.objects.all()
        main_page = self.request.query_params.get('main_page')
        if main_page == 'true':
            return queryset.order_by('-id')[:4]  # последние 4 участника
        return queryset


class OfficeListView(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.filter(is_published=True)  # Только опубликованные записи


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(is_published=True)  # Только опубликованные записи
    serializer_class = PostDetailSerializer
    lookup_field = 'id'  # Поиск будет по полю id


class PartnerListView(generics.ListAPIView):
    serializer_class = PartnerSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'main_page',
                openapi.IN_QUERY,
                description="If true, return the last 4 team members",
                type=openapi.TYPE_BOOLEAN
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = TeamMember.objects.all()
        main_page = self.request.query_params.get('main_page')
        if main_page == 'true':
            return queryset.order_by('-id')[:10]  # последние 4 участника
        return queryset


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'main_page',
                openapi.IN_QUERY,
                description="Filter by main page services (main_page=true)",
                type=openapi.TYPE_BOOLEAN
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Service.objects.all()
        main_page_param = self.request.query_params.get('main_page')

        if main_page_param == 'true':
            return queryset[:6]  # Отдаем только 6 сервисов для главной страницы
        return queryset  # Если параметр не передан, возвращаем все сервисы


class ProjectsListView(generics.ListAPIView):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return Projects.objects.all()  # Возвращаем все проекты


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class UserEmailCreateView(generics.CreateAPIView):
    queryset = UserEmail.objects.all()  # Указываем queryset, хотя он не обязательный
    serializer_class = UserEmailSerializer



class NewsListView(generics.ListAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.filter(is_published=True)  # Только опубликованные записи


class NewsDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(is_published=True)  # Только опубликованные записи
    serializer_class = PostDetailSerializer
    lookup_field = 'id'  # Поиск будет по полю id
