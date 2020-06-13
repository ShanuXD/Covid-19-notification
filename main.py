from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
    notification.notify(
        title= title,
        message=message,
        app_icon="icon_sample.ico",
        timeout=15

    )
def getData(url):
    req=requests.get(url)
    return req.text

if __name__ =="__main__":
    while True:
        #notifyMe('shanu','hello from the other side')
        htmlData=getData('https://www.mohfw.gov.in/')
        soup=BeautifulSoup(htmlData,'html.parser')
        #print(soup.prettify())
        myCoronaData=""
        for tr in soup.find_all('tbody'):
            myCoronaData=tr.get_text()
        myCoronaData=myCoronaData[2:]
        #print(myCoronaData)
        data=myCoronaData.split("\n\n\n")
        state=['Jharkhand','Odisha','West Bengal']
        for state_data in data[:35]:
            dataList=state_data.split("\n")
            if dataList[1] in state:
                #print(dataList)
                notification_text=f"State:{dataList[1]}\nCases: {dataList[2]}\nCured: {dataList[3]}, death: {dataList[4]}\nConformCase: {dataList[5]}"
                notifyMe('Cases Of Covid-19',notification_text)
                time.sleep(2)
        time.sleep(20)

