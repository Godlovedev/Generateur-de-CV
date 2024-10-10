from django.shortcuts import render
from pdf.models import Profile

# Create your views here.
def index(request):
    return render(request, "pdf/resume.html")

def formulaire(request):
    if request.method == "POST":
        name =request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("telephone")
        address = request.POST.get("address")
        competence = request.POST.get("competence")
        langue = request.POST.get("langue")
        interet = request.POST.get("interet")
        objectif = request.POST.get("objectif")
        experience = request.POST.get("experience")
        education = request.POST.get("education")
        projet = request.POST.get("projet")

        # Creation du profile en base de données
        profile = Profile.objects.create(name=name, email=email, phone=phone, address=address, competance=competence, langue=langue, interet=interet, objectif=objectif, experience=experience, education=education, projet=projet)
        profile.save()

    return render(request, "pdf/form.html")