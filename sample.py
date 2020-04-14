#字典方式直接转换成url参数
from urllib.parse import urlencode
params = {
    'name':'germey',
    'age':'122'
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)
