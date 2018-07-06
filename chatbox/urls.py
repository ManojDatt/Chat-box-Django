from django.conf.urls import url
from .views import SessionView, LoginView, LogoutView, SignupView

urlpatterns = [
url(r'^$', SessionView.as_view(), name='new_session'),
url(r'^login/$', LoginView.as_view(), name='login'),
url(r'^logout$', LogoutView.as_view(), name='logout'),
url(r'^registration/$', SignupView.as_view(), name='registration')
]
