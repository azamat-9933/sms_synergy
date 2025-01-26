from django.contrib import admin
from .models import *

@admin.register(MainPageFirstBanner)
class MainPageFirstBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'back_image', 'number', 'name')

@admin.register(MainPageAboutUsSection)
class MainPageAboutUsSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(MainPageOurServicesSection)
class MainPageOurServicesSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(MainPageSecondBanner)
class MainPageSecondBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(MainPageOurPartnersSection)
class MainPageOurPartnersSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(MainPageOurMissionSection)
class MainPageOurMissionSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(MainPageThirdBanner)
class MainPageThirdBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(MainPageStatisticsSection)
class MainPageStatisticsSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'first_number', 'first_title', 'second_number', 'second_title', 'third_number', 'third_title', 'fourth_number', 'fourth_title', 'right_image')

@admin.register(MainPageLastBanner)
class MainPageLastBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'back_image')

@admin.register(AboutPageFirstBanner)
class AboutPageFirstBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(AboutPageOurStorySection)
class AboutPageOurStorySectionAdmin(admin.ModelAdmin):
    list_display = ('text',)

@admin.register(AboutPageSecondBanner)
class AboutPageSecondBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(AboutPageOurTeamSection)
class AboutPageOurTeamSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(AboutUsPageLastBanner)
class AboutUsPageLastBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image', 'description')

@admin.register(ServicesPageFirstBanner)
class ServicesPageFirstBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(OurServicesSecondBanner)
class OurServicesSecondBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(OurProjectsPageFirstBanner)
class OurProjectsPageFirstBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(OurTeamPageFirstBanner)
class OurTeamPageFirstBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(OurTeamPageOurTeamSection)
class OurTeamPageOurTeamSectionAdmin(admin.ModelAdmin):
    list_display = ('text',)

@admin.register(OurTeamPageSecondBanner)
class OurTeamPageSecondBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(BlogPageFistBanner)
class BlogPageFistBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(BlogPageSecondBanner)
class BlogPageSecondBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(PostPageFirstBanner)
class PostPageFirstBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(PostPageSecondBanner)
class PostPageSecondBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')

@admin.register(ContactPageFirstBanner)
class ContactPageFirstBannerAdmin(admin.ModelAdmin):
    list_display = ('back_image',)

@admin.register(ContactPageSecondBanner)
class ContactPageSecondBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'back_image')
