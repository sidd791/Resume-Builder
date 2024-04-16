from django.shortcuts import render, redirect
from resumeApp.models import Profile

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        ph_num = request.POST.get("ph_num", "")
        education = request.POST.get("education", "")
        degree = request.POST.get("degree", "")
        skills = request.POST.get("skills", "")
        experience = request.POST.get("experience", "")
        hobbies = request.POST.get("hobbies", "")
        
        profile = Profile(name = name, email = email, ph_num = ph_num, education = education, degree = degree, skills = skills, experience = experience, hobbies = hobbies)
        profile.save()  
        return redirect('resumeApp:resume', id=profile.id)
    return render(request, 'cv/accept.html')

def resume(request, id):
    profile = Profile.objects.get(pk = id)
    return render(request, 'cv/resume.html', {'profile':profile})



