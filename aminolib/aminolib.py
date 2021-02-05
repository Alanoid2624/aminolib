import json, base64
from . import objects
import websocket, requests
from time import time, sleep
from threading import Thread

deviceId = "015051B67B8D59D0A86E0F4A78F47367B749357048DD5F23DF275F05016B74605AAB0D7A6127287D9C"

class Socket:
    def __init__(self, client):
        self.socket = None
        self.workers = {"message": []}
        self.client = client
        self.url = "wss://ws1.narvii.com"
        Thread(target = self.reconnectSocket).start()

    def close(self):
        self.socket.close()
    def on_ping(self, data):
        self.socket.sock.pong(data)
    def on_message(self, data):
        self.message(data)
    def reconnectSocket(self): 
        while True: sleep(180); self.close(); self.start()

    def start(self):
        self.headers = {"NDCDEVICEID": deviceId, "NDCAUTH": f"sid={self.client.sid}"}
        self.socket = websocket.WebSocketApp(f"{self.url}/?signbody={deviceId}%7C{int(time() * 1000)}",
            on_message = self.on_message, on_ping = self.on_ping, header = self.headers)
        Thread(target = self.socket.run_forever, kwargs = {"ping_interval": 20}).start()
    
    def event(self):
        def registerHandler(handler):
            self.workers["message"].append(handler)
            return handler
        return registerHandler

    def message(self, data):
        data = objects.Event(json.loads(data)["o"]).Event
        comId = data.comId
        chatId = data.message.chatId
        message = data.message.content
        if self.client.prefix and message:
            if message.startswith(self.client.prefix):
                for handler in self.workers["message"]:
                    handler(data, comId=comId, chatId=chatId, message=message)
        else:
            for handler in self.workers["message"]:
                handler(data, comId=comId, chatId=chatId, message=message)

class Amino:
    def __init__(self, email, password, verify: bool = True, proxies: list = None):
        self.links_dict = {}
        self.prefix = None
        self.verify = verify
        self.proxies = proxies
        self.socket = Socket(self)
        self.api = "https://service.narvii.com/api/v1/"
        self.headers = {"Content-Type": "application/json; charset=utf-8"}

        data = json.dumps({"v": 2,"email": email,"secret":"0 "+password,"deviceID": deviceId,
        "clientType": 100,"action": "normal","timestamp": int(time() * 1000)})
        result = requests.post(self.api+"g/s/auth/login", data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        try: self.profile: objects.UserProfile = objects.UserProfile(result["userProfile"]).UserProfile
        except: self.profile = None

        try: self.sid = result["sid"]
        except: print(result['api:message'])
        try: self.auid = result["auid"]
        except: print(result['api:message'])

        self.socket.start()

    def set_prefix(self, prefix):
        self.prefix = str(prefix)
        return self

    def get_user_info(self, comId: str = None, userId: str = None):
        if comId is not None:
            result = requests.get(f"{self.api}/x{comId}/s/user-profile/{userId}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        else:
            result = requests.get(f"{self.api}g/s/user-profile/{userId}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return objects.UserProfile(result["userProfile"]).UserProfile

    def get_chat_thread(self, comId: str = None, chatId: str = None):
        if comId:
            result = requests.get(f"{self.api}x{comId}/s/chat/thread/{chatId}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        else:
            result = requests.get(f"{self.api}g/s/chat/thread/{chatId}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return objects.ChatThread(result["thread"]).ChatThread
        

    def get_user_threads(self, comId: str = None, start: int = 0, size: int = 100):
        if not comId:
            result = requests.get(f"{self.api}g/s/chat/thread?type=joined-me&start={start}&size={size}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        else:
            result = requests.get(f"{self.api}x{comId}/s/chat/thread?type=joined-me&start={start}&size={size}", 
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def get_message_info(self, comId: str = None, chatId: str = None, messageId: str = None):
        if comId:
            result = requests.get(f"{self.api}x{comId}/s/chat/thread/{chatId}/message/{messageId}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        else:
            result = requests.get(f"{self.api}g/s/chat/thread/{chatId}/message/{messageId}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def get_chat_messages(self, comId: str = None, chatId: str = None, size: int = 100):
        if comId:
            result = requests.get(f"{self.api}x{comId}/s/chat/thread/{chatId}/message?v=2&pagingType=t&size={size}&sid={self.sid}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        else:
            result = requests.get(f"{self.api}g/s/chat/thread/{chatId}/message?v=2&pagingType=t&size={size}&sid={self.sid}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def get_wallet_info(self):
        result = requests.get(f"{self.api}g/s/wallet?sid={self.sid}",
        verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def get_wallet_history(self, start: int = 0, size: int = 100):
        result = requests.get(f"{self.api}g/s/wallet/coin/history?start={start}&size={size}&sid={self.sid}",
        verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def get_from_code(self, code: str):
        result = requests.get(f"{self.api}g/s/link-resolution?q={code}",
        verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return objects.FromCode(result["linkInfoV2"]).FromCode

    def get_best_quizes(self, comId: str = None, start: int = 0, size: int = 25):
        result = requests.get(f"{self.api}x{comId}/s/feed/quiz-best-quizzes?start={start}&size={size}",
        verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return objects.BlogList(result["blogList"]).BlogList

    def get_blog_info(self, comId: str = None, blogId: str = None, quizId: str = None, wikiId: str = None):
        if blogId:
            result = requests.get(f"{self.api}x{comId}/s/blog/{blogId}", 
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
            return objects.GetBlogInfo(result).GetBlogInfo

        elif quizId:
            result = requests.get(f"{self.api}x{comId}/s/blog/{quizId}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
            return objects.GetBlogInfo(result).GetBlogInfo

        elif wikiId:
            result = requests.get(f"{self.api}x{comId}/s/item/{wikiId}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
            return result

    def get_community_info(self, comId: str):
        result = requests.get(f"{self.api}g/s-x{comId}/community/info?withInfluencerList=1&withTopicList=true&influencerListOrderStrategy=fansCount",
        verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return objects.Community(result["community"]).Community

    def join_community(self, comId: str):
        data = json.dumps({"timestamp": int(time() * 1000)})
        result = requests.post(f"{self.api}/x{comId}/s/community/join",
        data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result
    
    def leave_community(self, comId: str):
        result = requests.post(f"{self.api}/x{comId}/s/community/leave",
        verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result
    
    def get_user_followers(self, comId: str = None, userId: str = None, start: int = 0, size: int = 25):
        result = requests.get(f"{self.api}x{comId}/s/user-profile/{userId}/member?start={start}&size={size}",
        verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return objects.UserProfileList(result["userProfileList"]).UserProfileList

    def follow(self, comId: str = None, userId: [str, list] = None):
        if isinstance(userId, str):
            result = requests.post(f"{self.api}x{comId}/s/user-profile/{userId}/member", verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        elif isinstance(userId, list):
            data = json.dumps({"targetUidList": userId, "timestamp": int(time() * 1000)})
            result = requests.post(f"{self.api}x{comId}/s/user-profile/{self.profile.userId}/joined", data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def get_quiz_rankings(self, comId: str = None, quizId: str = None, start: int = 0, size: int = 25):
        result = requests.get(f"{self.api}x{comId}/s/blog/{quizId}/quiz/result?start={start}&size={size}",
        verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return objects.QuizRankings(result).QuizRankings

    def send_message(self, message: str, comId: str = None, chatId: str = None, replyTo: str = None, messageType: int = 0, mentionUserIds: list = None):
        mentions = []
        if mentionUserIds:
            for mention in mentionUserIds:
                mentions.append({"uid": mention})
        message = message.replace("<$", "‎‏").replace("$>", "‬‭")

        data = {"content": message, "type": messageType, "clientRefId": int(time() / 10 % 1000000000),
                "timestamp": (int(time() * 1000)), "extensions": {"mentionedArray": mentions}}

        if replyTo: data["replyMessageId"] = replyTo
        if comId:
            result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/message?sid={self.sid}", 
            data=json.dumps(data), verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        else:
            result = requests.post(f"{self.api}g/s/chat/thread/{chatId}/message?sid={self.sid}", 
            data=json.dumps(data), verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def send_file(self, file, comId: str = None, chatId: str = None):
        rfile = base64.b64encode(open(file, "rb").read())
        if ".gif" in file:
            data = json.dumps({"type": 0, "clientRefId": int(time() / 10 % 1000000000), "timestamp": (int(time() * 1000)), "mediaType": 100,
            "mediaUploadValue": rfile.strip().decode(), "mediaUploadValueContentType": "image/gif", "mediaUhqEnabled": False, "attachedObject": None})

        elif ".mp3" in file or ".wav" in file:
            data = json.dumps({"type": 2, "clientRefId": int(time() / 10 % 1000000000), "timestamp": int(time() * 1000), "mediaType": 110,
            "mediaUploadValue": rfile, "attachedObject": None, "content": None})

        elif ".jpg" in file or ".png" in file:
            data = json.dumps({"type": 0, "clientRefId": int(time() / 10 % 1000000000), "timestamp": (int(time() * 1000)), "mediaType": 100,
            "mediaUploadValue": rfile.strip().decode(), "mediaUploadValueContentType": "image/jpg", "mediaUhqEnabled": False, "attachedObject": None})
        else: data = None
        
        if comId:
            result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/message?sid={self.sid}",
            data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        else:
            result = requests.post(f"{self.api}g/s/chat/thread/{chatId}/message?sid={self.sid}",
            data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def edit_chat(self, comId: str = None, chatId: str = None, title: str = None, content: str = None, backgroundUrl: str = None, iconUrl: str = None, announcement: str = None, coHosts: list = None, viewOnly: bool = None, invites: bool = None, tips: bool = None):
        data = {"timestamp": int(time() * 1000)}
        if title: data["title"] = title
        if content: data["content"] = content
        if iconUrl: data["icon"] = iconUrl

        if announcement is not None:
            if announcement == "": data["extensions"] = {"announcement": announcement, "pinAnnouncement": False}
            else: data["extensions"] = {"announcement": announcement, "pinAnnouncement": True}

        if backgroundUrl is not None:
            result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/member/{self.profile.userId}/background",
            data=json.dumps({"media": [100, backgroundUrl, None], "timestamp": int(time() * 1000)}),
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
            return result

        if coHosts is not None:
            result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/co-host",
            data=json.dumps({"uidList": coHosts, "timestamp": int(time() * 1000)}),
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
            return result

        if viewOnly is not None:
            if viewOnly is True:
                result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/view-only/enable",
                data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()
                
            else:
                result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/view-only/disable",
                data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()
            return result

        if invites is not None:
            if invites is True:
                result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/members-can-invite/enable",
                data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()

            else:
                result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/members-can-invite/disable",
                data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()
            return result

        if tips is not None:
            if tips:
                result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/tipping-perm-status/enable",
                data=data, headers=self.headers, proxies=self.proxies, verify=self.verify).json()

            else:
                result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/tipping-perm-status/disable",
                data=data, headers=self.headers, proxies=self.proxies, verify=self.verify).json()
            return result

        result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}",
        data=json.dumps(data),vheaders=self.headers, proxies=self.proxies, verify=self.verify).json()
        return result
    
    def edit_profile(self, comId: str = None, nickname: str = None, content: str = None, icon: str = None, chatRequestPrivilege: str = None, mediaList: list = None, backgroundImage: str = None, backgroundColor: str = None):
        data = {"timestamp": int(time() * 1000)}
        if icon: data["icon"] = icon
        if content: data["content"] = content
        if nickname: data["nickname"] = nickname
        if mediaList: data["mediaList"] = mediaList
        if backgroundColor: data["extensions"] = {"style": {"backgroundColor": backgroundColor}}
        if chatRequestPrivilege: data["extensions"] = {"privilegeOfChatInviteRequest": chatRequestPrivilege}
        if backgroundImage: data["extensions"] = {"style": {"backgroundMediaList": [[100, backgroundImage, None, None, None]]}}
        if comId: result = requests.post(f"{self.api}x{comId}/s/user-profile/{self.profile.userId}", data=json.dumps(data), verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        else: result = requests.post(f"{self.api}g/s/user-profile/{self.profile.userId}", data=json.dumps(data), verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def join_chat(self, comId: str = None, chatId: str = None):
        if comId:
            result = requests.post(f"{self.api}x{comId}/s/chat/thread/{chatId}/member/{self.auid}?sid={self.sid}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        else:
            result = requests.post(f"{self.api}g/s/chat/thread/{chatId}/member/{self.auid}?sid={self.sid}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result
    
    # def start_chat(self, comId: str = None, userId: [str, list] = None, message: str = None, title: str = None, content: str = None):
    #     if isinstance(userId, list): userIds = userId
    #     elif isinstance(userId, str): userIds = [userId]
    #     else: pass

    #     data = {"title": title, "inviteeUids": userIds, "initialMessageContent": message,
    #     "content": content, "type": 0, "publishToGlobal": 0,"timestamp": int(time() * 1000)}
    #     result = requests.post(f"{self.api}x{comId}/s/chat/thread", data=json.dumps(data), verify=self.verify, headers=self.headers, proxies=self.proxies).json()
    #     return result
    def start_chat(self, comId: str = None, userId: [str, list] = None, message: str = None, title: str = None, content: str = None):
        pass

    def leave_chat(self, comId: str = None, chatId: str = None):
        if comId:
            result = requests.delete(f"{self.api}x{comId}/s/chat/thread/{chatId}/member/{self.auid}?sid={self.sid}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()

        else:
            result = requests.delete(f"{self.api}g/s/chat/thread/{chatId}/member/{self.auid}?sid={self.sid}",
            verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result

    def play_quiz(self, comId: None, quizId: str, questionIdsList: list, answerIdsList: list, quizMode: int = 0):
        answers = []

        for question, answer in zip(questionIdsList, answerIdsList):
            answers.append(json.loads(json.dumps({"optIdList": [answer], "quizQuestionId": question, "timeSpent": 0.0})))
        data = json.dumps({"mode": quizMode, "quizAnswerList": answers, "timestamp": int(time() * 1000)})
        result = requests.post(f"{self.api}/x{comId}/s/blog/{quizId}/quiz/result",
        data=data, verify=self.verify, headers=self.headers, proxies=self.proxies).json()
        return result