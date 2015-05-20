from django.views.generic import ListView, DetailView
from .models import Link, UserProfile
from django.contrib.auth import get_user_model

class LinkListView(ListView):
	model = Link
	queryset = Link.with_votes.all()
	paginate_by = 5

class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user