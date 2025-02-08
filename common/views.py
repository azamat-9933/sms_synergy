from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import *

class FirstObjectView(generics.RetrieveAPIView):
    def get_object(self):
        obj = self.model.objects.first()
        if not obj:
            raise NotFound("No object found.")
        return obj

class MainPageFirstBannerView(FirstObjectView):
    model = MainPageFirstBanner
    serializer_class = MainPageFirstBannerSerializer

class MainPageAboutUsSectionView(FirstObjectView):
    model = MainPageAboutUsSection
    serializer_class = MainPageAboutUsSectionSerializer

class MainPageOurServicesSectionView(FirstObjectView):
    model = MainPageOurServicesSection
    serializer_class = MainPageOurServicesSectionSerializer

class MainPageSecondBannerView(FirstObjectView):
    model = MainPageSecondBanner
    serializer_class = MainPageSecondBannerSerializer

class MainPageOurPartnersSectionView(FirstObjectView):
    model = MainPageOurPartnersSection
    serializer_class = MainPageOurPartnersSectionSerializer

class MainPageOurMissionSectionView(FirstObjectView):
    model = MainPageOurMissionSection
    serializer_class = MainPageOurMissionSectionSerializer

class MainPageThirdBannerView(FirstObjectView):
    model = MainPageThirdBanner
    serializer_class = MainPageThirdBannerSerializer

class MainPageStatisticsSectionView(FirstObjectView):
    model = MainPageStatisticsSection
    serializer_class = MainPageStatisticsSectionSerializer

class MainPageLastBannerView(FirstObjectView):
    model = MainPageLastBanner
    serializer_class = MainPageLastBannerSerializer

class AboutPageFirstBannerView(FirstObjectView):
    model = AboutPageFirstBanner
    serializer_class = AboutPageFirstBannerSerializer

class AboutPageOurStorySectionView(FirstObjectView):
    model = AboutPageOurStorySection
    serializer_class = AboutPageOurStorySectionSerializer

class AboutPageSecondBannerView(FirstObjectView):
    model = AboutPageSecondBanner
    serializer_class = AboutPageSecondBannerSerializer

class AboutPageOurTeamSectionView(FirstObjectView):
    model = AboutPageOurTeamSection
    serializer_class = AboutPageOurTeamSectionSerializer

class AboutUsPageLastBannerView(FirstObjectView):
    model = AboutUsPageLastBanner
    serializer_class = AboutUsPageLastBannerSerializer

class ServicesPageFirstBannerView(FirstObjectView):
    model = ServicesPageFirstBanner
    serializer_class = ServicesPageFirstBannerSerializer

class OurServicesSecondBannerView(FirstObjectView):
    model = OurServicesSecondBanner
    serializer_class = OurServicesSecondBannerSerializer

class OurProjectsPageFirstBannerView(FirstObjectView):
    model = OurProjectsPageFirstBanner
    serializer_class = OurProjectsPageFirstBannerSerializer

class OurTeamPageFirstBannerView(FirstObjectView):
    model = OurTeamPageFirstBanner
    serializer_class = OurTeamPageFirstBannerSerializer

class OurTeamPageOurTeamSectionView(FirstObjectView):
    model = OurTeamPageOurTeamSection
    serializer_class = OurTeamPageOurTeamSectionSerializer

class OurTeamPageSecondBannerView(FirstObjectView):
    model = OurTeamPageSecondBanner
    serializer_class = OurTeamPageSecondBannerSerializer

class BlogPageFistBannerView(FirstObjectView):
    model = BlogPageFistBanner
    serializer_class = BlogPageFistBannerSerializer

class BlogPageSecondBannerView(FirstObjectView):
    model = BlogPageSecondBanner
    serializer_class = BlogPageSecondBannerSerializer

class PostPageFirstBannerView(FirstObjectView):
    model = PostPageFirstBanner
    serializer_class = PostPageFirstBannerSerializer

class PostPageSecondBannerView(FirstObjectView):
    model = PostPageSecondBanner
    serializer_class = PostPageSecondBannerSerializer

class ContactPageFirstBannerView(FirstObjectView):
    model = ContactPageFirstBanner
    serializer_class = ContactPageFirstBannerSerializer

class ContactPageSecondBannerView(FirstObjectView):
    model = ContactPageSecondBanner
    serializer_class = ContactPageSecondBannerSerializer

