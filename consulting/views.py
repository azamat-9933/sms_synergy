from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import *
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


class PostNewsListView(generics.ListAPIView):
    serializer_class = PostNewsSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'news',
                openapi.IN_QUERY,
                description="Filter by news (news=True)",
                type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter(
                'blog',
                openapi.IN_QUERY,
                description="Filter by blog posts (blog=True)",
                type=openapi.TYPE_BOOLEAN
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = PostNews.objects.filter(is_published=True)
        news_param = self.request.query_params.get('news')
        blog_param = self.request.query_params.get('blog')

        if news_param == 'true':
            return queryset.filter(post_or_news=PostNews.PostOrNewsChoices.NEWS)
        elif blog_param == 'true':
            return queryset.filter(post_or_news=PostNews.PostOrNewsChoices.POST)
        return queryset


class PostNewsDetailView(generics.RetrieveAPIView):
    queryset = PostNews.objects.filter(is_published=True)  # Только опубликованные записи
    serializer_class = PostNewsDetailSerializer
    lookup_field = 'id'  # Поиск будет по полю id


class PartnerFundListView(generics.ListAPIView):
    serializer_class = PartnerFundSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'partner',
                openapi.IN_QUERY,
                description="Filter by partners (partner=True)",
                type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter(
                'fund',
                openapi.IN_QUERY,
                description="Filter by funds (fund=True)",
                type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter(
                'main_page',
                openapi.IN_QUERY,
                description="Show only 4 latest partners for the main page (main_page=True)",
                type=openapi.TYPE_BOOLEAN
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = PartnerFund.objects.all()
        partner_param = self.request.query_params.get('partner')
        fund_param = self.request.query_params.get('fund')
        main_page_param = self.request.query_params.get('main_page')

        if partner_param == 'true' and main_page_param == 'true':
            return queryset.filter(fund_or_partner=PartnerFund.PartnerOrFundChoices.PARTNER).order_by('-created_at')[:4]
        elif partner_param == 'true':
            return queryset.filter(fund_or_partner=PartnerFund.PartnerOrFundChoices.PARTNER)
        elif fund_param == 'true':
            return queryset.filter(fund_or_partner=PartnerFund.PartnerOrFundChoices.FUNDS)
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

