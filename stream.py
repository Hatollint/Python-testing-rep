#!/usr/bin/env python
# encoding: utf-8
import json
import websocket
import requests
import random

def init_streaming_server(token): #Возвращяет данные для подключения
    request_url = "https://api.vk.com/method/streaming.getServerUrl?access_token={}&v=5.64".format(token)
    r = requests.get(request_url)
    data = r.json()
    print (data["response"]["key"])
    return {"server":data["response"]["endpoint"],"key":data["response"]["key"]}

def set_my_rules(value):
    rule_params = {"rule":{"value":value,"tag":'tag_'+str(random.randint(11111,99999))}}
    headers = {'content-type': 'application/json'}
    r = requests.post("https://{}/rules?key={}".format(stream["server"], stream["key"]), data=json.dumps(rule_params), headers=headers)
    data = r.json()
    return data['code'] == 200

def get_my_rules():
    r = requests.get("https://{}/rules?key={}".format(stream["server"], stream["key"]))
    data = r.json()
    if data['code'] != 200:
        return False

    return data['rules']

def del_my_rules(tag):
    headers = {'content-type': 'application/json'}
    rule_params = {"tag":tag}
    r = requests.delete("https://{}/rules?key={}".format(stream["server"], stream["key"]), data=json.dumps(rule_params), headers=headers)
    data = r.json()

    return data['code'] == 200

def listen_stream():
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://{}/stream?key={} ".format(stream["server"], stream["key"]),
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

def on_message(ws, message):
    data = json.loads(message)
    print("\r\n Text:", message[''])

def on_error(ws, error):
    print("Error:",error)

def on_close(ws):
    print("Close Thead")

def on_open(ws):
    print("Open Thead")
    
    
stream = init_streaming_server("88247f7988247f7988247f79a2887ad6d68882488247f79d1f4910dee8657d505692782")
rules = get_my_rules()
try:
    for rule in rules:
        print (rule)
        del_my_rules(rule['tag'])
    print ("Kill rules - Done. Start streaming!")
except Exception as e:
    print(e)
    
set_my_rules('россия')
listen_stream()
