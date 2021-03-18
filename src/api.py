# coding = utf-8
import logging
import uibot
from flask import Flask,request
app = Flask(__name__)


'''
定义RPA work
'''
def worker_001(args):
    x = uibot.UiBotAPI()
    '''参数'''
    
    # 功能参数
    execute_type = 1 #执行方式，1立即执行，2排队执行
    assign_type = 2  #分配方式，1自动分配，2指定Worker
    is_recording = 1 #是否录屏，1录屏，2不录屏，若不传，则使用默认配置
    task_count = 1   #若分配方式为自动分配，则必填，最大值为100，最小值为1

    # 流程参数
    department_id = 879
    flow_id = 959
    worker_ids = [1320]
    # args = args

    print(x.create_task(department_id, flow_id, execute_type, assign_type,worker_ids,task_count,args,is_recording))
    print(x.push_queue("this_queue_for_123",args))

'''
定义 api 接口
'''

# 测试
@app.route('/')
def index():
    return {"status":"i am working"}

# 吾来webhook
@app.route('/webhook')
def hello_world():
    # 获取参数
    p = request.args.get('p')
    # print(p)
    worker_001(p)

    # 返回结果
    response = {"slot_values": [ "ok"],"responses": []}
    return response


# 测试
if __name__ == "__main__":
    worker_001('{"cmd":"来也科技"}')




