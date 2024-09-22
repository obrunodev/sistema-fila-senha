from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

class UserIsOwnerMixin:
    owner_field = 'user'
    redirect_url = reverse_lazy('tasks:list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if getattr(obj, self.owner_field) != request.user:
            messages.error(request, 'You do not have permission to access.')
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
