from django.shortcuts import render

# Create your views here.
# SHOW DATA LIST TABLE
def list_table(request):
    return render(request, 'demoFrontent/table_demo/list_table.html')