from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, MedicalHistory
from .forms import ProfileForm, MedicalHistoryForm
from datetime import datetime

def get_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    # Redirect if any required fields are missing
    if not profile.birthdate or not profile.address or profile.weight is None or profile.height is None or profile.exercise_level is None:
        return redirect('/user/profile/edit')
    
     # Parse birthdate string and calculate age
    birthdate_str = profile.birthdate  # Assuming birthdate is stored as 'dd/mm/yyyy'
    birthdate = datetime.strptime(birthdate_str, '%d/%m/%Y')
    today = datetime.today()
    
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    medical_histories = profile.medical_histories.all()
    
    return render(request, 'ProfilePage.html', {
        'profile': profile,
        'medical_histories': medical_histories,
        'age': age,
    })

@login_required
def edit_profile(request):
    # Get or create the profile for the logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Handle profile updates
        profile_form = ProfileForm(request.POST, instance=profile, user=request.user)  # Pass user to the form
        item_form = MedicalHistoryForm(request.POST)  # Initialize MedicalHistoryForm

        if 'update_profile' in request.POST:
            if profile_form.is_valid():
                # Save profile data if valid
                profile_form.save()
                return redirect('/user/profile/')  # Refresh to show updated profile
            else:
                item_form = MedicalHistoryForm(request.POST)  # Reset the item form if the profile form is invalid

        elif 'add_medical_history' in request.POST:
            if item_form.is_valid():
                # Save new medical history item
                MedicalHistory.objects.create(profile=profile, item=item_form.cleaned_data['item'])
                return redirect('/user/profile/edit')  # Refresh to show updated medical history
            else:
                # Handle errors for medical history
                pass  # Errors can be handled as needed

        elif 'delete_item' in request.POST:
            item_id = request.POST.get('item_id')
            if item_id:
                medical_history_item = get_object_or_404(MedicalHistory, id=item_id, profile=profile)
                medical_history_item.delete()
                return redirect('/user/profile/edit')  # Refresh after deletion

    # Render the edit profile page with forms
    medical_histories = profile.medical_histories.all()
    item_form = MedicalHistoryForm()

    return render(request, 'EditProfilePage.html', {
        'profile_form': ProfileForm(instance=profile, user=request.user),  # Pass user here as well
        'item_form': item_form,
        'medical_histories': medical_histories,
        'created': created,
        'profile': profile,
    })
