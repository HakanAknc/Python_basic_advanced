from django.http import HttpResponse

def merhaba_dunya(request):
    return HttpResponse("Merhaba, Dünya!")