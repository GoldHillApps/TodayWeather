import ybc_ai
import ybc_ui
import ybc_data



r=['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
t=ybc_data.china_cities()
while True :
    xz = ybc_ui.picker_button('欢迎来到猿编程天气查询小程序',['查询','退出'])
    if xz == '查询':
        ybc_ui.message('欢迎来到 猿编程 天气查询小程序')
        f = ybc_ui.picker_button('请选择你想查询的城市',t)
        e = ybc_ui.picker_button('你想查询周几的天气呢？',r)    
        l = ybc_data.weather_week(f)
        if e == '星期一':
            s1 = l[4][0] + '天气预报' + '\n'
            s3 = '温度：' + l[4][3] + '\n'
            s4 = '天气：' + l[4][4] + '\n'
            s = s1 + s3 + s4
        elif e == '星期二':
            s1 = l[5][0] + '天气预报' + '\n'
            s3 = '温度：' + l[5][3] + '\n'
            s4 = '天气：' + l[5][4] + '\n'
            s = s1 + s3 + s4
        elif e == '星期三':
            s1 = l[6][0] + '天气预报' + '\n'
            s3 = '温度：' + l[6][3] + '\n'
            s4 = '天气：' + l[6][4] + '\n'
            s = s1 + s3 + s4
        elif e == '星期四':
            s1 = l[0][0] + '天气预报' + '\n'
            s3 = '温度：' + l[0][3] + '\n'
            s4 = '天气：' + l[0][4] + '\n'
            s = s1 + s3 + s4
        elif e == '星期五':
            s1 = l[1][0] + '天气预报' + '\n'
            s3 = '温度：' + l[1][3] + '\n'
            s4 = '天气：' + l[1][4] + '\n'
            s = s1 + s3 + s4
        elif e == '星期六':
            s1 = l[2][0] + '天气预报' + '\n'
            s3 = '温度：' + l[2][3] + '\n'
            s4 = '天气：' + l[2][4] + '\n'
            s = s1 + s3 + s4
        elif e == '星期天':
            s1 = l[3][0] + '天气预报' + '\n'
            s3 = '温度：' + l[3][3] + '\n'
            s4 = '天气：' + l[3][4] + '\n'

        ybc_ai.speak(s,10)
    elif  xz == '退出':
        break
