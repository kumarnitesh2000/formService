from django.urls import path
from . import views
urlpatterns = [
    path('create',views.create,name="create"),
    path('response',views.response,name="response"),
    path('form_info/<int:id>',views.formInfo,name="form_info")
]