from django.shortcuts import render


def cart_summary(request):
    return render(request, 'summary.html')


def cart_add(request):
    return render(request, 'add.html')


def cart_remove(request):
    return render(request, 'remove.html')


def cart_update(request):
    return render(request, 'update.html')
