from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

from grados.app.mixin.loginrequired import LoginRequiredMixins


class MessageMixins(LoginRequiredMixins, SuccessMessageMixin):
    success_message = _(
        "Your data is sucessfully %(messages)s"
    )

    @property
    def messages(self):
        return NotImplemented
    
    def get_success_message(self, cleaned_data, **kwargs):
        return self.success_message % dict(
            cleaned_data,
            messages = self.messages
        )
