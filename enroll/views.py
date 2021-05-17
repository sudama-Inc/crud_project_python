from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .forms import StudentRegistration
from .models import User_table
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User, auth





# Create your views here.

# Show table for Admin Page
def add_show(request):
    stud = User_table.objects.all()
    return render(request, 'enroll/addandshow.html', {'stu':stud})

# Update / Edit data for Admin page 
def update_data(request, id):
    if request.method == 'POST':
        pi = User_table.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User_table.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form':fm, 'payment_collection_id': id})



# Admin Delete Record
def delete_data(request, id):
    if request.method == 'POST':
        pi = User_table.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home')
    else:
        return HttpResponse("jnka")


# Add Data in Admin Page
def add_record(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            brd = fm.cleaned_data['brand']
            inva = fm.cleaned_data['invamt']
            invd = fm.cleaned_data['invdate']
            clta = fm.cleaned_data['cltnamt']
            cltd = fm.cleaned_data['cltndate']
            cust = fm.cleaned_data['customer']
            custc = fm.cleaned_data['customercode']
            coll = fm.cleaned_data['collectedby']
            paym = fm.cleaned_data['paymentmode']
            chq = fm.cleaned_data['cheque']
            bk = fm.cleaned_data['bank']
            dd = fm.cleaned_data['duedate']
            sss = fm.cleaned_data['status']
            dopd = fm.cleaned_data['doptdate']
            utrn = fm.cleaned_data['utrno']
            bksc = fm.cleaned_data['bksc']
            reg = User_table(brand=brd, invamt=inva, invdate=invd, cltnamt=clta, cltndate=cltd, customer=cust, customercode=custc, collectedby=coll, paymentmode=paym, cheque=chq, bank=bk, duedate=dd, status=sss, doptdate=dopd, utrno=utrn, bksc=bksc)
            reg.save()
            return HttpResponseRedirect('/home')
        else:
            return HttpResponse(fm.errors, 'sdfsdfs')      
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/add.html', {'form': fm})



# Show how many User are created by Admin in admin page
def totaluserinadmin(request):
    stud = User.objects.all()
    return render(request, 'enroll/totaluserinadmin.html', {'stu':stud})




################
# Common function for login & Authentication 
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','Admin')
        password = request.POST.get('password','Admin@123')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/userhome")
        elif username == "Admin" and password == "Admin@123":
            auth.login(request, user)
            return redirect("/home")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/loggedin')

    else:
        return render(request, 'enroll/loggedin.html')



# Create a new User by Admin
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                print('user created')
                return redirect('/home')
        else:
            messages.info(request, 'OOps!! your Password not matching')
            return redirect('/register')
        return redirect('/home')
    else:
        return render(request, 'enroll/base.html')
    

# Logout for common to all
def logout(request):
    auth.logout(request)
    return redirect('/loggedin')


# Show the login Page
def login_request(request):
    return render(request, "enroll/loggedin.html")



# User Data Function which shows table fo User
def show_userdata(request):
    stud = User_table.objects.all()
    return render(request, "enroll/showuserdata.html", {'stu':stud})    



# Function to Added Data in database By User 
def add_userdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            brd = fm.cleaned_data['brand']
            inva = fm.cleaned_data['invamt']
            invd = fm.cleaned_data['invdate']
            clta = fm.cleaned_data['cltnamt']
            cltd = fm.cleaned_data['cltndate']
            cust = fm.cleaned_data['customer']
            custc = fm.cleaned_data['customercode']
            coll = fm.cleaned_data['collectedby']
            paym = fm.cleaned_data['paymentmode']
            chq = fm.cleaned_data['cheque']
            bk = fm.cleaned_data['bank']
            dd = fm.cleaned_data['duedate']
            sss = fm.cleaned_data['status']
            dopd = fm.cleaned_data['doptdate']
            utrn = fm.cleaned_data['utrno']
            bksc = fm.cleaned_data['bankcharges']
            reg = User_table(brand=brd, invamt=inva, invdate=invd, cltnamt=clta, cltndate=cltd, customer=cust, customercode=custc, collectedby=coll, paymentmode=paym, cheque=chq, bank=bk, duedate=dd, status=sss, doptdate=dopd, utrno=utrn, bankcharges=bksc)
            reg.save()
            return HttpResponseRedirect('/userhome')    
            
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/adduserdata.html',{'form':fm})





# Function for Updated Data By User 
def update_userdata(request, id):
    if request.method == 'POST':
        pi = User_table.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            return render(request, 'enroll/updateuserdata.html', {'error':"New Record Added Successfully!!!"})
    else:
        pi = User_table.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updateuserdata.html', {'form':fm, 'user_collection_id': id})


# This Function will Delete Record from the user side
def delete_userdata(request, id):
    if request.method == 'POST':
        pi = User_table.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/userhome')
        