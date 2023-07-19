from .models import Config


def config(request):
    return {'config': Config.objects.first()}
