from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *

from random import randint

# Create your views here
def Indexpage(request):
    return render(request,"app/index.html")
def loginpage(request):
    return render(request,"app/login.html")
def homepage(request):
    return render(request,"app/homepage.html")
def ShowPage(request):
    return render(request,"app/showdata.html")
def Showdetail(request):
    all_doctor=Doctor.objects.all()
    return render(request, "app/showdata.html",{'all_doctor':all_doctor})
#def Showdetail2(request):
    #all_patient=Patient.objects.all()
   # return render(request, "app/showdata.html",{'all_patient':all_patient})


def RegisterUser(request):
    try:
        if  request.POST['role'] == 'doctor':
            firstname= request.POST['firstname']
            lastname= request.POST['lastname']
            #qualification= request.POST['qn']
            speciality= request.POST['speciality']
            mobile= str(request.POST['phone'])  
            #clinic= request.POST['clinic']
            #address= request.POST['address']
            city=request.POST['city']
            #state=request.POST['state']
            gender=request.POST['gender']
            birthdate= request.POST['birthdate']
            role = request.POST['role']
            password = request.POST['password']
            #confirmpassword = request.POST['confirmpassword']
            email = request.POST['email']
            image=request.FILES['image']
            
 
            
            
            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request, 'app/index.html', {})
            else:
                otp=randint(100000,999999)
                newuser=User.objects.create(
                    email=email,password=password,role=role,otp=otp)
                newdoctor=Doctor.objects.create(user_id=newuser,firstname=firstname,lastname=lastname,
                                                speciality=speciality,gender=gender,
                                                city=city,mobile=mobile,birthdate=birthdate,profile_pic=image)
                return HttpResponseRedirect(reverse("show"))
                
    
        else:
            
            firstname= request.POST['firstname']
            lastname= request.POST['lastname']
            #qualification= request.POST['qn']
            #speciality= request.POST['speciality']
            mobile= str(request.POST['phone'])  
            #clinic= request.POST['clinic']
            #address= request.POST['address']
            city=request.POST['city']
            #state=request.POST['state']
            gender=request.POST['gender']
            birthdate= request.POST['birthdate']
            role = request.POST['role']
            password = request.POST['password']
            #confirmpassword = request.POST['confirmpassword']
            email = request.POST['email']
            #image2=request.FILES['image2']

 
            
            
            

            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request, 'app/index.html', {})
            else:
                
                otp=randint(100000,999999)
                newuser=User.objects.create(
                            email=email,password=password,role=role,otp=otp)
                newdoctor=Patient.objects.create(user_id=newuser,firstname=firstname,lastname=lastname,
                                                gender=gender,#confirmpassword=confirmpassword,
                                                city=city,mobile=mobile,birthdate=birthdate,#pic2=image2)
               return render(request,"app/sucess.html", {})
                #return HttpResponseRedirect(reverse("show"))

                
    

    
    except User.DoesNotExist:
        return render(request, 'app/index.html',{})


def LoginUser(request):
    if request.POST['role']=="doctor":
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email)
        print(user)
        if user[0]:
                if user[0].password==password and user[0].role=='doctor':
                    doctor=Doctor.objects.filter(user_id=user[0])
                    request.session['email']=user[0].email
                    request.session['firstname']=doctor[0].firstname
    
                    request.session['lastname']=doctor[0].lastname
                    request.session['role']=user[0].role
                    request.session['id']=user[0].id

                    return HttpResponseRedirect(reverse("a"))
                else:
                    message = "Your password is incorrect or user doesn't exist'"
                    return render(request, 'app/login.html', {})
        else:
                message="user doesn't exist"
                return render(request, 'app/login.html', {})
    else:
            print("Patient coming soon")

def homepage(request):
        if 'email' in request.session and 'role' in request.session:
            if request.session['role']=='doctor':
                all_doctor=Doctor.objects.all()
                all_patient=Patient.objects.all()
                return render(request,"app/homepage.html",{'all_doctor':all_doctor,'all_patient':all_patient})
            else:
                all_doctors=Doctor.objects.all()
                return render(request, 'app/homepage.html',{'all_doctors':all_doctors})
        else:
            return HttpResponseRedirect(reverse('home'))
