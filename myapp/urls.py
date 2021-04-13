from django.urls import path
from myapp import views
urlpatterns =[
    path('',views.view1,name='view1'),
    path('view2/<email>',views.view2,name='view2'),
    path('view3/<name>',views.view3,name='view3'),
]