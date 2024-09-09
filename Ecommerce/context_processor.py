def staff_status(request):
    return {'is_staff': request.user.is_staff}


