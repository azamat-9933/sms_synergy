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


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ['email', 'phone', 'facebook', 'twitter', 'linkedin', 'instagram']


class TeamMemberSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = TeamMember
        fields = ['full_name', 'position', 'image', 'facebook', 'linked_in']


class OfficeSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = Office
        fields = ['city_name', 'email', 'phone', 'address', 'photo', 'created_at', 'main']


class PostNewsSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = PostNews
        fields = ['id', 'title', 'photo', 'created_at']


class PostNewsDetailSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer для поля с изображением
    content = serializers.SerializerMethodField()  # Добавляем поле для обработки контента

    class Meta:
        model = PostNews
        fields = '__all__'  # Возвращаем все поля модели

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


class PartnerFundSerializer(serializers.ModelSerializer):
    logo_photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = PartnerFund
        fields = ['logo_photo', 'title', 'description', 'fund_or_partner']


class ServiceSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = Service
        fields = ['photo', 'title', 'description']


class ProjectsSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()  # Применяем MediaURLSerializer к полю с изображением

    class Meta:
        model = Projects
        fields = ['photo', 'title', 'description', 'since', 'till']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmail
        fields = ['email']
