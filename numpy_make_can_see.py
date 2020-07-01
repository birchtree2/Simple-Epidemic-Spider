#encode: utf-8
import requests
import numpy
import time,sys,os
import configparser
from urllib import request
from urllib import parse
import matplotlib.pyplot as plt

def make_graph(t,x,y):
    plt.rcParams['font.sans-serif']='SimHei'
    plt.rcParams['axes.unicode_minus']=False
    #plt.figure()
    plt.title(t)
    plt.bar(x,y,linewidth=2.0,linestyle='--')
    plt.legend()
    plt.show()

def process(data):
    """
    Process data , output date and show graph
    """
    print("地区名："+data["name"])
    updateDate=data["trend"]["updateDate"]
    first,last=0,len(updateDate)-1
    print("日期："+updateDate[first]+" -> "+updateDate[last])
    for i in data["trend"]["list"]:
        make_graph(i["name"],updateDate,i["data"])
    print("-------")

if __name__=="__main__":
    url="https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish"
    response=requests.post(url)
    data=response.json()
    print(data['msg'])
    for i in data["data"]:
        process(i)