# coding = utf-8
import time
from hashlib import sha256
import hmac
import requests
from datetime import datetime
import random
import string
import re
import logging
import traceback

class UiBotAPI:

    def __init__(self):
        self.access_token = None  # 访问令牌
        self.server_url = None  # Commander服务器url
        self.ak_id = None  # Access Key ID
        self.ak_secret = None  # Access Key Secret
        self.token_timestamp = None  # 令牌时间戳
        self.token_timeout = None  # 令牌过期时间

        # 初始化
        self.set_auth('https://commander.uibot.com.cn///','ffdc71480dc34898b8c679eddc3b7178', '2d64a893c6c5404e834c26f6e711f923')
        self.set_log_config()
    
    def set_auth(self,url: str, id: str, secret: str):
        """
        设置授权信息

        :param url: Commander服务器url
        :param id: Access Key ID
        :param secret: Access Key Secret
        """
        # 去url末尾斜杠
        self.server_url = re.sub('/+$', '', url)
        self.ak_id = id
        self.ak_secret = secret


    def get_department_id(self,id: int = 0) -> dict:
        """
        获取部门ID

        :param: id: 父部门ID
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/department/get'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'departmentId': id}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def create_department(self,id: int, name: str) -> dict:
        """
        创建部门

        :param: id: 父部门ID
        :param: name: 部门名称
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/department/create'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'parentId': id, 'name': name}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def update_department(self,id: int, name: str) -> dict:
        """
        修改部门

        :param: id: 部门ID
        :param: name: 部门名称
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/department/update'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'id': id, 'name': name}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def get_department_user(self,id: int) -> dict:
        """
        根据部门Id获取部门下的用户列表

        :param: id: 部门ID
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/user/getByDepartmentId'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'departmentId': id}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def get_department_flow(self,id: int) -> dict:
        """
        根据部门Id获取流程

        :param: id: 部门ID
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/flow/getByDepartmentId'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'departmentId': id}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def get_department_worker(self,id: int) -> dict:
        """
        根据部门Id获取无人值守Worker

        :param: id: 部门ID
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/worker/getByDepartmentId'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'departmentId': id}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def create_worker(self,ids: tuple, name: str, auth_type: int, is_accept: int) -> dict:
        """
        创建无人值守Worker

        :param: ids: 授权部门ID列表
        :param: name: Worker名称
        :param: auth_type: 授权类型 1绑定机器 2浮动授权
        :param: is_accept: 是否接收任务 1接收 2不接收
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/worker/create'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'departmentIds': ids, 'name': name, 'authType': auth_type, 'isAccept': is_accept}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def update_worker(self,id: int, ids: tuple, name: str, is_accept: int) -> dict:
        """
        修改无人值守Worker

        :param: id: WorkerID
        :param: ids: 授权部门ID列表
        :param: name: Worker名称
        :param: is_accept: 是否接收任务 1接收 2不接收
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/worker/update'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'id': id, 'departmentIds': ids, 'name': name, 'isAccept': is_accept}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def get_argument(self,name: str) -> dict:
        """
        根据参数名获取参数

        :param: name: 参数名
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/parameter/get'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'name': name}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def set_argument(self,name: str, type: int, value) -> dict:
        """
        设置参数

        :param: name: 参数名
        :param: type: 参数类型,10 文本,20 数值,30 布尔
        :param: value: 参数值,不同类型参数值范围不一样,文本类型：0-65535个字符,数值类型：-65535~65536(小数保留3位),布尔类型：true或false
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/parameter/set'
            return requests.post(url, params={'accessToken': self.access_token}, json={
                'name': name, 'type': type, 'value': value}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def delete_argument(self,name: str) -> dict:
        """
        删除参数

        :param: name: 参数名
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/parameter/delete'
            return requests.post(url, params={'accessToken': self.access_token}, json={'name': name}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def create_queue(self,name: str) -> dict:
        """
        创建数据队列

        :param: name: 数据队列名 2-30个字符
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/queue/create'
            return requests.post(url, params={'accessToken': self.access_token}, json={'name': name}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def push_queue(self,name: str, data: str, t1: int = 0, t2: int = 2592000000) -> dict:
        """
        数据加入数据队列

        :param: name: 数据队列名 2-30个字符
        :param: data: 数据，必须是字符串，长度为0-1000个字符
        :param: t1: 生效时间，以当前时间向后推算的毫秒数，默认为0，取值范围为0~2592000000（30天）
        :param: t2: 生效时间，以当前时间向后推算的毫秒数，默认为2592000000（30天），取值范围为0~2592000000（30天）
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/queue/enqueue'
            return requests.post(url, params={'accessToken': self.access_token}, json={'name': name, 'data': data, 'availableTime': t1, 'expiredTime': t2}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def pull_queue(self,name: str) -> dict:
        """
        从数据队列中拉取数据

        :param: name: 数据队列名 2-30个字符
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/queue/dequeue'
            return requests.post(url, params={'accessToken': self.access_token}, json={'name': name}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def create_task(self,department_id: int, flow_id: int, execute_type: int, assign_type: int, worker_ids: tuple = None, task_count: int = 1, args: str = "{}", is_recording: int = 1) -> dict:
        """
        创建任务

        :param: department_id: 部门Id
        :param: flow_id: 流程Id
        :param: execute_type: 执行方式，1立即执行，2排队执行
        :param: assign_type: 分配方式，1自动分配，2指定Worker
        :param: worker_ids: WorkerID列表若分配方式为指定Worker，则必填
        :param: task_count: 任务数量，若分配方式为自动分配，则必填，最大值为100，最小值为1
        :param: args: 任务参数，必须为Json字符串，最长1000个字符
        :param: is_recording: 是否录屏，1录屏，2不录屏，若不传，则使用默认配置
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/task/create'
            json = {'departmentId': department_id, 'flowId': flow_id, 'executeType': execute_type, 'assignType': assign_type, 'workerIds': worker_ids, 'taskCount': task_count, 'args': args, 'isRecording': is_recording}
            return requests.post(url, params={'accessToken': self.access_token}, json=json).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def get_task_status(self,id: int) -> dict:
        """
        根据任务Id查询任务状态

        :param: id: 任务Id
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/task/getStatusById'
            return requests.post(url, params={'accessToken': self.access_token}, json={'taskId': id}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def stop_task(self,id: int) -> dict:
        """
        停止任务

        :param: id: 任务Id
        """
        try:
            self.get_token()
            url = self.server_url + '/open/commander/task/stopById'
            return requests.post(url, params={'accessToken': self.access_token}, json={'taskId': id}).json()
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


    def set_log_config(self,level=30, filepath=None, format='%(asctime)s - %(levelname)s - %(message)s'):
        """
        配置日志

        :param: level: 日志等级，调试、信息、警告、错误、严重错误（10、20、30、40、50）
        :param: filepath: 日志文件路径，默认无日志文件
        :param: format: 日志输出格式，默认打印日志时间、等级、信息
        """
        logging.basicConfig(level=level, format=format, filename=filepath)
        return


    def get_token(self) -> str:
        """
        获取访问令牌，令牌过期则重新获取

        :returns: AccessToken
        """
        try:
            # 令牌没过期跳过
            if self.access_token is not None:
                if round(time.time()) - self.token_timestamp < self.token_timeout:
                    return self.access_token
            # 生成时间戳
            self.token_timestamp = round(time.time())
            # 生成1-30位随机字符串
            nonce = ''.join(random.sample(string.ascii_letters +
                                        string.digits, random.randint(1, 30)))
            # 拼接url、id、secret，得到编码为UTF8的字节数组
            message = (self.ak_secret + str(self.token_timestamp) + nonce).encode('utf-8')
            # 签名(sha256加密)
            sign = hmac.new(self.ak_secret.encode('utf-8'), message,
                            digestmod=sha256).hexdigest()
            url = self.server_url + '/open/commander/common/getAccessToken'
            r = requests.get(url, params={
                'accessKeyId': self.ak_id, 'timestamp': self.token_timestamp, 'nonce': nonce, 'sign': sign}).json()
            self.token_timeout = r['data']['expiredTime']
            self.access_token = r['data']['accessToken']
            return self.access_token
        except Exception as e:
            logging.error(traceback.format_exc())
            return str(e)


if __name__ == "__main__":
    # set_auth('https://commander.uibot.com.cn///',
    #          '7f0aef423e364563bc2969e5053f7902', 'c9e60b6fb89f4d998a26801c76015167')
    # set_log_config()
    # print(get_department_id(1))
    # print(get_token())
    # print(create_department(1, "测试用"))
    # print(update_department(220, "测试测试测试"))
    # print(get_department_user(1))
    # print(get_department_flow(20))
    # print(get_department_worker(20))
    # print(create_worker([1],"测测测",2,1))
    # print(update_worker(438,[1],"测测",2))
    # print(get_argument("培训演示"))
    # print(set_argument("培训演示", 10, " s"))
    # print(create_queue("测测测"))
    # print(push_queue("测测测","sss"))
    # print(pull_queue("测测测"))
    # print(create_task(276, 774, 2, 1))
    # print(get_task_status(2021031000000310))
    # print(stop_task(2020101000000127))
    
    ''' class  '''
    x = UiBotAPI()
    # print(x.create_task(276, 774, 2, 1)) 
    # print(x.get_task_status(2021031000000310))
    # print(x.get_department_id(0))
    # print(x.get_token())
    # print(x.create_department(1, "测试用"))
    # print(x.update_department(220, "测试测试测试"))
    # print(x.get_department_user(879))
    # print(x.get_department_flow(879))
    # print(x.get_department_worker(879))
    # print(x.create_worker([1],"测测测",2,1))
    # print(x.update_worker(438,[1],"测测",2))
    # print(x.get_argument("培训演示"))
    # print(x.set_argument("培训演示", 10, " s"))
    # print(x.create_queue("this_queue_for_123"))
    print(x.push_queue("this_queue_for_123","来也科技"))
    # print(x.pull_queue("测测测"))
    # print(x.create_task(276, 774, 2, 1))
    # print(x.get_task_status(2021031000000310))
    # print(x.stop_task(2020101000000127))