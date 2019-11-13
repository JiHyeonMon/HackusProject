
from django.contrib import admin
from django.urls import path, include

import hackusapp.views
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('', hackusapp.views.home, name='home'),
    path('challenge/', hackusapp.views.challenge, name='challenge'),
    path('introduce/', hackusapp.views.introduce, name='introduce'),
    path('tutorial/', hackusapp.views.tutorial, name='tutorial'),
    path('writeupboard/', hackusapp.views.writeupboard, name='writeupboard'),
    path('ctf/', hackusapp.views.ctf, name='ctf'),

    path('mypage/', hackusapp.views.mypage, name = 'mypage'),
    
]
