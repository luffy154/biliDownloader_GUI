import os
import re, json, webbrowser
from time import sleep
from PySide6.QtCore import QThread, Signal
from pathlib import Path
# 共享VIP Cookie预留（不使用请注释）
# import requests
# import req_encrypt as request

# 不使用共享VIP Cookie（不使用请取消注释）
import requests as request


############################################################################################
# 检查更新防阻滞线程类
class CheckLatest(QThread):
    _feedback = Signal(int)

    def __init__(self, in_ver, proxy=None):
        super(CheckLatest, self).__init__()
        self.lab_version = in_ver
        self.Proxy = proxy

    # 将版本号转变为数字可比较类型
    # @staticmethod
    # def ver2num(in_var):
    #     temp = in_var.replace("V", "").split(".")
    #     temp = int(temp[0] + temp[1] + temp[2])
    #     return temp

    # 最新版本检查
    @staticmethod
    def is_latest(my_ver: str, latest_ver: str) -> bool:
        try:
            my = my_ver.split(".")
            server = latest_ver.split(".")
            print("[INFO]BiliWorker.extra.CheckLatest.is_latest: My Version is {}, Latest Version is {}.".format(my, server))
            if int(my[0]) < int(server[0]):
                return False
            if int(my[1]) < int(server[1]):
                return False
            if int(my[2]) < int(server[2]):
                return False
            return True
        except Exception as e:
            print("[EXCEPTION]BiliWorker.extra.CheckLatest.is_latest:", e)
            return False

    def run(self):
        try:
            des = request.get(
                "https://jimmyliang-lzm.github.io/source_storage/biliDownloader_verCheck.json",
                timeout=5,
                proxies=self.Proxy
            )
            res = des.json()["BD_GUI_Ver"]
            if self.is_latest(self.lab_version, res):
                self._feedback.emit(0)
                sleep(2)
                self._feedback.emit(-1)
            else:
                self._feedback.emit(1)
                webbrowser.open("https://github.com/JimmyLiang-lzm/biliDownloader_GUI/releases/latest")
            # latestVer = ver2num(res)
            # myVer = ver2num(self.lab_version)
            # if latestVer <= myVer:
            #     self._feedback.emit(0)
            #     sleep(2)
            #     self._feedback.emit(-1)
            # else:
            #     self._feedback.emit(1)
            #     webbrowser.open("https://github.com/JimmyLiang-lzm/biliDownloader_GUI/releases/latest")
            #     sleep(2)
        except Exception as e:
            print("[EXCEPTION]BiliWorker.extra.CheckLatest.run:", e)
            self._feedback.emit(2)
            sleep(2)
            self._feedback.emit(-1)


############################################################################################
# 测试代理地址防阻滞线程类
class checkProxy(QThread):
    _feedback = Signal(dict)

    def __init__(self, in_Proxy, auth=None):
        super(checkProxy, self).__init__()
        self.use_Proxy = in_Proxy
        self.index_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/72.0.3626.121 Safari/537.36 "
        }
        self.Auth = auth
        if auth:
            from requests.auth import HTTPProxyAuth
            self.Auth = HTTPProxyAuth(auth.get('usr'), auth.get('pwd'))

    def run(self):
        try:
            temp = {"code": 1}
            des = request.get("https://api.live.bilibili.com/xlive/web-room/v1/index/getIpInfo",
                              headers=self.index_headers,
                              timeout=10,
                              stream=False,
                              proxies=self.use_Proxy,
                              auth=self.Auth
                              )
            res = json.loads(des.content.decode('utf-8'))["data"]
            temp["ip"] = res["addr"]
            temp["area"] = res["country"]
            self._feedback.emit(temp)
        except Exception as e:
            print("[EXCEPTION]BiliWorker.extra.checkProxy.run:", e)
            self._feedback.emit({"code": -1, "message": "测试失败"})


##############################################################################
# Bili交互视频处理总进程
class biliWorker_interact(QThread):
    # 信号发射定义
    business_info = Signal(str)
    rthread_status = Signal(dict)
    back_result = Signal(dict)

    # 初始化
    def __init__(self, args, model=0, parent=None):
        super(biliWorker_interact, self).__init__(parent)
        self.model = model
        self.index_url = args['Address']
        self.index_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/72.0.3626.121 Safari/537.36 "
        }
        self.re_playinfo = 'window.__playinfo__=([\s\S]*?)</script>'
        self.re_INITIAL_STATE = 'window.__INITIAL_STATE__=([\s\S]*?);\(function'
        if args["useCookie"]:
            self.index_headers["cookie"] = args["cookie"]
        else:
            self.index_headers["cookie"] = ""
        # 使用代理
        self.Proxy = None
        if args["useProxy"]:
            self.Proxy = args["Proxy"]
        # 若使用代理验证
        self.ProxyAuth = None
        if args["ProxyAuth"]["inuse"]:
            from requests.auth import HTTPProxyAuth
            self.ProxyAuth = HTTPProxyAuth(args['ProxyAuth']['usr'], args['ProxyAuth']['pwd'])
        self.iscache = args['imgcache']
        self.cache_path = args['cache_path'] + "/temp"
        # 初始化缓存图片下载类
        self.imgCache_module = BiliImgCache(args)

    ###################################################################
    # BiliDOwnloader基础功能
    # File name conflict replace
    def name_replace(self, name):
        vn = name.replace(' ', '_').replace('\\', '').replace('/', '')
        vn = vn.replace('*', '').replace(':', '').replace('?', '').replace('<', '')
        vn = vn.replace('>', '').replace('\"', '').replace('|', '').replace('\x08', '')
        return vn

    ###################################################################
    # 交互进程初始数据获取函数
    def interact_preinfo(self):
        self.now_interact = {"cid": "", "bvid": "", "session": "", "graph_version": "", "node_id": "", "vname": ""}
        t1 = self.Get_Init_Info(self.index_url)
        if t1[0]:
            return 1, {}, {}
        self.index_headers['referer'] = self.index_url
        self.second_headers = self.index_headers
        t2 = self.isInteract()
        if t2[0]:
            return 1, {}, {}
        print("[INFO]BiliWorker.extra.biliWorker_interact.interact_preinfo:", self.now_interact)
        t3 = self.Get_Edge()
        if t3[0]:
            return 1, {}, {}
        return 0, self.now_interact, t3[1]

    # 改变线程运行模式
    def change_method(self, mode: int, **kwargs):
        # 单节点探查模式
        self.model = mode
        if mode == 1:
            if not kwargs.get('node_id'):
                return False
            self.now_interact['node_id'] = kwargs.get('node_id')
            self.iscache = kwargs.get('img_cache')
            return True
        # 递归探查模式
        elif mode == 2:
            nid = kwargs.get('cur_node_id')
            deep = kwargs.get('deep')
            if not deep:
                return False
            self.recur_deep = 0
            if deep < 0:
                self.unlimited_recur = True
            elif deep > 0:
                self.unlimited_recur = False
                self.recur_deep = deep
            else:
                return False
            self.recur_run = False
            self.now_interact['node_id'] = nid
            return True
        else:
            return False

    # 交互视频节点分析函数
    # def interact_nodeList(self):
    #     self.business_info.emit("开始分析互动视频节点，若长时间（10分钟）未弹出画面说明互动视频存在循环或进程坏死，请退出本程序...")
    #     self.business_info.emit(
    #         "-----------------------------------------------------------------------------------------")
    #     self.now_interact = {"cid": "", "bvid": "", "session": "", "graph_version": "", "node_id": "", "vname": ""}
    #     if self.Get_Init_Info(self.index_url) != 0:
    #         return -1
    #     self.index_headers['referer'] = self.index_url
    #     self.second_headers = self.index_headers
    #     if self.isInteract() != 0:
    #         return -1
    #     self.iv_structure = {}
    #     self.iv_structure[self.now_interact["vname"]] = {}
    #     self.iv_structure[self.now_interact["vname"]] = self.recursion_GET_List("初始节点")
    #     self.business_info.emit("节点探查完毕，窗口加载中...")
    #     return self.iv_structure

    # Interactive video initial information
    def Get_Init_Info(self, url):
        try:
            res = request.get(
                url,
                headers=self.index_headers,
                stream=False,
                timeout=10,
                proxies=self.Proxy,
                auth=self.ProxyAuth
            )
            dec = res.content.decode('utf-8')
            playinfo = re.findall(self.re_playinfo, dec, re.S)
            INITIAL_STATE = re.findall(self.re_INITIAL_STATE, dec, re.S)
            if playinfo == [] or INITIAL_STATE == []:
                raise Exception("无法找到初始化信息。")
            playinfo = json.loads(playinfo[0])
            INITIAL_STATE = json.loads(INITIAL_STATE[0])
            self.now_interact["session"] = playinfo["session"]
            self.now_interact["bvid"] = INITIAL_STATE["bvid"]
            self.now_interact["cid"] = str(INITIAL_STATE["cidMap"][INITIAL_STATE["bvid"]]["cids"]["1"])
            self.now_interact["vname"] = self.name_replace(INITIAL_STATE["videoData"]["title"])
            return 0, ""
        except Exception as e:
            return 1, str(e)

    # Judge the interactive video.
    def isInteract(self):
        make_API = "https://api.bilibili.com/x/player/v2"
        param = {
            'cid': self.now_interact["cid"],
            'bvid': self.now_interact["bvid"],
        }
        try:
            res = request.get(
                make_API,
                headers=self.index_headers,
                params=param,
                timeout=10,
                proxies=self.Proxy,
                auth=self.ProxyAuth
            )
            des = res.json()
            if "interaction" not in des["data"]:
                raise Exception("非交互视频")
            self.now_interact["graph_version"] = str(des["data"]["interaction"]["graph_version"])
            return 0, ""
        except Exception as e:
            return 1, str(e)

    # Edge Choose Search
    def Get_Edge(self):
        temp = {}
        make_API = "https://api.bilibili.com/x/stein/nodeinfo"
        param = {
            'bvid': self.now_interact["bvid"],
            'graph_version': self.now_interact["graph_version"],
            'node_id': self.now_interact["node_id"],
        }
        try:
            des = request.get(
                make_API,
                headers=self.index_headers,
                params=param,
                timeout=10,
                proxies=self.Proxy,
                auth=self.ProxyAuth
            )
            res = des.json()
        except Exception as e:
            print("[EXCEPTION]BiliWorker.extra.biliWorker_interact.Get_Edge:", e)
            return 1, "获取节点失败（网络连接错误）"
        # print(res)
        if "edges" not in res["data"]:
            return 0, temp
        for ch in res["data"]["edges"]["choices"]:
            temp[ch["option"]] = {}
            temp[ch["option"]]["cid"] = str(ch["cid"])
            temp[ch["option"]]["node_id"] = str(ch["node_id"])
            temp[ch["option"]]["isChoose"] = False
            if self.iscache:
                self.imgCache_module.img_cache(temp[ch["option"]]["cid"])
                # self.img_cache(temp[ch["option"]]["cid"])
        return 0, temp

    # 交互视频节点分析函数
    def interact_nodeList(self):
        self.business_info.emit("开始分析互动视频节点，若长时间（10分钟）未弹出画面说明互动视频存在循环或进程坏死，请退出本程序...")
        self.business_info.emit(
            "-----------------------------------------------------------------------------------------")
        # self.now_interact = {"cid": "", "bvid": "", "session": "", "graph_version": "", "node_id": "", "vname": ""}
        # self.Get_Init_Info(self.index_url)
        # self.index_headers['referer'] = self.index_url
        # self.second_headers = self.index_headers
        # self.isInteract()
        self.now_deep = 0
        self.recur_run = True
        iv_structure = {}
        # iv_structure[self.now_interact["vname"]] = {}
        iv_structure = self.recursion_GET_List('当前节点')
        self.business_info.emit("节点探查完毕!!")
        return iv_structure

    # Get interactive video node list (Use recursion algorithm)
    def recursion_GET_List(self, inword):
        temp = {
            "cid": self.now_interact["cid"],
            "node_id": self.now_interact["node_id"],
            "isChoose": False
        }
        if (self.now_deep <= self.recur_deep or self.unlimited_recur) and self.recur_run:
            temp["choices"] = {}
            make_API = "https://api.bilibili.com/x/stein/nodeinfo"
            param = {
                'bvid': self.now_interact["bvid"],
                'graph_version': self.now_interact["graph_version"],
                'node_id': self.now_interact["node_id"],
            }
            try:
                des = request.get(
                    make_API,
                    headers=self.index_headers,
                    params=param,
                    timeout=10,
                    proxies=self.Proxy,
                    auth=self.ProxyAuth
                )
                desp = des.json()
            except Exception as e:
                self.business_info.emit("获取节点信息出现网络问题：节点提取可能不全")
                print("[EXCEPTION]BiliWorker.extra.biliWorker_interact.recursion_GET_List:", e)
                return temp
            if "edges" not in desp["data"]:
                return temp
            for ch in desp["data"]["edges"]["choices"]:
                self.now_interact["cid"] = str(ch["cid"])
                self.now_interact["node_id"] = str(ch["node_id"])
                self.now_deep += 1
                self.business_info.emit(inword + " --> " + ch["option"])
                self.rthread_status.emit(
                    {
                        'code': 0,
                        'deep': self.now_deep,
                        'node_name': ch["option"],
                        'node_id': self.now_interact["node_id"],
                    }
                )
                temp["choices"][ch["option"]] = self.recursion_GET_List(inword + " --> " + ch["option"])
                self.now_deep -= 1
        return temp

    # Shutdown Recursion Thread
    def kill_rthread(self):
        self.recur_run = False

    # Start Worker Thread
    def run(self) -> None:
        if self.model == 0:
            res = self.interact_preinfo()
            if res[0]:
                self.back_result.emit({'code': -1, 'data': '获取初始信息失败'})
            self.back_result.emit({'code': 0, 'data': res[1], 'nodelist': res[2]})
        elif self.model == 1:
            res = self.Get_Edge()
            if res[0]:
                self.back_result.emit({'code': -1, 'data': '获取节点信息失败'})
            self.back_result.emit({'code': 1, 'nodelist': res[1]})
        elif self.model == 2:
            d = self.interact_nodeList()
            if 'choices' in d:
                self.rthread_status.emit({'code': 1, 'node_dict': d['choices']})
            else:
                self.rthread_status.emit({'code': -1, 'data': '为探查到更多节点。'})
        else:
            print("[INFO]BiliWorker.extra.biliWorker_interact.run: Operation Command Error", self.model)
            self.back_result.emit({'code': -1, 'data': '操作指令有误'})


##############################################################################
# Bili交互视频图片缓存线程
class BiliImgCache(QThread):
    # 初始化缓存对象
    def __init__(self, req_dict: dict):
        super(BiliImgCache, self).__init__()
        # 初始化requests参数
        self.index_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/72.0.3626.121 Safari/537.36 ", "cookie": ""}
        if req_dict["useCookie"]:
            self.index_headers["cookie"] = req_dict["cookie"]
        # 使用代理
        self.Proxy = None
        if req_dict["useProxy"]:
            self.Proxy = req_dict["Proxy"]
        # 若使用代理验证
        self.ProxyAuth = None
        if req_dict["ProxyAuth"]["inuse"]:
            from requests.auth import HTTPProxyAuth
            self.ProxyAuth = HTTPProxyAuth(req_dict['ProxyAuth']['usr'], req_dict['ProxyAuth']['pwd'])
        self.cache_path = req_dict['cache_path'] + "/temp"
        # 初始化递归字典
        self.recur_dict = {}
        self.busy = False

    # 设置递归字典
    def setRecurDict(self, indic: dict):
        self.recur_dict = indic

    # 递归字典转数组主程序
    def recur_dict2list(self, indic: dict, savelist: list):
        for ch in indic:
            savelist.append(indic[ch]['cid'])
            if "choices" in indic[ch]:
                savelist = self.recur_dict2list(indic[ch]['choices'], savelist)
        return savelist

    # 缓存输出主程序
    def img_cache(self, cid):
        url = "https://i0.hdslb.com/bfs/steins-gate/" + cid + "_screenshot.jpg"
        if not os.path.exists(self.cache_path):
            os.makedirs(self.cache_path)
        output_file = self.cache_path + "/" + cid + "_node.jpg"
        if Path(output_file).is_file():
            return 0
        try:
            res = request.get(
                url,
                headers=self.index_headers,
                timeout=10,
                proxies=self.Proxy,
                auth=self.ProxyAuth
            )
            file = res.content
            with open(output_file, 'wb') as f:
                f.write(file)
            return 0
        except Exception as e:
            self.business_info.emit("附带下载失败：{}".format(url))
            print("[EXCEPTION]BiliWorker.extra.BiliImgCache.img_cache:", e)
            return 1

    # 运行自动缓存系统
    def runAutoImgCache(self):
        cache_cid_list = self.recur_dict2list(self.recur_dict, [])
        for cid in cache_cid_list:
            self.img_cache(cid)

    # 主线程启动
    def run(self) -> None:
        self.busy = True
        self.runAutoImgCache()
        self.busy = False
