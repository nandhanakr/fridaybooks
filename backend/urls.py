from django.urls import path
from backend import views

urlpatterns=[
    path('indexpage/', views.indexpage, name="indexpage"),

    path('addcategory/', views.addcategory, name="addcategory"),
    path('category_save/', views.category_save, name="category_save"),
    path('category_details/', views.category_details, name="category_details"),
    path('catedit/<int:c_id>/', views.catedit, name="catedit"),
    path('cat_update/<int:c_id>/', views.cat_update, name="cat_update"),
    path('cat_delete/<int:c_id>/', views.cat_delete, name="cat_delete"),

    path('addproduct/', views.addproduct, name="addproduct"),
    path('product_save/', views.product_save, name="product_save"),
    path('product_details/', views.product_details, name="product_details"),
    path('proedit/<int:p_id>/', views.proedit, name="proedit"),
    path('pro_update/<int:p_id>/', views.pro_update, name="pro_update"),
    path('pro_delete/<int:p_id>/', views.pro_delete, name="pro_delete"),

    path('adminloginpage/',views.adminloginpage, name="adminloginpage"),
    path('admin_login/',views.admin_login, name="admin_login"),
    path('admin_logout/',views.admin_logout, name="admin_logout"),

    ]