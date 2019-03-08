from django.shortcuts import render

# Create your views here.
# SHOW DATA LIST TABLE
def list_table(request):
    return render(request, 'demoFrontent/table_demo/list_table.html')

def copy_to_clipboard(request):
    return render(request, 'demoFrontent/page_copy_to_clipboard.html')

def notification(request):
    return render(request, 'demoFrontent/page_notification.html')

def select2_single(request):
    return render(request, 'demoFrontent/page_select_2.html')

def dragable(request):
    return render(request, 'demoFrontent/dragable.html')
def spinner(request):
    return render(request, 'demoFrontent/page_spinner.html')
