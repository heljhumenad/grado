from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin

from grados.app.mixin.loginrequired import LoginRequiredMixins


class MessageMixins(LoginRequiredMixins, SuccessMessageMixin):
    success_message = _(
        "%(field)s is sucessfully %(messages)s"
    )

    @property
    def field_name(self):
        return NotImplemented
    
    @property
    def messages(self):
        return NotImplemented
    
    def get_success_message(self, cleaned_data, **kwargs):
        return self.success_message % dict(
            cleaned_data,
            field = self.object.field_name,
            messages = self.messages
        )