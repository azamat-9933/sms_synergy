from django.urls import path
from .views import *

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq-list'),
    path('general/', GeneralView.as_view(), name='general-info'),
    path('team-members/', TeamMemberListView.as_view(), name='team-members-list'),
    path('offices/', OfficeListView.as_view(), name='office-list'),
    path('posts/', PostListView.as_view(), name='posts-news-list'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-news-detail'),
    path('partners/', PartnerListView.as_view(), name='partners-funds-list'),
    path('services/', ServiceListView.as_view(), name='services-list'),
    path('projects/', ProjectsListView.as_view(), name='projects-list'),
    path('applications/', ApplicationCreateView.as_view(), name='application-create'),
    path('user-email/', UserEmailCreateView.as_view(), name='user-email-create'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:id>/', NewsDetailView.as_view(), name='news-detail')
]