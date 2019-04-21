from django.shortcuts import render
from common.get_data import hubspot_api
from common.db_helper import db_helper
from pprint import pprint
from django.http import HttpResponse,JsonResponse
from common.log import Log


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

def chart(request):
    # Lấy list ranking hiển thị người dùng đã setting
    list_show_ranking = "up11-29,up6-10,up1-5,nochange,down1-5,down6-10,down11-29"
    split_list_show_ranking = list_show_ranking.split(",")

    list_label_ranking = []
    for list_show_ranking in split_list_show_ranking:
        if list_show_ranking == "up100higher":
            list_label_ranking.append("Up 100 or higher")
        elif list_show_ranking == "up30-99":
            list_label_ranking.append("Up 30-99")
        elif list_show_ranking == "up11-29":
            list_label_ranking.append("Up 11-29")
        elif list_show_ranking == "up6-10":
            list_label_ranking.append("Up 6-10")
        elif list_show_ranking == "up1-5":
            list_label_ranking.append("Up 1-5")
        elif list_show_ranking == "nochange":
            list_label_ranking.append("No change")
        elif list_show_ranking == "down1-5":
            list_label_ranking.append("Down 1-5")
        elif list_show_ranking == "down6-10":
            list_label_ranking.append("Down 6-10")
        elif list_show_ranking == "down11-29":
            list_label_ranking.append("Down 11-29")
        elif list_show_ranking == "down100":
            list_label_ranking.append("Down 100 or higher")
        
    data = {
        'list_label_ranking' : list_label_ranking
    }

    return render(request, 'demoFrontent/chart.html', data)

def demo(request):
    dict_contact_marketing = {
        'subsrciber' : {
            'label' : 'Subsrciber',
            'list_contact' : [
                {
                    'vid' : '1',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '2',
                    'company' : 'Makudu1',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '3',
                    'company' : 'Makudu2',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
            ]
        },
        'lead' : {
            'label' : 'Lead',
            'list_contact' : [
                {
                    'vid' : '4',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '5',
                    'company' : 'Makudu1',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '5',
                    'company' : 'Makudu2',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
            ]
        },
        'marketingqualifiedlead' : {
            'label' : 'MQL',
            'list_contact' : [
                {
                    'vid' : '1',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                }
            ]
        }
    }

    dict_contact_sales = {
        'subsrciber' : {
            'label' : 'Subsrciber',
            'list_contact' : [
                {
                    'vid' : '1',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '2',
                    'company' : 'Makudu1',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '3',
                    'company' : 'Makudu2',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
            ]
        },
        'lead' : {
            'label' : 'Lead',
            'list_contact' : [
                {
                    'vid' : '4',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '5',
                    'company' : 'Makudu1',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '5',
                    'company' : 'Makudu2',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
            ]
        },
        'marketingqualifiedlead' : {
            'label' : 'MQL',
            'list_contact' : [
                {
                    'vid' : '1',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                }
            ]
        },
        'whatever1' : {
            'label' : 'Whatever 1',
            'list_contact' : [
                {
                    'vid' : '1',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '2',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '3',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
            ]
        },
        'whatever2' : {
            'label' : 'Whatever 2',
            'list_contact' : [
                {
                    'vid' : '1',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '2',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '3',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
            ]
        },
        'whatever3' : {
            'label' : 'Whatever 3',
            'list_contact' : [
                {
                    'vid' : '1',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '2',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '3',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
            ]
        },
        'whatever4' : {
            'label' : 'Whatever 4',
            'list_contact' : [
                {
                    'vid' : '1',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '2',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
                {
                    'vid' : '3',
                    'company' : 'Makudu',
                    'firstname' : 'Trina',
                    'lastname' : 'Foo2',
                    'closedate' : '2019-02-01'
                },
            ]
        }

    }

    data = {
        'dict_contact_marketing' : dict_contact_marketing,
        'dict_contact_sales' : dict_contact_sales
    }
    return render(request, 'demoFrontent/demo.html', data)

def demo_sales_setting(request):
    return render(request, 'demoFrontent/demo_sells_setting.html')

def ajax_get_form_sale_setting(request):
  if request.method == 'POST':

    if request.is_ajax():
      try:
        #1)Lấy dữ liệu từ request
        return render(request, 'demoFrontent/data/data_sale_setting.html')

      except Exception as inst:
        result = Log.write_log(inst)
        return HttpResponse(result)
        
    return HttpResponse('')