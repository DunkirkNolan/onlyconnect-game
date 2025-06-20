from django.urls import path
from . import views

urlpatterns = [
    path('cards/', views.get_cards),
    path('next-card/', views.next_card),
    path('reset-game/', views.reset_game),
    path('stop-timer/', views.stop_timer),  # ⬅️ новый путь
]