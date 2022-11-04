from django.urls import path
import web.views as views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    #
    path("statistics/", views.StatisticsView.as_view(), name="statistics"),
    #
    path("save/", views.SaveView.as_view(), name="save"),
    path("save/journal/csv/", views.JournalCSV, name="journal_csv"),
    path("save/journal/pdf/", views.JournalPDF, name="journal_pdf"),
    path("save/thought/csv/", views.ThoughtCSV, name="thought_csv"),
    path("save/thought/pdf/", views.ThoughtPDF, name="thought_pdf"),
    #
    path("journal/", views.JournalListView.as_view(), name="journal_list"),
    path("journal/add/", views.JournalCreateView.as_view(), name="journal_add"),
    path("journal/edit/<pk>", views.JournalUpdateView.as_view(), name="journal_edit"),
    path("journal/del/<pk>", views.JournalDeleteView.as_view(), name="journal_del"),
    # 
    path("thought/", views.ThoughtListView.as_view(), name="thought_list"),
    path("thought/add/", views.ThoughtCreateView.as_view(), name="thought_add"),
    path("thought/edit/<pk>", views.ThoughtUpdateView.as_view(), name="thought_edit"),
    path("thought/del/<pk>", views.ThoughtDeleteView.as_view(), name="thought_del"),
]
