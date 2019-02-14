from django.shortcuts import render

# Create your views here.
# SHOW DATA LIST TABLE
def list_table(request):
    return render(request, 'demoFrontent/table_demo/list_table.html')

def copy_to_clipboard(request):
    return render(request, 'demoFrontent/page_copy_to_clipboard.html')