from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
    search_fields = ('question',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'email', 'phone', 'main', 'created_at')
    search_fields = ('city_name', 'email', 'phone')
    list_filter = ('main', 'created_at')
    ordering = ('-created_at',)

@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'created_at')
    search_fields = ('email', 'phone')
    ordering = ('-created_at',)

@admin.register(PostNews)
class PostNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_or_news', 'is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'short_desc')
    list_filter = ('post_or_news', 'is_published', 'created_at')
    ordering = ('-created_at',)

@admin.register(PartnerFund)
class PartnerFundAdmin(admin.ModelAdmin):
    list_display = ('title', 'fund_or_partner', 'created_at')
    search_fields = ('title',)
    list_filter = ('fund_or_partner', 'created_at')
    ordering = ('-created_at',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    ordering = ('-created_at',)

@admin.register(UserEmail)
class UserEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    ordering = ('-created_at',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position')
    list_display_links = ['full_name']
    search_fields = ('full_name', 'position')


class SMSCampaignAdmin(admin.ModelAdmin):
    list_display = ['subject', 'message', 'sent_at']

admin.site.register(SMSCampaign, SMSCampaignAdmin)