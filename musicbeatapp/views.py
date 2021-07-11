from django.shortcuts import render,HttpResponse,redirect
from musicbeatapp.models import Song,Carousel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
        song = Song.objects.all()
        return render(request, 'index.html' , {'song':song})
        

def errorthis(request):
        return render(request, 'errorthis.html')



def songs(request):
        song = Song.objects.all()
        return render(request, 'musicbeatapp/songs.html', {'song':song})

def songpost(request,id):
        song  = Song.objects.filter(song_id = id).first()
        return render(request, 'musicbeatapp/songpost.html', {'song':song})

def demo(request):
        obj = Carousel.objects.all()
        context ={
                'obj': obj,
        }
        return render(request,'musicbeatapp/demo.html', context)




        # return render(request,"musicbeatapp/login.html")
        return HttpResponse('login')

def signup(request):
        if request.method=='POST':
                first_name=request.POST['firstname']
                last_name=request.POST['lastname']
                username=request.POST['username']
                password1=request.POST['pass1']
                password2=request.POST['pass2']
                email=request.POST['email']
                if password1==password2:
                        if User.objects.filter(email=email).exists():
                                messages.info(request,'Email Taken')
                                return redirect('/')
                        elif User.objects.filter(username=username).exists():
                                messages.info(request,'Username Taken')
                                return redirect('/')
                        else:    
                                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                                user.save()
                                print('user created')
                                return redirect('/')
                else:
                        messages.info(request,"Password don't match!")
                        return redirect('/musicbeatapp/signup')
        else:
                return render(request,"musicbeatapp/signup.html")


def login(request):
        if request.method=='POST':
                uname=request.POST['uname']
                password1=request.POST['password1']
                # return redirect('/')
                from django.contrib.auth import authenticate, login, logout
                from django.contrib import messages
                # Authenticating user

                user = authenticate(username = uname, password = password1)
                if user is not None:
                        login(request , user)
                        # messages.success(request, "Sucessfully logged in" )
                        return redirect('/')
                else:
                        return redirect('/musicbeatapp/errorthis')
        else:
                return HttpResponse('404-Not found')

def handleLogout(request):
        logout(request)
        messages.success(request,"sucessfully logged out")
        return redirect('/')


def search(request):
        return render(request, 'search.html')