from bs4 import BeautifulSoup
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


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']
        read_only_fields = ['id', 'question', 'answer']


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ['email', 'phone', 'facebook', 'twitter', 'linkedin', 'instagram']
        read_only_fields = fields


class TeamMemberSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = TeamMember
        fields = ['full_name', 'position', 'image', 'facebook', 'linked_in']
        read_only_fields = fields


class OfficeSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = Office
        fields = ['city_name', 'email', 'phone', 'address', 'photo', 'created_at', 'main']
        read_only_fields = fields


class PostsSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = Post
        fields = ['id', 'title', 'photo', 'created_at']
        read_only_fields = fields


class PostDetailSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer для поля с изображением
    content = serializers.SerializerMethodField()  # Добавляем поле для обработки контента

    class Meta:
        model = Post
        fields = '__all__'  # Возвращаем все поля модели
        read_only_fields = fields

    def get_content(self, obj):
        content = obj.content
        # Парсим контент с помощью BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")

        # Ищем все теги <img> и обновляем их src
        for img_tag in soup.find_all("img"):
            if img_tag.get("src"):
                # Преобразуем относительные пути в абсолютные URL
                img_tag["src"] = self.context["request"].build_absolute_uri(img_tag["src"])

        # Возвращаем обновленный HTML-контент
        return str(soup)


class PartnerSerializer(serializers.ModelSerializer):
    logo_photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = Partner
        fields = ['id', 'logo_photo', 'title', 'description', 'fund_or_partner']
        read_only_fields = fields


class ServiceSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = Service
        fields = ['id', 'photo', 'title', 'description']
        read_only_fields = fields


class ProjectsSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = Projects
        fields = ['id', 'photo', 'title', 'description', 'since', 'till']
        read_only_fields = fields


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmail
        fields = ['email']


class NewsSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = News
        fields = ['id', 'title', 'photo', 'created_at']
        ordering = ['-created_at']
        read_only_fields = fields


class NewsDetailSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer для поля с изображением
    content = serializers.SerializerMethodField()  # Добавляем поле для обработки контента

    class Meta:
        model = Post
        fields = '__all__'  # Возвращаем все поля модели
        read_only_fields = fields

    def get_content(self, obj):
        content = obj.content
        # Парсим контент с помощью BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")

        # Ищем все теги <img> и обновляем их src
        for img_tag in soup.find_all("img"):
            if img_tag.get("src"):
                # Преобразуем относительные пути в абсолютные URL
                img_tag["src"] = self.context["request"].build_absolute_uri(img_tag["src"])

        # Возвращаем обновленный HTML-контент
        return str(soup)
