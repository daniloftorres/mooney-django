from django.apps import AppConfig


class TransactionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.erp.transaction'

    def ready(self):
        # Importa o módulo signals para garantir que os sinais sejam registrados
        import apps.erp.transaction.signals
