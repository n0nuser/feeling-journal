from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from web.tests.factories import JournalFactory, ThoughtFactory, HabitFactory, CueFactory, RoutineFactory, RewardFactory

@login_required
def generate_fake_data(request):
    for _ in range(10):
        JournalFactory.create(user=request.user)
        ThoughtFactory.create(user=request.user)
        HabitFactory.create(user=request.user)
        CueFactory.create(user=request.user)
        RoutineFactory.create(user=request.user)
        RewardFactory.create(user=request.user)

    return HttpResponseRedirect(reverse_lazy("journal_list"))
