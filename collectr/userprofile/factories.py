import factory

from .models import UserProfile
import source.factories as source_factories


class UserProfileFactory(factory.DjangoModelFactory):
    FACTORY_FOR = UserProfile

    user = factory.SubFactory(source_factories.UserFactory)
