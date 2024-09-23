from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    # Set the default auto field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    # name of the app
    name = 'checkout'
