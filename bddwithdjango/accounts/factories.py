import factory
from django.contrib.auth.hashers import make_password
from .models import Interest
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'Standard'
    last_name = 'user'
    email = factory.Sequence(lambda n: 'user.{}@test.text'.format(n))
    password = make_password('pass')

    @factory.post_generation
    def interests(self, create, extracted, **kwargs):
        """
        Where 'interests' are defined, add them to this user
        """
        if not create:
            return
        if extracted:
            for interest in extracted:
                self.interests.add(interest)


class InterestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Interest

    name = factory.Sequence(lambda n: 'interest{}'.format(n))
