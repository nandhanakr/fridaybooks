from django.urls import path
from frontend import views

urlpatterns =[
    path('homepage/', views.homepage, name="homepage"),
    path('product_page/<cname>/', views.product_page, name="product_page"),
    path('singleproduct/<int:proid>/',views.singleproduct, name="singleproduct"),

    path('contactpage/', views.contactpage, name="contactpage"),
    path('contactsave/', views.contactsave, name="contactsave"),
    path('blogpage/', views.blogpage, name="blogpage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('termspage/', views.termspage, name="termspage"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('cartdelete/<p_id>',views.cartdelete, name="cartdelete"),
    path('cart_save/', views.cart_save, name="cart_save"),
    path('checkoutpage/',views.checkoutpage, name="checkoutpage"),
    path('save_checkout/',views.save_checkout, name="save_checkout"),
    path('success/',views.success, name="success"),

    path('userlogin/', views.userlogin, name="userlogin"),
    path('signin_save/', views.signin_save, name="signin_save"),
    path('signup_page/', views.signup_page, name="signup_page"),
    path('Userlogout/', views.Userlogout, name="Userlogout"),
    ]