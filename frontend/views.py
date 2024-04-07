from django.shortcuts import render, redirect, get_object_or_404
from frontend.models import ContactDB, RegistrationDB, CartDB, CheckoutDB
from backend.models import ProductDB, CategoryDB
from django.contrib import messages
from django.http import HttpResponseRedirect
from instamojo_wrapper import Instamojo
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
api = Instamojo(api_key="test_827ee1f7fd62948bb6956534dae", auth_token="test_c2aae28366a6a2f4845c198cb63", endpoint='https://test.instamojo.com/api/1.1/');

def homepage(request):
    pro = ProductDB.objects.all()
    cat = CategoryDB.objects.all()
    return render(request, "home.html", {'pro':pro, 'cat':cat})

def product_page(request, cname):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.filter(CName = cname)
    return render(request, "Product.html",  {'cat':cat, 'pro':pro})

def singleproduct(request, proid):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.get(id=proid)
    return render(request, "SingleProduct.html", {'pro': pro, 'cat': cat})

def contactpage(request):
    cat = CategoryDB.objects.all()
    return render(request, "Contact.html", {'cat': cat})

def contactsave(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('mes')
        obj = ContactDB(Name=a, Email=b, Message=c)
        obj.save()
        messages.success(request, "Sended Successfully !")
        return redirect(contactpage)

def blogpage(request):
    cat = CategoryDB.objects.all()
    return render(request, "Blog.html", {'cat': cat})

def aboutpage(request):
    cat = CategoryDB.objects.all()
    return render(request, "About.html", {'cat': cat})

def termspage(request):
    cat = CategoryDB.objects.all()
    return render(request, "Terms.html", {'cat': cat})
#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  -   -   -   -   -   -   -   -   -   -    -   -   -   -   -
def cart_save(request):
    if request.method == "POST":
        a = request.POST.get('uname')
        b = request.POST.get('pname')
        c = request.POST.get('qty')
        d = request.POST.get('price')
        e = request.POST.get('TotalPrice')
        obj = CartDB(UserName=a, Pname=b, Quantity=c, Price=d, TotalPrice=e)
        obj.save()
        messages.success(request, "Added To Cart")
        return redirect(cartpage)

def cartpage(request):
    data =CartDB.objects.filter(UserName=request.session['Name'])
    total_price =0
    for i in data:
        total_price = total_price+i.TotalPrice
    cat = CategoryDB.objects.all()
    return render(request, "Cart.html", {'data':data, 'total_price': total_price, 'cat': cat})

def cartdelete(request, p_id):
    cart = CartDB.objects.filter(id=p_id)
    cart.delete()
    messages.error(request, "Delete!")
    return redirect(cartpage)

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  -   -   -   -   -   -   -   -   -   -    -   -   -   -   -

def checkoutpage(request):
    data = CartDB.objects.filter(UserName=request.session['Name'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    cat = CategoryDB.objects.all()
    return render(request, "Checkout.html",  {'data':data, 'total_price': total_price, 'cat': cat})
def save_checkout(req):
    if req.method == "POST":
        a = req.POST.get('fname')
        b = req.POST.get('lname')
        c = req.POST.get('coun')
        d = req.POST.get('address')
        e = req.POST.get('city')
        f = req.POST.get('pin')
        g = req.POST.get('phone')
        h = req.POST.get('email')
        i = req.POST.get('amount')
        response = api.payment_request_create(
            amount=i,
            purpose="shopping",
            send_email=True,
            email=h,
            redirect_url="http://127.0.0.1:9000/Frontend/success/"
        )
        print(response)
        payment_url = response['payment_request']['longurl']
        payment_id = response['payment_request']['id']
        obj = CheckoutDB(FirstName=a, LastName=b, Country=c, Address=d, City=e, Pincode=f, Phone=g, Email=h, Amount=i, PaymentID=payment_id, Orderstatus='pending')
        obj.save()
        # print the long URL of the payment request.
        print(payment_url)
        if payment_url:
            send_mail('Payment request from Friday Books',
                      f"Dear {a}, \nWe would like to kindly request a payment of ₹{i} from you for the shopping with FridayBooks. ",
                      'nandhanakr303 @ gmail.com', ['nandhanakr303 @ gmail.com'], fail_silently=False)
            return HttpResponseRedirect(payment_url)
            # messages.success(req, "Saved checkout successfully")
        return redirect(homepage)


def success(request):
    try:
        # Get the PaymentID and payment_status from the request
        payment_id = request.GET.get("payment_request_id")
        payment_status = request.GET.get("payment_status")

        # Get the CheckoutDB object based on the PaymentID
        checkout_instance = get_object_or_404(CheckoutDB, PaymentID=payment_id)

        # Update the Orderstatus field
        checkout_instance.Orderstatus = payment_status
        checkout_instance.save()

        # Render a success template indicating the update was successful
        return render(request, 'Success.html')

    except Exception as e:
        # Render an error template if an exception occurs
        return render(request, 'Success.html')

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  -   -   -   -   -   -   -   -   -   -    -   -   -   -   -
def userlogin(request):
    return render(request, "Userlogin.html")

def signin_save(request):
    if request.method == "POST":
        a = request.POST.get('username')
        b = request.POST.get('email')
        c = request.POST.get('password')
        obj = RegistrationDB(Name=a, Email=b, Password=c)
        obj.save()
        return redirect(userlogin)

def signup_page(request):
    if request.method == "POST":
        nm = request.POST.get('name')
        pwd = request.POST.get('password')
        if RegistrationDB.objects.filter(Name=nm, Password=pwd).exists():
            request.session['Name']=nm
            request.session['Password']=pwd
            return redirect(homepage)
        else:
            return redirect(userlogin)
    else:
        return redirect(userlogin)

def Userlogout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(userlogin)
#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  -   -   -   -   -   -   -   -   -   -    -   -   -   -   -
