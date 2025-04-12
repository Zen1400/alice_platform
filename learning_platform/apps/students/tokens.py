from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):

        '''
        Generates a hash value for the user and timestamp.
        This is used to create a unique token for the user.
        The hash value is based on the user's primary key, timestamp,
        '''
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active) # is_active status (ensures token invalidates after activation)
        )

account_activation_token = AccountActivationTokenGenerator()