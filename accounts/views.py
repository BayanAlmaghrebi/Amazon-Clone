from django.shortcuts import render , redirect
from .models import Profile
from .forms import SignupForm
from django.core.mail import send_mail

def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']


            user = form.save(commit=False)
            user.is_active = False
            form.save()

            profile = Profile.objects.get(user__username=username) 


            send_mail(
                "Activate Your Account",
                f" Welcome {username} \nUse this code {profile.code} to activate your account\nMystroTeam",
                "bayanalmaghrebi@gmail.com", #send from
                [email], #send to
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')

    else:
        form = SignupForm()

    return render(request,'signup.html',{'form':form})
    

def activated(request,username):
    pass 
