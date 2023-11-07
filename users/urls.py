from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.login, name="home"),
    path('user-login/',views.user_login, name="login"),
    path('short-course-view/',views.short_course_view,name="short-course-view"),
    path('short-course-create/',views.short_course_create, name="short-course-create"),
    path('add-new-course/',views.add_new_course, name='add-new-course'),
    path('profile/',views.profile, name="profile"),
    path('password-change/',views.password_change, name="password-change")
]