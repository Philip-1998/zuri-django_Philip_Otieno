from django.urls import path
from . import views


app_name = "polls"
urlpatterns = [
    path('',views.Index.as_view(),name="index"),
    path('create_question/',views.Question_create.as_view(),name='create'),
    path('<int:pk>/update_question/',views.Question_update.as_view(),name="update"),
    path('<int:pk>/question_delete',views.Question_delete.as_view(),name="delete"),
    path('login_form/',views.formview,name="login"),
    path('choice_form/',views.choice_form,name="choice"),
    path('<int:pk>/create_new_choice',views.create_new_choice,name="create_new_choice"),
    path('<int:pk>/detail/',views.Question_detail.as_view(),name="detail"),
    path("<int:pk>/results/",views.Result_detail.as_view(),name="results"),
    path('<int:question_id>/vote/',views.vote,name="vote")
]