import json
import requests
from bs4 import BeautifulSoup
import os
import time

class leetocode : 

    def extract_data(self , url):
    
        r = requests.get(url)

        soup = BeautifulSoup(r.text , 'html.parser')

        res = soup.find_all('script' , attrs={"id":"__NEXT_DATA__"})

        data = json.loads(res[0].contents[0])
        fildered_data = data["props"]["pageProps"]["dehydratedState"]["queries"][0]['state']['data']['question']

        keys = fildered_data.keys()
        keys = list(keys)
        tags = []

        for i in data["props"]["pageProps"]["dehydratedState"]["queries"][9]["state"]["data"]["question"]["topicTags"]:
            tags.append(i['name'])

        ques_no = fildered_data[keys[0]]
        title = fildered_data[keys[2]]
        difficulty = fildered_data[keys[5]]

        return (ques_no , title , difficulty , tags)

    def get_json(self , url):
        (ques_no , title , difficulty , tags) = self.extract_data(url=url)

        data = {
            "q_number":ques_no,
            "title" : title,
            "difficulty":difficulty,
            "tags":tags
        }

        return json.dumps(data)


if __name__ == "__main__":

    os.system("CLS")
    s = leetocode()

    enter = -1
    while enter == -1:

        url =  input("Enter the problem link : ")
        if url.find("https://") == -1 or url.find("leetcode.com") == -1:
            enter = -1
            print("Enter a valid link")
            time.sleep(2)
            os.system("CLS")
        else :
            enter = 0

    data = s.get_json(url=url)
    print(json.loads(data))

    
