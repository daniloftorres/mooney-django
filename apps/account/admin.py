from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Adicione o campo de timezone à lista de campos para serem exibidos na listagem de usuários
    list_display = UserAdmin.list_display + ('timezone',)

    # Adicione o campo de timezone ao fieldset para permitir a edição no formulário do usuário
    fieldsets = UserAdmin.fieldsets + (
        (_('Personal info'), {
         'fields': ('age', 'timezone', 'full_name', 'language')}),
    )

    # Se você quiser permitir a edição de timezone ao criar um novo usuário, atualize esta configuração também
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Personal info'), {
         'fields': ('age', 'timezone', 'full_name', 'language')}),
    )


# Registre o modelo CustomUser com o CustomUserAdmin personalizado
admin.site.register(CustomUser, CustomUserAdmin)
