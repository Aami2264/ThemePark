from django.urls import path
from Backend import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('addstaff/',views.addstaff, name="addstaff"),
    path('saveadmin/',views.saveadmin, name="saveadmin"),
    path('displayadmin/', views.displayadmin, name="displayadmin"),
    path('delete/<int:dataid>',views.delete,name="delete"),
    path('edit/<int:dataid>', views.edit, name="edit"),
    path('update/<int:dataid>',views.update,name="update"),
    path('addtickets/',views.addtickets,name="addtickets"),
    path('saveticket/', views.saveticket, name="saveticket"),
    path('displaytickets/', views.displaytickets, name="displaytickets"),
    path('editicket/<int:dataid>', views.editticket, name="editticket"),
    path('deleteticket/<int:dataid>', views.deleteticket, name="deleteticket"),
    path('updateticket/<int:dataid>', views.updateticket, name="updateticket"),
    path('addactivities/',views.addactivities,name="addactivities"),
    path('addactivities/', views.addactivities, name="addactivities"),
    path('saveactivities/', views.saveactivities, name="saveactivities"),
    path('displayactivities/', views.displayactivities, name="displayactivities"),
    path('editactivity/<int:dataid>', views.editactivity, name="editactivity"),
    path('updateactivity/<int:dataid>', views.updateactivity, name="updateactivity"),
    path('deleteactivity/<int:dataid>', views.deleteactivity, name="deleteactivity"),
    path('gallery/', views.gallery, name="gallery"),
    path('saveimages/', views.saveimages, name="saveimages"),
    path('displaygallery/', views.displaygallery, name="displaygallery"),
    path('deleteimage/<int:dataid>', views.deleteimage, name="deleteimage"),
    path('feedbackdisp/', views.feedbackdisp, name="feedbackdisp"),
    path('deletemsg/<int:dataid>', views.deletemsg, name="deletemsg"),
    path('familyreserved/', views.familyreserved, name="familyreserved"),
    path('deleteticket/<int:dataid>', views.deleteticket, name="deleteticket"),
    path('birthdayreserved/', views.birthdayreserved, name="birthdayreserved"),
    path('deletebdayticket/<int:dataid>', views.deletebdayticket, name="deletebdayticket"),
    path('schoolreserved/', views.schoolreserved, name="schoolreserved"),
    path('deleteschoolticket/<int:dataid>', views.deleteschoolticket, name="deleteschoolticket")
]
