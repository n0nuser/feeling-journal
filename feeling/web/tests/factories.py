import factory
from web.models import Journal, Thought, Cue, Routine, Reward, Habit


class JournalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Journal

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    ocurred_at = factory.Faker("date_time_this_month")
    number_of_times = factory.Faker("pyint")
    situation_emotion = factory.Faker("sentence")
    afterwards_feeling = factory.Faker("sentence")


class ThoughtFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Thought

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    created_at = factory.Faker("date_time_this_month")
    journal = factory.SubFactory(JournalFactory)
    thought = factory.Faker("sentence")


class CueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cue

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    trigger = factory.Faker("sentence")


class RoutineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Routine

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    response = factory.Faker("sentence")
    type = factory.Faker("random_element", elements=("M", "E", "P"))


class RewardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reward

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    reward = factory.Faker("sentence")


class HabitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Habit

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    ocurred_at = factory.Faker("date_time_this_month")
    number_of_times = factory.Faker("pyint")
    cue = factory.SubFactory(CueFactory)
    routine = factory.SubFactory(RoutineFactory)
    reward = factory.SubFactory(RewardFactory)
