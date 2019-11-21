from django.shortcuts import redirect


def login_required(target_func):
    def wrapped(request, *args, **kwargs):
        email = request.session.get("customer_email")
        if email is None or not email:
            return redirect("/login")
        return target_func(request, *args, **kwargs)
    return wrapped
