def staff_status(request):
    # This function returns a dictionary indicating whether the user is a staff member
    return {'is_staff': request.user.is_staff}
