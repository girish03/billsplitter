from django.conf.urls import url
from expenses import views

urlpatterns = [
    url(r'^add_expense', views.add_expense),
    url(r'^delete_expense', views.delete_expense),
    url(r'^divide_expense', views.divide_expense)
]