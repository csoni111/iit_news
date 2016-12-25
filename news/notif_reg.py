import requests
from user_agents import parse

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def regiter_token_for_topic(token):
 	url = 'https://iid.googleapis.com/iid/v1/'+ token +'/rel/topics/iitnews'
 	headers = {'Authorization': 'key=AAAA8Vstr2U:APA91bGMpzQlTdM96Xt5HwBDmy_jubWoIyPBG9_ZJZUVMHJctl-'
		+'hBP5MZ35aeUTnNOR5o8sJfy5i5FyPU_QUt2KySzVDQCnEf_leOcni31iwC17_bpMD24ptoOrjMDwwfcQ9pOx'
		+'TIXBRfAKz_DV3_oZ6cpkbbP_fuA'}
 	r = requests.post(url, headers=headers)
 	return r.status_code

def getUserDetails(request):
	ua_string = request.META.get('HTTP_USER_AGENT')
	user_agent = parse(ua_string)
	browser = user_agent.browser.family + ' ' + user_agent.browser.version_string
	os = user_agent.os.family + ' ' + user_agent.os.version_string
	device = user_agent.device.family
	return browser, os, device