from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    verbose_name = 'Новости' #можем писать конфигурацию в NewsConfig,потому что в settings указали news.apps.NewsConfig, а не news
