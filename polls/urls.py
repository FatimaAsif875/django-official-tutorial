from django.urls import path

from . import views
app_name="polls"
urlpatterns = [
    path("", views.index, name="index"),

    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),    
    path("<int:question_id>/choice/", views.choice, name="choice"),
    path("<int:question_id>/newchoice/", views.newchoice, name="newchoice"),
    path("<int:question_id>/reset/", views.resetVote, name="reset"), 
    path("new/", views.newQs, name="new"),    
   
    
   

]