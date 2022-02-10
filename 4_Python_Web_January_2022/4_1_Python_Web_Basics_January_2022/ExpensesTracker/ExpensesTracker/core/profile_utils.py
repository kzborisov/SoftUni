from ExpensesTracker.profiles.models import Profile
from ExpensesTracker.web.models import Expense


def get_profile():
    profile = Profile.objects.first()
    if profile:
        expenses = Expense.objects.all()
        profile.budget_left = profile.budget - sum(e.price for e in expenses)
    return profile
