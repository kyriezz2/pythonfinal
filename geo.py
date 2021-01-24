import requests,json
import pandas as pd
import pandas as display
# 地理编码函数
zmf_key= '33c09d3dd1144ed439260dff0cd0c5bc'
def geocode(key,address,city=None,batch=None)->str:
    """获取高德API的地理编码
    注释：key是指高德API的秘钥，请先去注册
          address是指结构化地址，具体请查看：https://lbs.amap.com/api/webservice/guide/api/georegeo   
    """
    url = "https://restapi.amap.com/v3/geocode/geo?paramete." \
          "" \
          "//rs"
    params = {
        "key":key,
        "address":address,
        "city":city,
        "batch":batch
    }
    response = requests.get(url,params=params)
    results = response.json()['geocodes'][0]['location']
    # 返回值
    return results

# 逆地理编码
def regeo(key,location,extensions="base",radius=None,poitype=None):
    """"""
    url = "https://restapi.amap.com/v3/geocode/regeo?parameters"
    params = {
        "key":key,
        "location":location,
        "extensions":extensions,
        "radius":radius,
        "poitype":poitype
    }
    r = requests.get(url,params)
    results = r.json()
    return results

# 步行路经规划函数
def walk(key,origin,destination):
    walk_url = "https://restapi.amap.com/v3/direction/walking?parameters"
    params ={
        "key":key,
        "origin":origin,
        "destination":destination
    }
    r = requests.get(walk_url,params=params)
    d = r.json()
    f = pd.json_normalize(d["route"]["paths"][0]['steps'])
    result=f["instruction"]
    return result
# 车辆路线规划
def car(key,origin,destination,extensions='base'):
    car_url = "https://restapi.amap.com/v3/direction/driving?parameters"
    params ={
        "key":key,
        "origin":origin,
        "destination":destination,
        'extensions':extensions,
    }
    r = requests.get(car_url,params=params)
    d = r.json()
    f = pd.json_normalize(d["route"]["paths"][0]['steps'])
    result=f["instruction"]
    return result

# 公交车路径规划函数
def bus(key,origin,destination,city):
    bus_url = "https://restapi.amap.com/v3/direction/transit/integrated?parameters"
    params ={
        "key":key,
        "origin":origin,
        "destination":destination,
        "city":city
    }
    r = requests.get(bus_url,params=params)
    d=r.json()['route']['transits'][0]['segments'][0]['bus']['buslines']
    df_步行路径规划 = pd.json_normalize(d)
    result=df_步行路径规划
    return result

# 骑行路径规划函数
def cycle(key,origin,destination):
    cycle_url = "https://restapi.amap.com/v4/direction/bicycling?parameters"
    params ={
        "key":key,
        "origin":origin,
        "destination":destination
    }
    r = requests.get(cycle_url,params=params)
    d = r.json()['data']['paths'][0]['steps']
    df_骑行路径规划 = pd.json_normalize(d)['instruction']
    result=df_骑行路径规划
    return result

# 货车路径规划的函数
def truck(key,origin,destination,size,originid=None,originidtype=None,destinationid=None,destinationtype=None,diu=None,strategy=1,waypoints=None,height=1.6,width=2.5,load=10,weight=0.9,axis=2,province=None,number=None,cartype=0,avoidpolygons=None,showpolyline=1,nosteps=0,output="json"):
    url = "https://restapi.amap.com/v4/direction/truck?parameters"
    params = {
        "key":key,
        "origin":origin,
        "originidtype":originidtype,
        "destination":destination,
        "destinationid":destinationid,
        "destinationtype":destinationtype,
        "diu":diu,
        "strategy":strategy,
        "waypoints":waypoints,
        "size":size,
        "height":height,
        "width":width,
        "load":load,
        "weight":weight,
        "axis":axis,
        "province":province,
        "number":number,
        "cartype":cartype,
        "avoidpolygons":avoidpolygons,
        "showpolyline":showpolyline,
        "nosteps":nosteps,
        "output":output
    }
    r = requests.get(url,params)
    d = r.json()['data']['route']['paths'][0]['steps']
    df_步行路径规划 = pd.json_normalize(d)['instruction']
    result=df_步行路径规划
    return result

# 距离测量的函数
def distance(key,origins,destination,type=1,sig=None,output="json",callback=None):
    url = "https://restapi.amap.com/v3/distance?parameters"
    params = {
        "key":key,
        "origins":origins,
        "destination":destination,
        "type":type,
        "sig":sig,
        "output":output,
        "callback":callback
    }
    r = requests.get(url,params)
    results = r.json()
    return results


# 行政区域查询的函数
def district(key,keywords=None,subdistrict=1,page=1,offset=20,extensions="base",filter=None,callback=None,output="json"):
    url = "https://restapi.amap.com/v3/config/district?parameters"
    params = {
        "key":key,
        "keywords":keywords,
        "subdistrict":subdistrict,
        "page":page,
        "offset":offset,
        "extensions":extensions,
        "filter":filter,
        "callback":callback,
        "output":output
    }
    r = requests.get(url,params)
    results = r.json()
    return results


# 关键字搜索的函数
def text(key,keywords=None,types=None,city=None,citylimit="false",children=0,offset=20,page=1,extensions="base",sig=None,output="json",callback=None):
    url = "https://restapi.amap.com/v3/place/text?parameters"
    params = {
        "key":key,
        "keywords":keywords,
        "types":types,
        "city":city,
        "citylimit":citylimit,
        "children":children,
        "offset":offset,
        "page":page,
        "extensions":extensions,
        "sig":sig,
        "output":output,
        "callback":callback
    }
    r = requests.get(url,params)
    results = r.json()
    return results


# 周边搜索的函数
def around(key,location,keywords=None,types=None,city=None,radius=3000,sortrule="distance",offset=20,page=1,extensions="base",sig=None,output="json",callback=None):
    url = "https://restapi.amap.com/v3/place/around?parameters"
    params = {
        "key":key,
        "location":location,
        "keywords":keywords,
        "types":types,
        "city":city,
        "radius":radius,
        "sortrule":sortrule,
        "offset":offset,
        "page":page,
        "extensions":extensions,
        "sig":sig,
        "output":output,
        "callback":callback
    }
    r = requests.get(url,params)
    results = r.json()
    return results


# 多边形搜索的函数
import json
def polygon(key,polygon,keywords=None,types=None,offset=20,page=1,extensions="base",sig=None,output="json",callback=None):
    url = "https://restapi.amap.com/v3/place/polygon?parameters"
    params = {
        "key":key,
        "polygon":polygon,
        "keywords":keywords,
        "types":types,
        "offset":offset,
        "page":page,
        "extensions":extensions,
        "sig":sig,
        "output":output,
        "callback":callback        
    }
    r =requests.get(url,params)
    results = r.json()
    return results


# ID查询的函数
def detail(key,id,sig=None,output="json",callback=None):
    url = "https://restapi.amap.com/v3/place/detail?parameters"
    params = {
        "key":key,
        "id":id,
        "sig":sig,
        "output":output,
        "callback":callback
    }
    r = requests.get(url,params)
    results = r.json()
    return results


# IP定位的函数
def ip(key,ip,sig=None,output="json"):
    url = "https://restapi.amap.com/v3/ip?parameters"
    params = {
        "key":key,
        "ip":ip,
        "sig":sig,
        "output":output
    }
    r = requests.get(url,params)
    results = r.json()
    return results


# 静态地图的函数
def staticmap(key,location,zoom):
    url = "https://restapi.amap.com/v3/staticmap?parameters"
    params = {
        "key":key,
        "location":location,
        "zoom":zoom
    }
    r = requests.get(url,params=params)
    results = mage.open(BytesIO(r.content))
    return results


# 坐标转换的函数
def convert(key,locations,coordsys="autonavi",output="json"):
    url = "https://restapi.amap.com/v3/assistant/coordinate/convert?parameters"
    params = {
        "key":key,
        "locations":locations,
        "coordsys":coordsys,
        "output":output
    }
    r = requests.get(url,params)
    results = r.json()
    return results


# 天气查询
def weatherinfo(key,city,extensions="all",output="json"):
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    params = {
        "key":key,
        "city":city,
        "extensions":extensions,
        "output":output
    }
    r = requests.get(url,params)
    results = r.json()
    return results


# 输入提示的函数
def inputtips(key,keywords,type=None,location=None,city=None,citylimit=None,datatype="all",sig=None,output=None,callback=None):
    url = "https://restapi.amap.com/v3/assistant/inputtips?parameters"
    params = {
        "key":key,
        "keywords":keywords,
        "type":type,
        "location":location,
        "city":city,
        "citylimit":citylimit,
        "datatype":datatype,
        "sig":sig,
        "output":output,
        "callback":callback
    }
    r = requests.get(url,params)
    results = r.json()
    return results