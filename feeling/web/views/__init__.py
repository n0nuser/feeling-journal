from web.views.cue import CueListView, CueCreateView, CueUpdateView, CueDeleteView
from web.views.habit import HabitListView, HabitCreateView, HabitUpdateView, HabitDeleteView
from web.views.home import IndexView
from web.views.generate import generate_fake_data
from web.views.journal import JournalListView, JournalCreateView, JournalUpdateView, JournalDeleteView
from web.views.reward import RewardListView, RewardCreateView, RewardUpdateView, RewardDeleteView
from web.views.routine import RoutineListView, RoutineCreateView, RoutineUpdateView, RoutineDeleteView
from web.views.save import (
    SaveView,
    JournalCSV, JournalPDF,
    ThoughtCSV, ThoughtPDF,
    CueCSV, CuePDF,
    RoutineCSV, RoutinePDF,
    RewardCSV, RewardPDF,
    HabitCSV, HabitPDF,
)
from web.views.statistics import StatisticsView
from web.views.thought import ThoughtListView, ThoughtCreateView, ThoughtUpdateView, ThoughtDeleteView
