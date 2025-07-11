from django.urls import path
from .views import *


urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('shop',shop_view, name = "shop"),
    # path('free-plan',free_plan, name = "free-plan"),
    path('classes/', classes_list, name='classes_list'),
    path('attend/', attend_class, name='attend_class'),

]