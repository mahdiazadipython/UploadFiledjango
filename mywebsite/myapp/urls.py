from django.urls import path


from.import views


urlpatterns = [
    path('',views.index,name= "index"),
    path("addcard/",views.addcard,name="card"),
    path("learnpython/",views.learnpython,name="learnpython"),
    path("article/",views.article,name = "article"),
]
