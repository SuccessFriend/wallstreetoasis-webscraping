import requests
import csv
from datetime import datetime

def get_data():
    
    initial = ["Channel Number", "Channel Name", "Start Time", "Duration", "Program Name"]
    with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(initial)

    tDate = datetime.today().strftime('%Y-%m-%d')
    
    with open('channels.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            Number = row[1]
            Name = row[0]

            targetURL = f"https://www.eternityready.tv/live-tv/schedule/{Number}/{tDate}"
            headers = {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest",
                "cookie": "_ga=GA1.2.659833277.1710525344; _gid=GA1.2.389328520.1710525347; _ga_WTK9PYWWDG=GS1.1.1710580771.2.0.1710580771.0.0.0",
                "Referer": "https://www.eternityready.tv/live-tv",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            }
        
            response = requests.get(targetURL, headers=headers)

            if response.ok:
                datas = response.json()  # assuming the response is in JSON format

                for data in datas:
                    starts = data["starts"][0] + data["starts"][1] + ":" + data["starts"][2] + data["starts"][3]
                    duration = data["duration"]
                    program_name = data["program_name"]

                    result = [Number, Name, starts, duration, program_name]
                    with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow(result)

get_data()