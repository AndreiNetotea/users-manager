from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend


class EmailAuthenticationBackend(ModelBackend):
    """
    Authenticate using email
    """

    def authenticate(self, username=None,  password=None, **args):

        try:
            username = username.replace(' ','')
            q = Q(username__iexact=username) | Q(email__iexact=username)

            user = User.objects.get(q)
            if check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist as e:
            return None
        except:
            return None
