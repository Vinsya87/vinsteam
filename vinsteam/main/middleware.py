from django.conf import settings
from django.contrib.sessions.backends.base import SessionBase
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.cache import cache


class AnonymousSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        engine = __import__(settings.SESSION_ENGINE, {}, {}, [""])
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
        if not session_key:
            session_key = engine.SessionStore().session_key
            request.COOKIES[settings.SESSION_COOKIE_NAME] = session_key
        request.session = engine.SessionStore(session_key)
        request.session.modified = False
        request.session[settings.SESSION_COOKIE_NAME] = session_key
        cache.set(session_key, request.session._session, settings.SESSION_COOKIE_AGE)

        response = self.get_response(request)

        return response


class AnonymousSessionMixin:
    def __init__(self):
        super().__init__()
        self.anonymous_middleware = AnonymousSessionMiddleware

    def dispatch(self, request, *args, **kwargs):
        middleware = self.anonymous_middleware
        response = middleware(request)
        return super().dispatch(request, *args, **kwargs)
