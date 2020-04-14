# 引入request模块
# 引入json模块
import json
import urllib.request
from urllib import response
from urllib.request import urlopen
from urllib.parse import urlencode
# from request import gettext

def weather_main():
    City = input('请输入要查询的城市名称： ') # 输入城市名称
    location = City # 定义城市参数

    # 拼接输入和key
    params = {
        'location':location,
        'key':'dcb2ae571d2a47c8bbc18930513b170b'
    }
    base_url = 'https://free-api.heweather.net/s6/weather/now?'
    url = base_url+urlencode(params)

    # 使用request发起请求，接受返回的结果
    rs = urllib.response.List(url)
    rs.decode('utf-8')
    # 使用loads函数，将json字符串转换为python的字典或者列表
    rs_dict = json.loads(rs)
    # 取出status
    error_code = rs_dict['error']
    # 取出status为ok，标识数据正常，否则没有查询到结果
    if error_code == 0:
        results = rs_dict['results']
        info_dict = results[0]
        city_name = info_dict['city']
        pm25 = info_dict['pm25']
        print('当前城市: %s  pm值: %s' %(city_name, pm25))
        weather_data = info_dict['weather_data']
        for weather_dict in weather_data:
            date = weather_dict['data']
            weather = weather_dict['weather']
            wind = weather_dict['wind']
            temperature = weather_dict['temperature']
            print('%s %s %s %s' % (date, weather, wind, temperature))
    else:
        print('没有查询到天气信息')

weather_main()

# url = "https://free-api.heweather.net/s6/weather/now?location=beijing&key=dcb2ae571d2a47c8bbc18930513b170b"
# # req = urllib.request(url)
# req = urlopen(url)
# print(req)
# resp = req.read().decode('utf8')


# #将JSON转化为Python的数据结构
# json_data = json.loads(resp)
# data = json_data['HeWeather6'][0]
#
# #获取PM2.5的值
# pm25 = data['aqi']['city']['pm25']
# #获取空气质量
# air_quality = data['aqi']['city']['qlty']
#
# #获取城市
# city = data['basic']['city']
#
# #获取现在的天气、温度、体感温度、风向、风力等级
# now_weather = data['now']['cond']['txt']
# now_tmp = data['now']['tmp']
# now_fl = data['now']['fl']
# now_wind_dir = data['now']['wind']['dir']
# now_wind_sc = data['now']['wind']['sc']
#
# #今天的天气
# today = data['daily_forecast'][0]
# weather_day = today['cond']['txt_d']
# weather_night = today['cond']['txt_n']
# tmp_high = today['tmp']['max']
# tmp_low = today['tmp']['min']
# wind_dir = today['wind']['dir']
# wind_sc = today['wind']['sc']
#
# #天气建议
#
# #舒适度
# comf = data['suggestion']['comf']['brf']
# comf_txt = data['suggestion']['comf']['txt']
#
# #流感指数
# flu = data['suggestion']['flu']['brf']
# flu_txt = data['suggestion']['flu']['txt']
#
# #穿衣指数
# drsg = data['suggestion']['drsg']['brf']
# drsg_txt = data['suggestion']['drsg']['txt']
#
# weather_forcast_txt = "%s今天白天天气%s,夜间天气%s,最高气温%s摄氏度,最低气温%s摄氏度,风力%s,风向%s,天气舒适度：%s,%s,流感" \
#                       "指数：%s,%s 穿衣指数：%s,%s 现在外面的天气：%s,当前温度:%s,当前风力:%s"%(city,weather_day,weather_night,tmp_high,tmp_low,wind_sc,wind_dir,comf,comf_txt,flu,flu_txt,drsg,drsg_txt,now_weather,now_tmp,now_wind_sc)
#
# print(weather_forcast_txt)

