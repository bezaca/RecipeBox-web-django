from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from recipes.views import(
    LandingPageView, 
    SignupView
)
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LandingPageView.as_view(), name='landing-page'),
    path("recipes/", include("recipes.urls", namespace='recipes')),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("signup/", SignupView.as_view(), name='signup'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
