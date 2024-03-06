from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Supondo que o modelo de perfil do usuário tenha um campo 'timezone'
            tz_str = request.user.timezone
            if tz_str:
                timezone.activate(tz_str)
            else:
                timezone.deactivate()
        response = self.get_response(request)
        return response
