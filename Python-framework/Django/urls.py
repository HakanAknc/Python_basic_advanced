from django.contrib import admin
from django.urls import path
from .views import merhaba_dunya

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', merhaba_dunya),  # Anasayfa "Merhaba, Dünya!" yazacak
]