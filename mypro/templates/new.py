def signup_user(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        us = request.POST['n']
        e = request.POST['e']
        p = request.POST['p']
        pic = request.FILES['i']

        user = User.objects.create_user(first_name=fn, last_name=ln, username=us, email=e, password=p, is_active=False)
        try:
            user.save()
            ex = Extra(pid=user, img=pic)
            ex.save()

            # Generate activation link
            email_subject = "Registration"
            email_body = f"Thank you for registering on our website. Click the link below to activate your account:"
            email = EmailMessage(
                email_subject,
                email_body,
                "anumsaleem698@gmail.com",
                [e]
            )
            email.send()
            return redirect('login')
        except Exception as error:
            return HttpResponse(f"Error: {error}")

    return render(request, 'signup.html')