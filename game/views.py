from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.timezone import now
from .models import GameState

@api_view(['GET'])
def get_cards(request):
    state, _ = GameState.objects.get_or_create(id=1)
    return Response({
        "cards": state.cards,
        "timer_started_at": state.timer_started_at,
        "timer_stopped": state.timer_stopped,
    })

@api_view(['POST'])
def next_card(request):
    state, _ = GameState.objects.get_or_create(id=1)
    all_cards = ["Лимон", "Киви", "Апельсин", "Мандарин"]
    visible_count = len(state.cards)

    if visible_count < 4:
        state.cards.append(all_cards[visible_count])
        if visible_count == 0 and not state.timer_started_at:
            state.timer_started_at = now()
        state.save()

    return Response({"status": "ok"})

@api_view(['POST'])
def reset_game(request):
    state, _ = GameState.objects.get_or_create(id=1)
    state.cards = []
    state.timer_started_at = None
    state.timer_stopped = False
    state.save()
    return Response({"status": "reset"})

@api_view(['POST'])
def stop_timer(request):
    state, _ = GameState.objects.get_or_create(id=1)
    state.timer_stopped = True
    state.save()
    return Response({"status": "stopped"})