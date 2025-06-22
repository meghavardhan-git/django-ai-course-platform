from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('mark_complete/<int:course_id>/', views.mark_complete, name='mark_complete'),
    path('gemini_chat/', views.gemini_chat, name='gemini_chat'),
    path('gemini_suggest_courses/', views.gemini_suggest_courses, name='gemini_suggest_courses'),
    path('signup/', views.signup, name='signup'),
    path('my_progress/', views.user_progress, name='user_progress'),
    path('import-courses/', views.import_courses, name='import_courses'),

]
