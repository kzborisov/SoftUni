from library.profiles.models import Profile


def get_profile():
    profile = Profile.objects.all().first()
    if profile:
        return profile
