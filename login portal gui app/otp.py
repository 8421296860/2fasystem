import math
import random
import request_otp


def otpfunc(userid):
    corpus = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    generate_OTP = ""
    size = 5
    length = len(corpus)
    for i in range(size):
        generate_OTP += corpus[math.floor(random.random() * length)]
    
    request_otp.send_req(userid,generate_OTP)
    return generate_OTP


