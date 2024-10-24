from django.shortcuts import redirect

def role_required(group_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home_page')  # Replace with your access denied URL name
        return wrapper
    return decorator
