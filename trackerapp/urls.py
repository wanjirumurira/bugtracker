from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('create_project',views.create_project,name='create_project'),
    path('register/',views.register,name='register'),
    path('login/',views.sign_in,name='login'),
    path('logout',views.sign_out,name='logout')


]+ static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)