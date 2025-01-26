from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class MainPageFirstBanner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    back_image = models.ImageField(upload_to="common/images/")
    number = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Header Main Banner'
        verbose_name_plural = 'Header Main Banners'


class MainPageAboutUsSection(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field()

    class Meta:
        verbose_name = 'About Us Section'
        verbose_name_plural = 'About Us Sections'


class MainPageOurServicesSection(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field()

    class Meta:
        verbose_name = 'Services Section'
        verbose_name_plural = 'Services Sections'


class MainPageSecondBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Main Page Second Banner'
        verbose_name_plural = 'Main Page Second Banners'


class MainPageOurPartnersSection(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field()

    class Meta:
        verbose_name = 'Our Partners Section'
        verbose_name_plural = 'Our Partners Sections'


class MainPageOurMissionSection(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field()

    class Meta:
        verbose_name = 'Our Mission Section'
        verbose_name_plural = 'Our Mission Sections'


class MainPageThirdBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Main Page Third Banner'
        verbose_name_plural = 'Main Page Third Banners'


class MainPageStatisticsSection(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field()

    first_number = models.IntegerField()
    first_title = models.CharField(max_length=255)

    second_number = models.IntegerField()
    second_title = models.CharField(max_length=255)

    third_number = models.IntegerField()
    third_title = models.CharField(max_length=255)

    fourth_number = models.IntegerField()
    fourth_title = models.CharField(max_length=255)

    right_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Statistics Section'
        verbose_name_plural = 'Statistics Sections'


class MainPageLastBanner(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field()
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Main Page Last Banner'
        verbose_name_plural = 'Main Page Last Banners'


class AboutPageFirstBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'About Page First Banner'
        verbose_name_plural = 'About Page First Banners'


class AboutPageOurStorySection(models.Model):
    text = CKEditor5Field()

    class Meta:
        verbose_name = 'About Section'
        verbose_name_plural = 'About Sections'


class AboutPageSecondBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'About Page Second Banner'
        verbose_name_plural = 'About Page Second Banners'


class AboutPageOurTeamSection(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field()

    class Meta:
        verbose_name = 'Our Team Page'
        verbose_name_plural = 'Our Team Pages'


class AboutUsPageLastBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")
    description = CKEditor5Field()

    class Meta:
        verbose_name = 'Our Team Last Banner'
        verbose_name_plural = 'Our Team Last Banners'


class ServicesPageFirstBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Services Page First Banner'
        verbose_name_plural = 'Services Page First Banners'


class OurServicesSecondBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Our Services Second Banner'
        verbose_name_plural = 'Our Services Second Banners'


class OurProjectsPageFirstBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Our Projects Page First Banner'
        verbose_name_plural = 'Our Projects Page First Banners'


class OurTeamPageFirstBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Our Team Page First Banner'
        verbose_name_plural = 'Our Team Page First Banners'


class OurTeamPageOurTeamSection(models.Model):
    text = CKEditor5Field()

    class Meta:
        verbose_name = 'Our Team Section'
        verbose_name_plural = 'Our Team Sections'


class OurTeamPageSecondBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Our Team Page Second Banner'
        verbose_name_plural = 'Our Team Page Second Banners'


class BlogPageFistBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Blog Page First Banner'
        verbose_name_plural = 'Blog Page First Banners'


class BlogPageSecondBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Blog Page Second Banner'
        verbose_name_plural = 'Blog Page Second Banners'

class PostPageFirstBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Post Page First Banner'
        verbose_name_plural = 'Post Page First Banners'


class PostPageSecondBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Post Page Second Banner'
        verbose_name_plural = 'Post Page Second Banners'


class ContactPageFirstBanner(models.Model):
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Contact Page First Banner'
        verbose_name_plural = 'Contact Page First Banners'


class ContactPageSecondBanner(models.Model):
    title = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to="common/images/")

    class Meta:
        verbose_name = 'Contact Page Second Banner'
        verbose_name_plural = 'Contact Page Second Banners'

