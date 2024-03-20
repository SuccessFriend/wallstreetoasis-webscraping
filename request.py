import requests
import csv


def scrapFunction():

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9,ko;q=0.8",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "cookie": "_wingify_pc_uuid=8a9906f27dbe4e20a0689f43dacd1899; _gcl_au=1.1.1714061934.1710809347; _gid=GA1.2.1144493223.1710809356; wingify_donot_track_actions=0; SSESS84b8eb2fc163af7faac8c002380d1992=0pIbnew0PGntedE2jhS%2C1M%2C1O%2CxOS8KWFoWFUktO0gRlLUKJ; _pbjs_userid_consent_data=3524755945110770; _pubcid=0e5c974a-ad92-4f26-a494-73edf2668d77; AMP_TOKEN=%24NOT_FOUND; _ga_V8N6PBSJ8B=GS1.1.1710819039.2.1.1710819165.59.0.0; _ga=GA1.2.770924125.1710809352; _gat_UA-2564900-1=1"
    }

    response = requests.get("https://www.wallstreetoasis.com/forum/real-estate/pipd-help", headers=headers)

    if response.ok:
        data = response.json()  # assuming the response is in JSON format
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ", data)
        # channels = data["channels"]
        # for channel in channels:
        #     name = channel["name"]
        #     number = channel["number"]
        #     schedule_url = channel["schedule_url"]

        #     result = [name, number, schedule_url]
        #     with open('channels.csv', mode='a', newline='', encoding='utf-8') as file:
        #         writer = csv.writer(file)
        #         writer.writerow(result)

scrapFunction()