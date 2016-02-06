from django.conf.urls import patterns, include, url

urlpatterns = [
        url(r'^signup/$',UserRegistrationView.as_view(), name='signup')
]