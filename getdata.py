#encode: utf-8
import requests
import numpy
import time,sys,os
import configparser
from urllib import request
from urllib import parse
def parse1(data):
    print("地区名："+data["name"])
    updateDate=data["trend"]["updateDate"]
    last=len(updateDate)-1
    date=updateDate[last]
    print("日期："+date)
    for i in data["trend"]["list"]:
        #print(i)
        lst=len(i["data"])-1
        print(i["name"]+":"+(str)(i["data"][lst]))
    print("-------")

if __name__=="__main__":
    url = "https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish"
    response=requests.post(url)
    data=response.json()
    print(data['msg'])
    for i in data["data"]:
        parse1(i)