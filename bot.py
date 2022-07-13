import requests
from datetime import datetime
#Telegram API URL
#chat_url = https://api.telegram.org/bot16865xxxx:AAFYtHHqBN0326dxxxxFHKq6rStkXhpvQk/sendMessage?chat_id=@__groupid__&text=
api_url_telegram = "/////////////////////////////////////chat url//////////////////////////////////// "
telegram_api_bot= "https://api.telegram.org/bot"

group_id = "vaccinetest123"
bot_token = "1686545061:AAFYtHHqBN0326d3aMraFHKq6rStkXhpvQk"
#COWIN API URL
base_cowin_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")

raj_district_ids = [511,373]

#Functions
def fetch_data_from_cowin(district_id):
    query_params = "?district_id={}&date={}".format(district_id,today_date)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    final_url = base_cowin_url + query_params
    response = requests.get(final_url, headers=headers)
    extract_availability_data(response)
    #print(response)
	
def fetch_data_for_state(district_ids):
    for district_id in district_ids:
        fetch_data_from_cowin(district_id)

def extract_availability_data(response):
    response_json = response.json()
    for center in response_json["centers"]:
        for session in center["sessions"]:
            if session["available_capacity_dose1"] > 0:
                message = "Pincode: {}, Name : {}, Slots:{},Minimum Age: {} ".format(center["pincode"],center["name"],session["available_capacity_dose1"],session["min_age_limit"])
                send_message_telegram(message)
        
def send_message_telegram(message):
    final_telegram_url=api_url_telegram.replace("__groupid__", group_id)
    final_telegram_url = final_telegram_url + message
    response = requests.get(final_telegram_url)
    print(response)

'''       
def find_chatid():
    find_chatid = "/getUpdates"
    query_chatid =  telegram_api_bot + bot_token +find_chatid    
    response_chat = requests.get(query_chatid)
    #print(response_chat)
    extract_chatid(response_chat)
    
def extract_chatid(response_chat):
    response_chat_json = response_chat.json()
    for res in response_chat_json["result"] :
        for msg in res["message"]:
            for chat in msg["chat"]:
                print("msg checked")
    
    
'''     
if __name__ == "__main__":
    #fetch_data_for_state(raj_district_ids)
    fetch_data_for_state(raj_district_ids)
