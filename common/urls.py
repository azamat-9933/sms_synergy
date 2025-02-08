from django.urls import path

from common.views import *

urlpatterns = [
    path('main-page/first-banner/', MainPageFirstBannerView.as_view(), name='main-page-first-banner'),
    path('main-page/about-us/', MainPageAboutUsSectionView.as_view(), name='main-page-about-us'),
    path('main-page/our-services/', MainPageOurServicesSectionView.as_view(), name='main-page-our-services'),
    path('main-page/second-banner/', MainPageSecondBannerView.as_view(), name='main-page-second-banner'),
    path('main-page/our-partners/', MainPageOurPartnersSectionView.as_view(), name='main-page-our-partners'),
    path('main-page/our-mission/', MainPageOurMissionSectionView.as_view(), name='main-page-our-mission'),
    path('main-page/third-banner/', MainPageThirdBannerView.as_view(), name='main-page-third-banner'),
    path('main-page/statistics/', MainPageStatisticsSectionView.as_view(), name='main-page-statistics'),
    path('main-page/last-banner/', MainPageLastBannerView.as_view(), name='main-page-last-banner'),
    path('about-page/first-banner/', AboutPageFirstBannerView.as_view(), name='about-page-first-banner'),
    path('about-page/our-story/', AboutPageOurStorySectionView.as_view(), name='about-page-our-story'),
    path('about-page/second-banner/', AboutPageSecondBannerView.as_view(), name='about-page-second-banner'),
    path('about-page/our-team/', AboutPageOurTeamSectionView.as_view(), name='about-page-our-team'),
    path('about-page/last-banner/', AboutUsPageLastBannerView.as_view(), name='about-page-last-banner'),
    path('services-page/first-banner/', ServicesPageFirstBannerView.as_view(), name='services-page-first-banner'),
    path('services-page/second-banner/', OurServicesSecondBannerView.as_view(), name='services-page-second-banner'),
    path('projects-page/first-banner/', OurProjectsPageFirstBannerView.as_view(), name='projects-page-first-banner'),
    path('team-page/first-banner/', OurTeamPageFirstBannerView.as_view(), name='team-page-first-banner'),
    path('team-page/our-team/', OurTeamPageOurTeamSectionView.as_view(), name='team-page-our-team'),
    path('team-page/second-banner/', OurTeamPageSecondBannerView.as_view(), name='team-page-second-banner'),
    path('blog-page/first-banner/', BlogPageFistBannerView.as_view(), name='blog-page-first-banner'),
    path('blog-page/second-banner/', BlogPageSecondBannerView.as_view(), name='blog-page-second-banner'),
    path('post-page/first-banner/', PostPageFirstBannerView.as_view(), name='post-page-first-banner'),
    path('post-page/second-banner/', PostPageSecondBannerView.as_view(), name='post-page-second-banner'),
    path('contact-page/first-banner/', ContactPageFirstBannerView.as_view(), name='contact-page-first-banner'),
    path('contact-page/second-banner/', ContactPageSecondBannerView.as_view(), name='contact-page-second-banner'),
]
