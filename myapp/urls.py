from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[
    path('', views.index, name='index'),
    path('school/',views.school,name='school'),
    path('doe/',views.doe,name="doe"),

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
    path('<int:id>/doe_projector_delete/', views.doe_projector_delete, name="doe_projector_delete")




]

urlpatterns += staticfiles_urlpatterns()