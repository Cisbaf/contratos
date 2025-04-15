from django.urls import path
from accounts import views

urlpatterns = [
    path('contract_create_user', views.create_user, name="contract_create_user"),
    path('delete/<int:pk>', views.delete_user, name="account_delete"),
    path('get_users', views.get_users, name="contract_get_users"),
    path('theme/<int:index>', views.define_color, name="theme"),
    path('fiscalFake', views.register_fiscais_fake)
]
