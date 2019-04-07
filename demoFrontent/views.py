from django.shortcuts import render
from common.get_data import hubspot_api
from common.db_helper import db_helper
from pprint import pprint

db_controller = db_helper()

# Create your views here.
# SHOW DATA LIST TABLE
def list_table(request):
    # Lấy dữ liệu từ database
    

    return render(request, 'demoFrontent/table_demo/list_table.html')

def copy_to_clipboard(request):
    return render(request, 'demoFrontent/page_copy_to_clipboard.html')

def notification(request):
    return render(request, 'demoFrontent/page_notification.html')

def select2_single(request):
    return render(request, 'demoFrontent/page_select_2.html')

def dragable(request):
    list_vid = hubspot_api.get_list_vid_in_list()
    list_info_contact = []
    for vid in list_vid:
        info_contact = hubspot_api.get_info_contact(vid)
        list_info_contact.append(info_contact)

    # Lấy list lifecycle stage
    sql_query_list_lifecycle = ''' SELECT * FROM demo.lifecycle_stages; '''
    object_list_lifecycle = db_controller.query(sql_query_list_lifecycle) 
        
    data = {
        'info_contact' : list_info_contact,
        'list_lifecycle' : object_list_lifecycle
    }
    return render(request, 'demoFrontent/dragable.html', data)
    
def spinner(request):
    return render(request, 'demoFrontent/page_spinner.html')
