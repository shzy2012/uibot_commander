# coding = utf-8
import logging
import uibot


'''
定义work
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
    department_id = 276
    flow_id = 774
    worker_ids = [721]
    args = args

    print(x.create_task(department_id, flow_id, execute_type, assign_type,worker_ids,task_count,args,is_recording))

def worker_002(args):
    pass

'''
调度
'''
def scheduler(data):
    '''
    调用 uibot worker

    '''
    
    # 解析data
    params = data.split('$')
    workerNo = params[0]
    args = params[1]

    if workerNo == '001':
        worker_001(args)
        logging.info(f'call {workerNo}')

    elif workerNo == '002':
        worker_002(args)
        logging.info(f'call {workerNo}')

    else:
        pass

# 测试
if __name__ == "__main__":
    scheduler('001${"name":"aaa"}')



