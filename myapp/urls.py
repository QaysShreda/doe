from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index', views.index, name='index'),
    path('school/',views.school,name='school'),
    path('doe/',views.doe,name="doe"),
    path('register',views.register,name='register'),
    #DOE COMPUTER
    path('doe_computer/',views.doe_computer,name="doe_computer"),
    path('computer_form/', views.computer_form, name="computer_form"),
    path('<int:id>/computer_form/', views.computer_form, name="computer_update"),
    path('<int:id>/computer_delete/', views.computer_delete, name="computer_delete"),

    #DOE COPIER
    path('doe_copier/', views.doe_copier, name="doe_copier"),
    path('doe_copier_form/',views.doe_copier_form,name="doe_copier_form"),
    path('<int:id>/doe_copier_form/', views.doe_copier_form, name="doe_copier_form_update"),
    path('<int:id>/doe_copier_delete/', views.doe_copier_delete, name="doe_copier_delete"),

    #DOE PRINTER
    path('doe_printer/', views.doe_printer,name="doe_printer"),
    path('doe_printer_form/', views.doe_printer_form,name="doe_printer_form"),
    path('<int:id>/doe_printer_form/', views.doe_printer_form,name="doe_printer_update"),
    path('<int:id>/doe_printer_delete/',views.doe_printer_delete, name="doe_printer_delete"),

    # DOE PROJECTOR
    path('doe_projector/', views.doe_projector, name="doe_projector"),
    path('doe_projector_form/', views.doe_projector_form, name="doe_projector_form"),
    path('<int:id>/doe_projector_form/', views.doe_projector_form, name="doe_projector_update"),
    path('<int:id>/doe_projector_delete/', views.doe_projector_delete, name="doe_projector_delete"),

 # DOE NETWORK
    path('doe_network/',views.doe_network,name="doe_network"),
    #FIBER
    path('doe_fiber_form/',views.doe_fiber_form,name="doe_fiber_form"),
    path('<int:id>/doe_fiber_form/',views.doe_fiber_form,name="doe_fiber_update"),
    path('<int:id>/doe_fiber_delete/',views.doe_fiber_delete,name="doe_fiber_delete"),
    #IP
    path('doe_ip_form/', views.doe_ip_form, name="doe_ip_form"),
    path('<int:id>/doe_ip_form/', views.doe_ip_form, name="doe_ip_update"),
    path('<int:id>/doe_ip_delete/', views.doe_ip_delete, name="doe_ip_delete"),
    #wifi
    path('doe_wifi_form/', views.doe_wifi_form, name="doe_wifi_form"),
    path('<int:id>/doe_wifi_form/', views.doe_wifi_form, name="doe_wifi_update"),
    path('<int:id>/doe_wifi_delete/', views.doe_wifi_delete, name="doe_wifi_delete"),


# School

    path('school_info', views.school_info, name="school_info"),
    path('school_form', views.school_form, name='school_form'),
    path('<int:id>/school_form', views.school_form, name='school_update'),
    path('<int:id>/school_delete/', views.school_delete, name="school_delete"),

     # Lab
    path('school_lab',views.school_lab,name='school_lab'),
    path('school_lab_form',views.school_lab_form,name='school_lab_form'),
    path('<int:id>/school_lab_form',views.school_lab_form,name='school_lab_update'),
    path('<int:id>/school_lab_delete',views.school_lab_delete,name='school_lab_delete'),



    path('<int:lab>/school_computer_form',views.school_computer_form,name='school_computer_form'),
    path('<int:lab>/<int:id>/school_computer_form', views.school_computer_form, name='school_computer_update'),
    path('<int:id>/school_computer_delete', views.school_computer_delete, name='school_computer_delete'),
    path('<int:id>/school_lab_computers',views.school_lab_computers,name='school_lab_computers'),


]

urlpatterns += staticfiles_urlpatterns()