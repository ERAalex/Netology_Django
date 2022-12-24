from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return render(request, 'calculator/index.html')


def dish_show(request, name):
    say_total_person = 'Рецепт блюда на 1 человека'

    if name == 'omlet':
        context = {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    }
    elif name == 'pasta':
        context = {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    }
    elif name == 'buter':
        context = {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }

    return render(request, 'calculator/index.html', {'recipe':context, 'total_p':say_total_person})



def dish_show_total(request, name, servings):
    say_total_person = f'Рецепт блюда на {servings} чел.'

    if name == 'omlet':
        context = {
        'яйца, шт': 2*int(servings),
        'молоко, л': 0.1*int(servings),
        'соль, ч.л.': 0.5*int(servings),
    }
    elif name == 'pasta':
        context = {
        'макароны, г': 0.3*int(servings),
        'сыр, г': 0.05*int(servings),
    }
    elif name == 'buter':
        context = {
        'хлеб, ломтик': 1*int(servings),
        'колбаса, ломтик': 1*int(servings),
        'сыр, ломтик': 1*int(servings),
        'помидор, ломтик': 1*int(servings),
    }

    return render(request, 'calculator/index.html', {'recipe':context, 'total_p':say_total_person})


