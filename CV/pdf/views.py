from django.shortcuts import render, redirect
from pdf.models import Profile
import weasyprint
from django.template.loader import render_to_string
from django.http import HttpResponse
import datetime

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

        return redirect("verification")

    return render(request, "pdf/form.html")

def verification(request):
    profile = Profile.objects.latest("id")
    return render(request, "pdf/verification.html", {"profile":profile})

def generate(request, id):
    profile = Profile.objects.get(id=id)
    context = {
        "name":profile.name,
        "email":profile.email,
        "phone":profile.phone,
        "address":profile.address,
        "competance":profile.competance,
        "langue":profile.langue,
        "interet":profile.interet,
        "objectif":profile.objectif,
        "experience":profile.experience,
        "education":profile.education,
        "projet":profile.projet,
    }

    template = render_to_string("pdf/generator.html", context)

    pdf = weasyprint.HTML(string=template).write_pdf()

    #retourner le pdf telechargé
    response = HttpResponse(pdf, content_type='application/pdf')
    response["Content-Disposition"] = "attachment; filename='CV.pdf'"

    return response