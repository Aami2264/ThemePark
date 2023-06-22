from django.urls import path
from Frontend import views

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('homepage/',views.homepage,name="homepage"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('gallerydisp/', views.gallerydisp, name="gallerydisp"),
    path('activitydisp/', views.activitydisp, name="activitydisp"),
    path('activityeach/<int:dataid>', views.activityeach, name="activityeach"),
    path('contactus/', views.contactus, name="contactus"),
    path('feedback/', views.feedback, name="feedback"),
    path('map/', views.map, name="map"),
    path('ticketdetail/', views.ticketdetail, name="ticketdetail"),
    path('selectpack/', views.selectpack, name="selectpack"),
    path('familyform/', views.familyform, name="familyform"),
    path('savebooking/',views.savebooking,name="savebooking"),
    path('birthdayform/',views.birthdayform,name="birthdayform"),
    path('savebdaybooking/', views.savebdaybooking, name="savebdaybooking"),
    path('schoolform/', views.schoolform, name="schoolform"),
    path('saveschoolbooking/', views.saveschoolbooking, name="saveschoolbooking")

]