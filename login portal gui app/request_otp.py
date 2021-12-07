import requests


def send_req(userid,otp):
    req = 'https://motion-alert.azurewebsites.net/api/myfirstfunction?name='+str(userid)+'&otp_send='+str(otp)
    response = str(requests.get(req))
    if response == "<Response [200]>":
        print("OTP Sent successfully.....")
