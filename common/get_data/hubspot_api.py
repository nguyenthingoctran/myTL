import requests
import urllib.request
import json

PREV_API_URl = "http://api.hubapi.com"
API_KEY = "demo"
COUNT = "100"

# ====================================================================
# =================== LIST ===========================================
# ====================================================================

# LẤY LIST_VID TỪ MỘT LIST
def get_list_vid_in_list(listID = "516085"):
    has_more = True
    vid_offset = "0"
    list_contact = []
    while has_more == True:
        requestUrl = PREV_API_URl + "/contacts/v1/lists/"+ listID +"/contacts/all?vidOffset=" + vid_offset + "&count=" + COUNT + "&hapikey=" + API_KEY
        statistics = requests.get(requestUrl).json()
        for vid in statistics['contacts']:
            list_contact.append(vid['vid'])
        has_more = statistics['has-more']
        vid_offset = str(statistics['vid-offset'])
    return list_contact

# ====================================================================
# =================== CONTACT ========================================
# ====================================================================

# LẤY THÔNG TIN CHI TIẾT CỦA MỘT CONTACT
def get_info_contact(vid):
    url = PREV_API_URl + "/contacts/v1/contact/vid/"+ str(vid) +"/profile?hapikey=demo&property=createdate&property=state&property=lastname&property=phone&property=firstname&property=city&property=company&property=company&property=photo&property=lifecyclestage"
    list_info_a_contact = {}
    with urllib.request.urlopen(url) as url:
        response = url.read()
    all_info_contact = json.loads(response)

    for key, value in all_info_contact['properties'].items():
        list_info_a_contact[key] = value['value']
    return list_info_a_contact