from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def superuser_required(user):
    return user.is_superuser

@user_passes_test(superuser_required)
def analise_view(request):
    return render(request, 'analise/flexmonster.html')