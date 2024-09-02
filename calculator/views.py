from django.shortcuts import render
from .models import CalculationResult
from .forms import MathEquationForm

def solve_equation(request):
    result = None
    if request.method == 'POST':
        form = MathEquationForm(request.POST)
        if form.is_valid():
            equation = form.cleaned_data['input']
            try:
                result = eval(equation)
                CalculationResult.objects.create(
                    input=equation,
                    result=str(result),
                )
            except Exception as e:
                result = f"Error: {e}"
    else:
        form = MathEquationForm()

    return render(
        request,
        'calc.html',
        {'form': form, 'result': result}
    )