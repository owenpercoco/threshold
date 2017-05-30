from .models import User_Group

def data_for_templates(request):
    # Create fixed data structures to pass to template
    # very simple, gives you user data and if user is logged in
    #added: gives you what groups you are in
    if request.user.is_authenticated():
        group = request.user.user_groups.all()
        user_data = request.user
        logged_in = True
        return {'USER_DATA': user_data, 'GROUPS': group, 'LOGGED_IN': logged_in}
    else:
        logged_in = False
        return {'LOGGED_IN': logged_in}

