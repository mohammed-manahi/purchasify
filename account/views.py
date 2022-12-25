from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import User
from account.forms import UserRegistrationForm, UserEditForm


@login_required
def dashboard(request):
    """
    Create user dashboard view
    :param request:
    :return dashboard:
    """
    user_name = request.user.username
    template = 'account/dashboard.html'
    context = {'user_name': user_name}
    return render(request, template, context)


def register(request):
    """
    Create registration and use password check defined in user registration form
    :param request:
    :return:
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # set password method handles password hashing
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'You have been registered successfully')
            template = 'account/register_done.html'
            context = {'new_user': new_user}
            return render(request, template, context)
        messages.error(request, 'Something went wrong. Try again')
        user_form = UserRegistrationForm()
        template = 'account/register.html'
        context = {'user_form': user_form}
        return render(request, template, context)
    else:
        user_form = UserRegistrationForm()
        template = 'account/register.html'
        context = {'user_form': user_form}
        return render(request, template, context)


@login_required
def edit(request):
    """
    Create uer edit view to edit user fields in user edit form and profile edit form
    :param request:
    :return:
    """
    if request.method == 'POST':
        # Get the instance since this view performs edit
        user_form = UserEditForm(data=request.POST, instance=request.user)
        # Define files attribute because the profile fields contain photo upload
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'An Error occurred while updating your profile')

    else:
        user_form = UserEditForm(instance=request.user)
    template = 'account/edit.html'
    context = {'user_form': user_form}
    return render(request, template, context)
