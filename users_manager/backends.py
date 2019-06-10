from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend


class EmailAuthenticationBackend(ModelBackend):
    """
    Authenticate using email
    """

    def authenticate(self, username=None,  password=None, **args):
        print('test')
        try:
            username = username.replace(' ','')
            q = Q(username__iexact=username) | Q(email__iexact=username)

            user = User.objects.get(q)
            print(user)
            if check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist as e:
            raise e
            return None
        except Exception as es:
            raise es
            return None
