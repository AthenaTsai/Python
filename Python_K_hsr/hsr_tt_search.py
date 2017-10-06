import requests
import pandas as pd
import html5lib
import timeit
from bs4 import BeautifulSoup


# import timeit



def THSR(StartStation, EndStation, SearchDate, SearchTime, SearchWay):
    station = {
        '南港': '2f940836-cedc-41ef-8e28-c2336ac8fe68',
        '台北': '977abb69-413a-4ccf-a109-0272c24fd490',
        '板橋': 'e6e26e66-7dc1-458f-b2f3-71ce65fdc95f',
        '桃園': 'fbd828d8-b1da-4b06-a3bd-680cdca4d2cd',
        '新竹': 'a7a04c89-900b-4798-95a3-c01c455622f4',
        '苗栗': 'e8fc2123-2aaf-46ff-ad79-51d4002a1ef3',
        '台中': '3301e395-46b8-47aa-aa37-139e15708779',
        '彰化': '38b8c40b-aef0-4d66-b257-da96ec51620e',
        '雲林': '5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f',
        '嘉義': '60831846-f0e4-47f6-9b5b-46323ebdcef7',
        '台南': '9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
        '左營': 'f2519629-5973-4d08-913b-479cce78a356'
    }

    sway = {
        '出發': 'DepartureInMandarin',
        '抵達': 'ArrivalInMandarin'
    }

    # all 5 required
    parameter = {
        'StartStation': station.get(StartStation),
        'EndStation': station.get(EndStation),
        'SearchDate': SearchDate[0:4] + '/' + SearchDate[4:6] + '/' + SearchDate[6:8],
        'SearchTime': SearchTime[0:2] + ':' + SearchTime[2:4],
        'SearchWay': sway.get(SearchWay)
    }

    url = 'https://www.thsrc.com.tw/tw/TimeTable/SearchResult'

    #     start = timeit.default_timer() # 計算高鐵網站回應時間
    html_result = BeautifulSoup(requests.post(url=url, data=parameter).text, 'lxml')
    #     stop = timeit.default_timer()  # 計算高鐵網站回應時間
    #     print(stop-start)              # 計算高鐵網站回應時間


    # 時刻表查詢結果 變數宣告儲存
    train_schedule = list()
    for i in html_result.findAll('table', {'class': 'touch_table'}):  # 找尋 html tag 裡面有 td 且屬性 class 為 toTouch
        for x in i.findAll('td', limit=4):
            train_schedule.append(x.text)

    # 轉化為表格
    train_schedule_to_df = list()
    train_index = len(train_schedule)
    start_iter = 0
    for x in range(4, train_index + 1, 4):
        train_schedule_to_df.append(train_schedule[start_iter:x])
        start_iter = x
    df_columns = ['車次', '出發時間', '抵達時間', '行車時間']
    df_result = pd.DataFrame(data=train_schedule_to_df, columns=df_columns)

    return df_result

result = THSR('台北', '左營', '20171006', '1230', '抵達')
print(result)
