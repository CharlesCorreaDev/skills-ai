from django.apps import AppConfig

class ExampleExtensionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'example_extension'
    label = 'example_extension'
    verbose_name = 'Example Extension for Gravewright'

    def ready(self):
        # EN: Optional domain API registrations for trusted server extensions
        # PT-BR: Registro opcional de operações de domínio quando o Django estiver pronto
        pass
