from django.contrib.auth import get_user_model


class EmailBackend(object):

    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if UserModel is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(
                email=username
            ).order('id').first()
        except UserModel.DoesNotExist:
            return "No existe Usuario %s" % self.username

        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
