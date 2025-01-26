from rest_framework import serializers
from .models import *


class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        try:
            if hasattr(media, 'url'):
                return self.context["request"].build_absolute_uri(media.url)
            return None
        except Exception as e:
            return "http://testserver/media/default.jpg"  # Путь по умолчанию, если ошибка


class MainPageFirstBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = MainPageFirstBanner
        fields = ['id', 'title', 'description', 'back_image', 'number', 'name']
        read_only_fields = fields


class MainPageAboutUsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageAboutUsSection
        fields = ['id', 'title', 'description']
        read_only_fields = fields


class MainPageOurServicesSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageOurServicesSection
        fields = ['id', 'title', 'description']
        read_only_fields = fields


class MainPageSecondBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = MainPageSecondBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class MainPageOurPartnersSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageOurPartnersSection
        fields = ['id', 'title', 'description']
        read_only_fields = fields


class MainPageOurMissionSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageOurMissionSection
        fields = ['id', 'title', 'description']
        read_only_fields = fields


class MainPageThirdBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = MainPageThirdBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class MainPageStatisticsSectionSerializer(serializers.ModelSerializer):
    right_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = MainPageStatisticsSection
        fields = [
            'title', 'description',
            'first_number', 'first_title',
            'second_number', 'second_title',
            'third_number', 'third_title',
            'fourth_number', 'fourth_title',
            'right_image'
        ]
        read_only_fields = fields


class MainPageLastBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = MainPageLastBanner
        fields = ['id', 'title', 'description', 'back_image']
        read_only_fields = fields


class AboutPageFirstBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = AboutPageFirstBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class AboutPageOurStorySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPageOurStorySection
        fields = ['id', 'text']
        read_only_fields = fields


class AboutPageSecondBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = AboutPageSecondBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class AboutPageOurTeamSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPageOurTeamSection
        fields = ['id', 'title', 'description']
        read_only_fields = fields


class AboutUsPageLastBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = AboutUsPageLastBanner
        fields = ['id', 'title', 'back_image', 'description']
        read_only_fields = fields


class ServicesPageFirstBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = ServicesPageFirstBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class OurServicesSecondBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = OurServicesSecondBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class OurProjectsPageFirstBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = OurProjectsPageFirstBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class OurTeamPageFirstBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = OurTeamPageFirstBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class OurTeamPageOurTeamSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeamPageOurTeamSection
        fields = ['id', 'text']
        read_only_fields = fields


class OurTeamPageSecondBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = OurTeamPageSecondBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class BlogPageFistBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = BlogPageFistBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class BlogPageSecondBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = BlogPageSecondBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class PostPageFirstBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = PostPageFirstBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class PostPageSecondBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = PostPageSecondBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields


class ContactPageFirstBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = ContactPageFirstBanner
        fields = ['id', 'back_image']
        read_only_fields = fields


class ContactPageSecondBannerSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer(read_only=True)

    class Meta:
        model = ContactPageSecondBanner
        fields = ['id', 'title', 'back_image']
        read_only_fields = fields
