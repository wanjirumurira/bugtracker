from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.sign_in,name='login')

]+ static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)