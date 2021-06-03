from luffyapi.libs.rly.SmsSDK import SmsSDK
from luffyapi.settings.dev import SMS
import json

def send_message(mobile,datas,tid='1'):
    sdk = SmsSDK(SMS.get('accId'),SMS.get('accToken'), SMS.get('appId'))
    resp = sdk.sendMessage(tid, mobile, datas)
    return json.loads(resp)# {"statusCode":"000000","templateSMS":{"smsMessageSid":"a51c3cbbe57b41e998e19eacd98e8160","dateCreated":"20210601160416"}}

