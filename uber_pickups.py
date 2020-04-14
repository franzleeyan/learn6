# 天气预告
# url 统一资源定位符
# windows + r  cmd 打开命令行工具 输入pip install requests
# 引入 requests
import urllib.request
# 引入python中内置的包json. 用来解析和生成json数据的
import json
# import itchat


def weather_main():
    city = input('请输入要查询的城市名称：')

    url = 'http://api.map.baidu.com/weather/v1/?district_id=222405&data_type=all&ak=taW58mcmUGG3vutGB2YGFRlSsgrC6xDi'
    # 使用requests发起请求，接受返回的结果
    rs = urllib.request.get(url)
    # 使用loads函数，将json字符串转换为python的字典或列表
    rs_dict = json.loads(rs.text)
    # 取出error
    error_code = rs_dict['error']
    # 如果取出的error为0，表示数据正常，否则没有查询到结果
    if error_code == 0:
        # 从字典中取出数据
       results = rs_dict['results']
       # 根据索引取出天气信息字典
       info_dict = results[0]
        # 根据字典的key，取出城市名称
       city_name = info_dict['city']
        # 取出pm值
       pm25 = info_dict['pm25']
        print('当前城市：%s  pm值：%s'%(city_name,pm25))
        # 取出天气信息列表
       weather_data = info_dict['weather_data']
        # for循环取出每一天天气的小字典
       for weather_dict in weather_data:
            # 取出日期，天气，风级，温度
            date = weather_dict['date']
            weather = weather_dict['weather']
            wind = weather_dict['wind']
            temperature = weather_dict['temperature']
            print('%s %s %s %s'%(date,weather,wind,temperature))

            # # nickname = input('please input your firends\' nickname : ' )
            # #   想给谁发信息，先查找到这个朋友,name后填微信备注即可
            # # users = itchat.search_friends(name=nickname)
            # users = itchat.search_friends(name='起风了')  # 使用备注名来查找实际用户名
            # # 获取好友全部信息,返回一个列表,列表内是一个字典
            # print(users)
            # # 获取`UserName`,用于发送消息
            # userName = users[0]['UserName']
            # itchat.send(date+weather+wind+temperature, toUserName=userName)

            print('succeed')

    else:
        print('没有查询到天气信息')


# itchat.auto_login()
weather_main()