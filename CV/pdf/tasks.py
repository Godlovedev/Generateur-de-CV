from celery import shared_task
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string



@shared_task
def download_cv(id):
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

    #generer le pdf
    pdf = HTML(string=template).write_pdf()

    # envoyer le pdf a l'utilisatuer
    response = HttpResponse(pdf, content_type='application/pdf')
    response["Content-Disposition"] = "attachment; filename='MonCV.pdf'"