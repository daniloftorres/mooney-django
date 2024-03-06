from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class UserLanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            user_language = getattr(request.user, 'language', 'en')
            translation.activate(user_language)
            request.LANGUAGE_CODE = translation.get_language()
