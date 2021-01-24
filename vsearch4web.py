# flask web 网络编程文件
from flask import Flask, render_template, request,escape
from geo import walk, bus,car,geocode,cycle,truck,around

# html 调用方法：render_template  按照 jinja2 规则
def log_request(req: 'flask_request',res: str) -> None:
    with open('fen.py','a')as log:

        print(req.form, req.remote_addr,req.user_agent,res,file=log,sep=" | ")
zmf_key= '33c09d3dd1144ed439260dff0cd0c5bc'
xu_key = "1a8b4a8f8eacf6e72af8287289e0e270"
app = Flask(__name__)

@app.route('/')
@app.route('/zhoumingfeng')
def huang_xx() -> 'html':
    return render_template('home.html',)

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('fen.py') as log:
        for line in log:
            contents.append([])
            for item in line.split(' | '):
                contents[-1].append(escape(item))
    titles = ('Form Data','Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='日志系统',
                           the_row_titles=titles,
                           the_data=contents,)
@app.route('/entry')
def entry_page_1() -> 'html':
    return render_template('entry_bianma.html',)
@app.route('/entry2')
def entry_page_2() -> 'html':
    return render_template('entry_walk.html',)

@app.route('/entry3')
def entry_page3() -> 'html':
    return render_template('entry_bus.html',)

@app.route('/entry4')
def entry_page4() -> 'html':
    return render_template('entry_drive.html',)

@app.route('/entry5')
def entry_page5() -> 'html':
    return render_template('entry_riding.html',)
@app.route('/entry6')
def entry_page6() -> 'html':
    return render_template('entry_trucks.html',)
@app.route('/entry7')
def entry_page7() -> 'html':
    return render_template('entry_zhoubian.html',)

@app.route('/search', methods=['POST'])
def do_search1() -> 'html':
    # 获取颜色=request.form['color']
    # 获取颜色1=request.form['color01']
    用户输入的结构化地址 = request.form['geocode']
    经纬度坐标 = geocode(zmf_key, 用户输入的结构化地址)
    return render_template('result_bianma.html',
                           the_geo=经纬度坐标,)
                           # the_color=获取颜色)
                           # the_color01=获取颜色1,

@app.route('/search2', methods=['POST'])
def do_search2() -> 'html':
    获取起点 = request.form['walk_origin']
    起点 = geocode(zmf_key, 获取起点)
    获取终点 = request.form['walk_disitination']
    终点 = geocode(zmf_key, 获取终点)
    步行规划 = walk(zmf_key,起点,终点)
    return render_template('result_walk.html',
                           the_walk=步行规划,
                           the_origin=获取起点,
                           the_disitination=获取终点,)
@app.route('/search3', methods=['POST'])
def do_search3() -> 'html':
    获取公交起点 = request.form['bus_origin']
    bus_origin1 = geocode(zmf_key, 获取公交起点)
    获取公交终点 = request.form['bus_zhongdian']
    bus_city1=request.form['bus_city']
    bus_disitination1 = geocode(zmf_key, 获取公交终点)
    公交规划 = bus(zmf_key,bus_origin1,bus_disitination1,bus_city1)
    return render_template('result_bus.html',
                           the_bus=公交规划,
                           thebus_origin=获取公交起点,
                           thebus_disitination= 获取公交终点,
                           )

@app.route('/search4', methods=['POST'])
def do_search4() -> 'html':
    获取车辆起点 = request.form['car_origin']
    bus_origin1 = geocode(zmf_key, 获取车辆起点)
    获取车辆终点 = request.form['car_zhongdian']
    car_disitination1 = geocode(zmf_key, 获取车辆终点)
    车辆规划 = car(zmf_key,bus_origin1,car_disitination1)
    return render_template('result_drive.html',
                           the_car=车辆规划,
                           thecar_origin=获取车辆起点,
                           thecar_disitination= 获取车辆终点,
                           )
@app.route('/search5', methods=['POST'])
def do_search5() -> 'html':
    获取骑行起点 = request.form['cycle_origin']
    cycle_origin1 = geocode(zmf_key, 获取骑行起点)
    获取骑行终点 = request.form['cycle_zhongdian']
    cycle_disitination1 = geocode(zmf_key, 获取骑行终点)
    车辆规划 = cycle(zmf_key,cycle_origin1,cycle_disitination1)
    return render_template('result_riding.html',
                           the_cycle=车辆规划,
                           thecar_origin=获取骑行起点,
                           thecar_disitination= 获取骑行终点,
                           )
@app.route('/search6', methods=['POST'])
def do_search6() -> 'html':
    获取货车起点 = request.form['huoche_origin']
    huoche_origin1 = geocode(zmf_key, 获取货车起点)
    获取货车终点 = request.form['huoche_zhongdian']
    huoche_disitination1 = geocode(zmf_key, 获取货车终点)
    huochesize1=request.form['huoche_size']
    货车规划 = truck(xu_key,huoche_origin1,huoche_disitination1,huochesize1,)
    return render_template('result_6.html',
                           the_huoche=货车规划,
                           thehuoche_origin=获取货车起点,
                           thehuoche_disitination= 获取货车终点,
                           )
@app.route('/search7', methods=['POST'])
def do_search7() -> 'html':
    didian=request.form['around_origin']
    周边1=geocode(zmf_key,didian)
    周边=around(zmf_key, 周边1)
    return render_template('result_zhoubian.html',
                           the_zhoubian=周边,
                           )

if __name__ == '__main__':
    app.run(debug=True)
