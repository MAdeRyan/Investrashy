from core.models import UserProfileInfo
from django.contrib.auth.models import User

def profile_picture(request):     
    if request.user.id:
        if request.user.username == 'admin':
            return {'profile_picture': 'profile_pics/profile.jpg'}        
        pic = UserProfileInfo.objects.get(user=request.user)
        return {'profile_picture': pic.profile_pic}
    return {'profile_picture': 'profile_pics/profile.jpg'}
    