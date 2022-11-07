from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from faker import Factory

from web.tests.factories import JournalFactory, HabitFactory, CueFactory, RoutineFactory, RewardFactory

User = get_user_model()
faker = Factory.create()


class JournalViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=faker.user_name(), password=faker.password())
        self.client.login(username=self.user.username, password=faker.password())
        self.journal = JournalFactory.create(user=self.user)

    def test_journal_list_view(self):
        response = self.client.get(reverse("web:journal_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "web/journal_list.html")

    def test_journal_create_view(self):
        response = self.client.get(reverse("web:journal_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/add.html")

    def test_journal_update_view(self):
        response = self.client.get(reverse("web:journal_update", kwargs={"pk": self.journal.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/update.html")

    def test_journal_delete_view(self):
        response = self.client.get(reverse("web:journal_delete", kwargs={"pk": self.journal.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/delete.html")


class HabitViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=faker.user_name(), password=faker.password())
        self.client.login(username=self.user.username, password=faker.password())
        self.habit = HabitFactory.create(user=self.user)

    def test_habit_list_view(self):
        response = self.client.get(reverse("web:habit_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "web/habit_list.html")

    def test_habit_create_view(self):
        response = self.client.get(reverse("web:habit_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/add.html")

    def test_habit_update_view(self):
        response = self.client.get(reverse("web:habit_update", kwargs={"pk": self.habit.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/update.html")

    def test_habit_delete_view(self):
        response = self.client.get(reverse("web:habit_delete", kwargs={"pk": self.habit.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/delete.html")


class CueViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=faker.user_name(), password=faker.password())
        self.client.login(username=self.user.username, password=faker.password())
        self.cue = CueFactory.create(user=self.user)

    def test_cue_list_view(self):
        response = self.client.get(reverse("web:cue_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "web/cue_list.html")

    def test_cue_create_view(self):
        response = self.client.get(reverse("web:cue_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/add.html")

    def test_cue_update_view(self):
        response = self.client.get(reverse("web:cue_update", kwargs={"pk": self.cue.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/update.html")

    def test_cue_delete_view(self):
        response = self.client.get(reverse("web:cue_delete", kwargs={"pk": self.cue.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/delete.html")


class RoutineViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=faker.user_name(), password=faker.password())
        self.client.login(username=self.user.username, password=faker.password())
        self.routine = RoutineFactory.create(user=self.user)

    def test_routine_list_view(self):
        response = self.client.get(reverse("web:routine_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "web/routine_list.html")

    def test_routine_create_view(self):
        response = self.client.get(reverse("web:routine_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/add.html")

    def test_routine_update_view(self):
        response = self.client.get(reverse("web:routine_update", kwargs={"pk": self.routine.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/update.html")

    def test_routine_delete_view(self):
        response = self.client.get(reverse("web:routine_delete", kwargs={"pk": self.routine.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/delete.html")


class RewardViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=faker.user_name(), password=faker.password())
        self.client.login(username=self.user.username, password=faker.password())
        self.reward = RewardFactory.create(user=self.user)

    def test_reward_list_view(self):
        response = self.client.get(reverse("web:reward_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "web/reward_list.html")

    def test_reward_create_view(self):
        response = self.client.get(reverse("web:reward_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/add.html")

    def test_reward_update_view(self):
        response = self.client.get(reverse("web:reward_update", kwargs={"pk": self.reward.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/update.html")

    def test_reward_delete_view(self):
        response = self.client.get(reverse("web:reward_delete", kwargs={"pk": self.reward.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/delete.html")
