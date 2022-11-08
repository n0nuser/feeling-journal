from django.urls import path
import web.views as views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    #
    path("statistics/", views.StatisticsView.as_view(), name="statistics"),
    #
    path("generate/", views.generate_fake_data, name="generate"),
    #
    path("save/", views.SaveView.as_view(), name="save"),
    path("save/journal/csv/", views.JournalCSV, name="journal_csv"),
    path("save/journal/pdf/", views.JournalPDF, name="journal_pdf"),
    path("save/thought/csv/", views.ThoughtCSV, name="thought_csv"),
    path("save/thought/pdf/", views.ThoughtPDF, name="thought_pdf"),
    path("save/cue/csv/", views.CueCSV, name="cue_csv"),
    path("save/cue/pdf/", views.CuePDF, name="cue_pdf"),
    path("save/routine/csv/", views.RoutineCSV, name="routine_csv"),
    path("save/routine/pdf/", views.RoutinePDF, name="routine_pdf"),
    path("save/reward/csv/", views.RewardCSV, name="reward_csv"),
    path("save/reward/pdf/", views.RewardPDF, name="reward_pdf"),
    path("save/habit/csv/", views.HabitCSV, name="habit_csv"),
    path("save/habit/pdf/", views.HabitPDF, name="habit_pdf"),
    #
    path("journal/", views.JournalListView.as_view(), name="journal_list"),
    path("journal/add/", views.JournalCreateView.as_view(), name="journal_create"),
    path("journal/edit/<pk>", views.JournalUpdateView.as_view(), name="journal_update"),
    path("journal/del/<pk>", views.JournalDeleteView.as_view(), name="journal_delete"),
    # 
    path("thought/", views.ThoughtListView.as_view(), name="thought_list"),
    path("thought/add/", views.ThoughtCreateView.as_view(), name="thought_create"),
    path("thought/edit/<pk>", views.ThoughtUpdateView.as_view(), name="thought_update"),
    path("thought/del/<pk>", views.ThoughtDeleteView.as_view(), name="thought_delete"),
    #
    path("habit/", views.HabitListView.as_view(), name="habit_list"),
    path("habit/add/", views.HabitCreateView.as_view(), name="habit_create"),
    path("habit/edit/<pk>", views.HabitUpdateView.as_view(), name="habit_update"),
    path("habit/del/<pk>", views.HabitDeleteView.as_view(), name="habit_delete"),
    #
    path("cue/", views.CueListView.as_view(), name="cue_list"),
    path("cue/add/", views.CueCreateView.as_view(), name="cue_create"),
    path("cue/edit/<pk>", views.CueUpdateView.as_view(), name="cue_update"),
    path("cue/del/<pk>", views.CueDeleteView.as_view(), name="cue_delete"),
    #
    path("routine/", views.RoutineListView.as_view(), name="routine_list"),
    path("routine/add/", views.RoutineCreateView.as_view(), name="routine_create"),
    path("routine/edit/<pk>", views.RoutineUpdateView.as_view(), name="routine_update"),
    path("routine/del/<pk>", views.RoutineDeleteView.as_view(), name="routinet_delete"),
    #
    path("reward/", views.RewardListView.as_view(), name="reward_list"),
    path("reward/add/", views.RewardCreateView.as_view(), name="reward_create"),
    path("reward/edit/<pk>", views.RewardUpdateView.as_view(), name="reward_update"),
    path("reward/del/<pk>", views.RewardDeleteView.as_view(), name="reward_delete"),
]
