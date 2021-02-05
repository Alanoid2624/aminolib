class UserProfile:
    def __init__(self, data):
        self.data = data
    
    @property
    def UserProfile(self):
        try: self.status = self.data["status"]
        except: self.status = None
        try: self.moodSticker = self.data["moodSticker"]
        except: self.moodSticker = None
        try: self.itemsCount = self.data["itemsCount"]
        except: self.itemsCount = None
        try: self.checkInDays = self.data["consecutiveCheckInDays"]
        except: self.checkInDays = None
        try: self.userId = self.data["uid"]
        except: self.userId = None
        try: self.modifiedTime = self.data["modifiedTime"]
        except: self.modifiedTime = None
        try: self.followingStatus = self.data["followingStatus"]
        except: self.followingStatus = None
        try: self.onlineStatus = self.data["onlineStatus"]
        except: self.onlineStatus = None
        try: self.accountMembershipStatus = self.data["accountMembershipStatus"]
        except: self.accountMembershipStatus = None
        try: self.isGlobal = self.data["isGlobal"]
        except: self.isGlobal = None
        try: self.avatarFrameId = self.data["avatarFrameId"]
        except: self.avatarFrameId = None
        try: self.fanClubList = self.data["fanClubList"]
        except: self.fanClubList = None
        try: self.reputation = self.data["reputation"]
        except: self.reputation = None
        try: self.postsCount = self.data["postsCount"]
        except: self.postsCount = None
        try: self.avatarFrame = self.data["avatarFrame"]
        except: self.avatarFrame = None
        try: self.frameStatus = self.data["avatarFrame"]["status"]
        except: self.frameStatus = None
        try: self.ownershipStatus = self.data["avatarFrame"]["ownershipStatus"]
        except: self.ownershipStatus = None
        try: self.frameVersion = self.data["avatarFrame"]["version"]
        except: self.frameVersion = None
        try: self.frameResourceUrl = self.data["avatarFrame"]["resourceUrl"]
        except: self.frameResourceUrl = None
        try: self.frameName = self.data["avatarFrame"]["name"]
        except: self.frameName = None
        try: self.frameUrl = self.data["avatarFrame"]["icon"]
        except: self.frameUrl = None
        try: self.frameType = self.data["avatarFrame"]["frameType"]
        except: self.frameType = None
        try: self.frameId = self.data["avatarFrame"]["frameId"]
        except: self.frameId = None
        try: self.followersCount = self.data["membersCount"]
        except: self.followersCount = None
        try: self.nickname = self.data["nickname"]
        except: self.nickname = None
        try: self.mediaList = self.data["mediaList"]
        except: self.mediaList = []
        try: self.avatarUrl = self.data["icon"]
        except: self.avatarUrl = None
        try: self.isNicknameVerified = self.data["isNicknameVerified"]
        except: self.isNicknameVerified = None
        try: self.visitorsCount = self.data["visitorsCount"]
        except: self.visitorsCount = None
        try: self.mood = self.data["mood"]
        except: self.mood = None
        try: self.level = self.data["level"]
        except: self.level = None
        try: self.notificationSubscriptionStatus = self.data["notificationSubscriptionStatus"]
        except: self.notificationSubscriptionStatus = None
        try: self.pushEnabled = self.data["pushEnabled"]
        except: self.pushEnabled = None
        try: self.membershipStatus = self.data["membershipStatus"]
        except: self.membershipStatus = None
        try: self.content = self.data["content"]
        except: self.content = None
        try: self.followingCount = self.data["joinedCount"]
        except: self.followingCount = None
        try: self.role = self.data["role"]
        except: self.role = None
        try: self.commentsCount = self.data["commentsCount"]
        except: self.commentsCount = None
        try: self.ndcId = self.data["ndcId"]
        except: self.ndcId = None
        try: self.createdTime = self.data["createdTime"]
        except: self.createdTime = None
        try: self.extensions = self.data["extensions"]
        except: self.extensions = None
        try: self.defaultBubbleId = self.data["extensions"]["defaultBubbleId"]
        except: self.defaultBubbleId = None
        try: self.extensionsStyle = self.data["extensions"]["style"]
        except: self.extensionsStyle = None
        try: self.styleBackgroundColor = self.data["extensions"]["style"]["backgroundColor"]
        except: self.styleBackgroundColor = None
        try: self.visitPrivacy = self.data["visitPrivacy"]
        except: self.visitPrivacy = None
        try: self.storiesCount = self.data["storiesCount"]
        except: self.storiesCount = None
        try: self.blogsCount = self.data["blogsCount"]
        except: self.blogsCount = None
        return self

class UserProfileList:
    def __init__(self, data):
        self.data = data

        self.accountMembershipStatus = []
        self.avatarFrame = []
        self.avatarFrameId = []
        self.backgroundColor = []
        self.backgroundImage = []
        self.blogsCount = []
        self.commentsCount = []
        self.content = []
        self.createdTime = []
        self.customTitles = []
        self.defaultBubbleId = []
        self.extensions = []
        self.followersCount = []
        self.followingCount = []
        self.followingStatus = []
        self.icon = []
        self.isGlobal = []
        self.isNicknameVerified = []
        self.itemsCount = []
        self.level = []
        self.mediaList = []
        self.membershipStatus = []
        self.modifiedTime = []
        self.mood = []
        self.moodSticker = []
        self.nickname = []
        self.notificationSubscriptionStatus = []
        self.onlineStatus = []
        self.postsCount = []
        self.pushEnabled = []
        self.reputation = []
        self.role = []
        self.status = []
        self.storiesCount = []
        self.userId = []
        self.visitPrivacy = []
        self.visitorsCount = []
        self.warningCount = []

    @property
    def UserProfileList(self):
        for x in self.data:
            try: self.accountMembershipStatus.append(x["accountMembershipStatus"])
            except: self.accountMembershipStatus.append(None)
            try: self.avatarFrame.append(x["avatarFrame"])
            except: self.avatarFrame.append(None)
            try: self.avatarFrameId.append(x["avatarFrameId"])
            except: self.avatarFrameId.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except: self.backgroundColor.append(None)
            try: self.backgroundImage.append(x["extensions"]["style"]["backgroundMediaList"][1])
            except: self.backgroundImage.append(None)
            try: self.blogsCount.append(x["blogsCount"])
            except: self.blogsCount.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except: self.commentsCount.append(None)
            try: self.content.append(x["content"])
            except: self.content.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.customTitles.append(x["extensions"]["customTitles"])
            except: self.customTitles.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.followersCount.append(x["membersCount"])
            except: self.followersCount.append(None)
            try: self.followingCount.append(x["joinedCount"])
            except: self.followingCount.append(None)
            try: self.followingStatus.append(x["followingStatus"])
            except: self.followingStatus.append(None)
            try: self.icon.append(x["icon"])
            except: self.icon.append(None)
            try: self.isGlobal.append(x["isGlobal"])
            except: self.isGlobal.append(None)
            try: self.isNicknameVerified.append(x["isNicknameVerified"])
            except: self.isNicknameVerified.append(None)
            try: self.itemsCount.append(x["itemsCount"])
            except: self.itemsCount.append(None)
            try: self.level.append(x["level"])
            except: self.level.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.membershipStatus.append(x["membershipStatus"])
            except: self.membershipStatus.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.mood.append(x["mood"])
            except: self.mood.append(None)
            try: self.moodSticker.append(x["moodSticker"])
            except: self.moodSticker.append(None)
            try: self.nickname.append(x["nickname"])
            except: self.nickname.append(None)
            try: self.notificationSubscriptionStatus.append(x["notificationSubscriptionStatus"])
            except: self.notificationSubscriptionStatus.append(None)
            try: self.onlineStatus.append(x["onlineStatus"])
            except: self.onlineStatus.append(None)
            try: self.postsCount.append(x["postsCount"])
            except: self.postsCount.append(None)
            try: self.pushEnabled.append(x["pushEnabled"])
            except: self.pushEnabled.append(None)
            try: self.reputation.append(x["reputation"])
            except: self.reputation.append(None)
            try: self.role.append(x["role"])
            except: self.role.append(None)
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.storiesCount.append(x["storiesCount"])
            except: self.storiesCount.append(None)
            try: self.userId.append(x["uid"])
            except: self.userId.append(None)
            try: self.visitPrivacy.append(x["visitPrivacy"])
            except: self.visitPrivacy.append(None)
            try: self.visitorsCount.append(x["visitorsCount"])
            except: self.visitorsCount.append(None)
            try: self.warningCount.append(x["adminInfo"]["warningCount"])
            except: self.warningCount.append(None)
        return self

class Blog:
    def __init__(self, data):
        self.data = data

    @property
    def Blog(self):
        try: self.author: UserProfile = UserProfile(self.data["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([])
        try: self.quizQuestionList: QuizQuestionList = QuizQuestionList(self.data["quizQuestionList"]).QuizQuestionList
        except: self.quizQuestionList: QuizQuestionList = QuizQuestionList([])
        try: self.globalVotesCount = self.data["globalVotesCount"]
        except: self.globalVotesCount = None
        try: self.globalVotedValue = self.data["globalVotedValue"]
        except: self.globalVotedValue = None
        try: self.keywords = self.data["keywords"]
        except: self.keywords = None
        try: self.mediaList = self.data["mediaList"]
        except: self.mediaLis = None
        try: self.style = self.data["style"]
        except: self.style = None
        try: self.totalQuizPlayCount = self.data["totalQuizPlayCount"]
        except: self.totalQuizPlayCount = None
        try: self.title = self.data["title"]
        except: self.title = None
        try: self.tipInfo = self.data["tipInfo"]
        except: self.tipInfo = None
        try: self.tippersCount = self.data["tipInfo"]["tippersCount"]
        except: self.tippersCount = None
        try: self.tippable = self.data["tipInfo"]["tippable"]
        except: self.tippable = None
        try: self.tippedCoins = self.data["tipInfo"]["tippedCoins"]
        except: self.tippedCoins = None
        try: self.contentRating = self.data["contentRating"]
        except: self.contentRating = None
        try: self.needHidden = self.data["needHidden"]
        except: self.needHidden = None
        try: self.guestVotesCount = self.data["guestVotesCount"]
        except: self.guestVotesCount = None
        try: self.type = self.data["type"]
        except: self.type = None
        try: self.status = self.data["status"]
        except: self.status = None
        try: self.globalCommentsCount = self.data["globalCommentsCount"]
        except: self.globalCommentsCount = None
        try: self.modifiedTime = self.data["modifiedTime"]
        except: self.modifiedTime = None
        try: self.widgetDisplayInterval = self.data["widgetDisplayInterval"]
        except: self.widgetDisplayInterval = None
        try: self.totalPollVoteCount = self.data["totalPollVoteCount"]
        except: self.totalPollVoteCount = None
        try: self.blogId = self.data["blogId"]
        except: self.blogId = None
        try: self.comId = self.data["ndcId"]
        except: self.comId = None
        try: self.viewCount = self.data["viewCount"]
        except: self.viewCount = None
        try: self.shareUrl = self.data["shareURLFullPath"]
        except: self.shareUrl = None
        try: self.fansOnly = self.data["extensions"]["fansOnly"]
        except: self.fansOnly = None
        try: self.backgroundColor = self.data["extensions"]["style"]["backgroundColor"]
        except: self.backgroundColor = None
        try: self.votesCount = self.data["votesCount"]
        except: self.votesCount = None
        try: self.endTime = self.data["endTime"]
        except: self.endTime = None
        try: self.refObjectId = self.data["refObjectId"]
        except: self.refObjectId = None
        try: self.refObject = self.data["refObject"]
        except: self.refObject = None
        try: self.votedValue = self.data["votedValue"]
        except: self.votedValue = None
        try: self.content = self.data["content"]
        except: self.content = None
        try: self.createdTime = self.data["createdTime"]
        except: self.createdTime = None
        try: self.extensions = self.data["extensions"]
        except: self.extensions = None
        try: self.commentsCount = self.data["commentsCount"]
        except: self.commentsCount = None
        try: self.featuredType = self.data["extensions"]["featuredType"]
        except: self.featuredType = None
        try: self.disabledTime = self.data["extensions"]["__disabledTime__"]
        except: self.disabledTime = None
        try: self.quizPlayedTimes = self.data["extensions"]["quizPlayedTimes"]
        except: self.quizPlayedTimes = None
        try: self.quizTotalQuestionCount = self.data["extensions"]["quizTotalQuestionCount"]
        except: self.quizTotalQuestionCount = None
        try: self.quizTrendingTimes = self.data["extensions"]["quizTrendingTimes"]
        except: self.quizTrendingTimes = None
        try: self.quizLastAddQuestionTime = self.data["extensions"]["quizLastAddQuestionTime"]
        except: self.quizLastAddQuestionTime = None
        return self

class BlogList:
    def __init__(self, data):
        self.data = data

        _author, _quizQuestionList = [], []
        for dat in self.data:
            try: _author.append(dat["author"])
            except: _author.append(None)
            try: _quizQuestionList.append(QuizQuestionList(dat["quizQuestionList"]).QuizQuestionList)
            except: _quizQuestionList.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.quizQuestionList = _quizQuestionList

        self.createdTime = []
        self.globalVotesCount = []
        self.globalVotedValue = []
        self.keywords = []
        self.mediaList = []
        self.style = []
        self.totalQuizPlayCount = []
        self.title = []
        self.tipInfo = []
        self.tippersCount = []
        self.tippable = []
        self.tippedCoins = []
        self.contentRating = []
        self.needHidden = []
        self.guestVotesCount = []
        self.type = []
        self.status = []
        self.globalCommentsCount = []
        self.modifiedTime = []
        self.widgetDisplayInterval = []
        self.totalPollVoteCount = []
        self.blogId = []
        self.viewCount = []
        self.fansOnly = []
        self.backgroundColor = []
        self.votesCount = []
        self.endTime = []
        self.refObjectId = []
        self.refObject = []
        self.votedValue = []
        self.extensions = []
        self.commentsCount = []
        self.content = []
        self.featuredType = []
        self.shareUrl = []
        self.disabledTime = []
        self.quizPlayedTimes = []
        self.quizTotalQuestionCount = []
        self.quizTrendingTimes = []
        self.quizLastAddQuestionTime = []

    @property
    def BlogList(self):
        for x in self.data:
            try: self.globalVotesCount.append(x["globalVotesCount"])
            except: self.globalVotesCount.append(None)
            try: self.globalVotedValue.append(x["globalVotedValue"])
            except: self.globalVotedValue.append(None)
            try: self.keywords.append(x["keywords"])
            except: self.keywords.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.style.append(x["style"])
            except: self.style.append(None)
            try: self.totalQuizPlayCount.append(x["totalQuizPlayCount"])
            except: self.totalQuizPlayCount.append(None)
            try: self.title.append(x["title"])
            except: self.title.append(None)
            try: self.tipInfo.append(x["tipInfo"])
            except: self.tipInfo.append(None)
            try: self.tippersCount.append(x["tipInfo"]["tippersCount"])
            except: self.tippersCount.append(None)
            try: self.tippable.append(x["tipInfo"]["tippable"])
            except: self.tippable.append(None)
            try: self.tippedCoins.append(x["tipInfo"]["tippedCoins"])
            except: self.tippedCoins.append(None)
            try: self.contentRating.append(x["contentRating"])
            except: self.contentRating.append(None)
            try: self.needHidden.append(x["needHidden"])
            except: self.needHidden.append(None)
            try: self.guestVotesCount.append(x["guestVotesCount"])
            except: self.guestVotesCount.append(None)
            try: self.type.append(x["type"])
            except: self.type.append(None)
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.globalCommentsCount.append(x["globalCommentsCount"])
            except: self.globalCommentsCount.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.widgetDisplayInterval.append(x["widgetDisplayInterval"])
            except: self.widgetDisplayInterval.append(None)
            try: self.totalPollVoteCount.append(x["totalPollVoteCount"])
            except: self.totalPollVoteCount.append(None)
            try: self.blogId.append(x["blogId"])
            except: self.blogId.append(None)
            try: self.viewCount.append(x["viewCount"])
            except: self.viewCount.append(None)
            try: self.fansOnly.append(x["extensions"]["fansOnly"])
            except: self.fansOnly.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except: self.backgroundColor.append(None)
            try: self.votesCount.append(x["votesCount"])
            except: self.votesCount.append(None)
            try: self.endTime.append(x["endTime"])
            except: self.endTime.append(None)
            try: self.refObjectId.append(x["refObjectId"])
            except: self.refObjectId.append(None)
            try: self.refObject.append(x["refObject"])
            except: self.refObject.append(None)
            try: self.votedValue.append(x["votedValue"])
            except: self.votedValue.append(None)
            try: self.content.append(x["content"])
            except: self.content.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.shareUrl.append(x["shareURLFullPath"])
            except: self.shareUrl.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except: self.commentsCount.append(None)
            try: self.featuredType.append(x["extensions"]["featuredType"])
            except: self.featuredType.append(None)
            try: self.disabledTime.append(x["extensions"]["__disabledTime__"])
            except: self.disabledTime.append(None)
            try: self.quizPlayedTimes.append(x["extensions"]["quizPlayedTimes"])
            except: self.quizPlayedTimes.append(None)
            try: self.quizTotalQuestionCount.append(x["extensions"]["quizTotalQuestionCount"])
            except: self.quizTotalQuestionCount.append(None)
            try: self.quizTrendingTimes.append(x["extensions"]["quizTrendingTimes"])
            except: self.quizTrendingTimes.append(None)
            try: self.quizLastAddQuestionTime.append(x["extensions"]["quizLastAddQuestionTime"])
            except: self.quizLastAddQuestionTime.append(None)
        return self

class GetBlogInfo:
    def __init__(self, data):
        self.data = data

    @property
    def GetBlogInfo(self):
        try: self.blog: Blog = Blog(self.data["blog"]).Blog
        except: self.blog: Blog = Blog([])
        try: self.isBookmarked = self.data["isBookmarked"]
        except: self.isBookmarked = None
        return self

class QuizQuestionList:
    def __init__(self, data):
        self.data = data
        _answersList = []

        for y in data:
            try: _answersList.append(QuizAnswers(y["extensions"]["quizQuestionOptList"]).QuizAnswers)
            except: _answersList.append(None)

        self.status = []
        self.parentType = []
        self.title = []
        self.createdTime = []
        self.questionId = []
        self.parentId = []
        self.mediaList = []
        self.extensions = []
        self.style = []
        self.backgroundImage = []
        self.backgroundColor = []
        self.answerExplanation = []
        self.answersList = _answersList

    @property
    def QuizQuestionList(self):
        for x in self.data:
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.parentType.append(x["parentType"])
            except: self.parentType.append(None)
            try: self.title.append(x["title"])
            except: self.title.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.questionId.append(x["quizQuestionId"])
            except: self.questionId.append(None)
            try: self.parentId.append(x["parentId"])
            except: self.parentId.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.style.append(x["extensions"]["style"])
            except: self.style.append(None)
            try: self.backgroundImage.append(x["extensions"]["style"]["backgroundMediaList"][0][1])
            except: self.backgroundImage.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except: self.backgroundColor.append(None)
            try: self.answerExplanation.append(x["extensions"]["quizAnswerExplanation"])
            except: self.answerExplanation.append(None)
        return self

class QuizAnswers:
    def __init__(self, data):
        self.data = data
        self.answerId = []
        self.isCorrect = []
        self.mediaList = []
        self.title = []
        self.qhash = []

    @property
    def QuizAnswers(self):
        for x in self.data:
            try: self.answerId.append(x["optId"])
            except: self.answerId.append(None)
            try: self.qhash.append(x["qhash"])
            except: self.qhash.append(None)
            try: self.isCorrect.append(x["isCorrect"])
            except: self.isCorrect.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.title.append(x["title"])
            except: self.title.append(None)
        return self

class QuizRanking:
    def __init__(self, data):
        self.data = data

    @property
    def QuizRanking(self):
        try: self.highestMode = self.data["highestMode"]
        except: self.highestMode = None
        try: self.modifiedTime = self.data["modifiedTime"]
        except: self.modifiedTime = None
        try: self.isFinished = self.data["isFinished"]
        except: self.isFinished = None
        try: self.hellIsFinished = self.data["hellIsFinished"]
        except: self.hellIsFinished = None
        try: self.highestScore = self.data["highestScore"]
        except: self.highestScore = None
        try: self.beatRate = self.data["beatRate"]
        except: self.beatRate = None
        try: self.lastBeatRate = self.data["lastBeatRate"]
        except: self.lastBeatRate = None
        try: self.totalTimes = self.data["totalTimes"]
        except: self.totalTimes = None
        try: self.latestScore = self.data["latestScore"]
        except: self.latestScore = None
        try: self.latestMode = self.data["latestMode"]
        except: self.latestMode = None
        try: self.createdTime = self.data["createdTime"]
        except: self.createdTime = None
        return self

class QuizRankings:
    def __init__(self, data):
        self.data = data
        _rankingList = []

        for y in data:
            try: _rankingList.append(QuizRanking(y["quizResultRankingList"]).QuizRanking)
            except: _rankingList.append(None)

        self.rankingList = _rankingList
        self.profile: QuizRanking = QuizRanking([])

    @property
    def QuizRankings(self):
        try: self.quizPlayedTimes = self.data["quizPlayedTimes"]
        except: self.quizPlayedTimes = None
        try: self.quizInBestQuizzes = self.data["quizInBestQuizzes"]
        except: self.quizInBestQuizzes = None
        try: self.profile: QuizRanking = QuizRanking(self.data["quizResultOfCurrentUser"]).QuizRanking
        except: pass
        return self

class ChatThread:
    def __init__(self, data):
        self.data = data

    @property
    def ChatThread(self):
        try: self.userAddedTopicList = self.data["userAddedTopicList"]
        except: self.userAddedTopicList = []
        try: self.chatBubbles = self.data["chatBubbles"]
        except: self.chatBubbles = {}
        try: self.hostId = self.data["uid"]
        except: self.hostId = None
        try: self.membersQuota = self.data["membersQuota"]
        except: self.membersQuota = None
        try: self.membersSummary = self.data["membersSummary"]
        except: self.membersSummary = []
        try: self.chatId = self.data["threadId"]
        except: self.chatId = None
        try: self.keywords = self.data["keywords"]
        except: self.keywords = None
        try: self.membersCount = self.data["membersCount"]
        except: self.membersCount = None
        try: self.strategyInfo = self.data["strategyInfo"]
        except: self.strategyInfo = None
        try: self.isPinned = self.data["isPinned"]
        except: self.isPinned = None
        try: self.title = self.data["title"]
        except: self.title = None
        try: self.tipInfo = self.data["tipInfo"]
        except: self.tipInfo = {}
        try: self.tipOptionList = self.data["tipInfo"]["tipOptionList"]
        except: self.tipOptionList = []
        try: self.tipMaxCoin = self.data["tipInfo"]["tipMaxCoin"]
        except: self.tipMaxCoin = None
        try: self.tippersCount = self.data["tipInfo"]["tippersCount"]
        except: self.tippersCount = None
        try: self.tippable = self.data["tipInfo"]["tippable"]
        except: self.tippable = None
        try: self.tipMinCoin = self.data["tipInfo"]["tipMinCoin"]
        except: self.tipMinCoin = None
        try: self.tipCustomOption = self.data["tipInfo"]["tipCustomOption"]
        except: self.tipCustomOption = None
        try: self.tipCustomOptionValue = self.data["tipInfo"]["tipCustomOption"]["value"]
        except: self.tipCustomOptionValue = None
        try: self.tipCustomOptionIcon = self.data["tipInfo"]["tipCustomOption"]["icon"]
        except: self.tipCustomOptionIcon = None
        try: self.tippedCoins = self.data["tipInfo"]["tippedCoins"]
        except: self.tippedCoins = None
        try: self.membershipStatus = self.data["membershipStatus"]
        except: self.membershipStatus = None
        try: self.content = self.data["content"]
        except: self.content = None
        try: self.needHidden = self.data["needHidden"]
        except: self.needHidden = None
        try: self.alertOption = self.data["alertOption"]
        except: self.alertOption = None
        try: self.lastReadTime = self.data["lastReadTime"]
        except: self.lastReadTime = None
        try: self.type = self.data["type"]
        except: self.type = None
        try: self.status = self.data["status"]
        except: self.status = None
        try: self.publishToGlobal = self.data["publishToGlobal"]
        except: self.publishToGlobal = None
        try: self.modifiedTime = self.data["modifiedTime"]
        except: self.modifiedTime = None
        try: self.lastMessageSummary = self.data["lastMessageSummary"]
        except: self.lastMessageSummary = []
        try: self.condition = self.data["condition"]
        except: self.condition = None
        try: self.iconUrl = self.data["icon"]
        except: self.iconUrl = None
        try: self.latestActivityTime = self.data["latestActivityTime"]
        except: self.latestActivityTime = None
        try: self.author: UserProfile = UserProfile(self.data["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([]).UserProfile
        try: self.extensions = self.data["extensions"]
        except: self.extensions = None
        try: self.announcement = self.data["extensions"]["announcement"]
        except: self.announcement = None
        try: self.coHosts = self.data["extensions"]["coHost"]
        except: self.coHosts = None
        try: self.language = self.data["extensions"]["language"]
        except: self.language = None
        try: self.membersCanInvite = self.data["extensions"]["membersCanInvite"]
        except: self.membersCanInvite = None
        try: self.screeningRoomPermission = self.data["extensions"]["screeningRoomPermission"]["action"]
        except: self.screeningRoomPermission = None
        try: self.background = self.data["extensions"]["bm"]
        except: self.background = []
        try: self.backgroundUrl = self.data["extensions"]["bm"][1]
        except: self.backgroundUrl = None
        try: self.backgroundFileName = self.data["extensions"]["bm"][5]["fileName"]
        except: self.backgroundFileName = None
        try: self.avchatMemberUidList = self.data["extensions"]["avchatMemberUidList"]
        except: self.avchatMemberUidList = []
        try: self.visibility = self.data["extensions"]["visibility"]
        except: self.visibility = None
        try: self.bannedUserIds = self.data["extensions"]["bannedMemberUidList"]
        except: self.bannedUserIds = None
        try: self.lastMembersSummaryUpdateTime = self.data["extensions"]["lastMembersSummaryUpdateTime"]
        except: self.lastMembersSummaryUpdateTime = None
        try: self.fansOnly = self.data["extensions"]["fansOnly"]
        except: self.fansOnly = None
        try: self.channelType = self.data["extensions"]["channelType"]
        except: self.channelType = None
        try: self.pinAnnouncement = self.data["extensions"]["pinAnnouncement"]
        except: self.pinAnnouncement = None
        try: self.vvChatJoinType = self.data["extensions"]["vvChatJoinType"]
        except: self.vvChatJoinType = None
        try: self.viewOnly = self.data["extensions"]["viewOnly"]
        except: self.viewOnly = None
        try: self.comId = self.data["ndcId"]
        except: self.comId = None
        try: self.createdTime = self.data["createdTime"]
        except: self.createdTime = None
        return self

class Community:
    def __init__(self, data):
        self.data = data

    @property
    def Community(self):
        try: self.agent: UserProfile = UserProfile(self.data["agent"]).UserProfile
        except: self.agent: UserProfile = UserProfile([])
        try: self.name = self.data["name"]
        except: self.name = None
        try: self.usersCount = self.data["membersCount"]
        except: self.usersCount = None
        try: self.createdTime = self.data["createdTime"]
        except: self.createdTime = None
        try: self.aminoId = self.data["endpoint"]
        except: self.aminoId = None
        try: self.icon = self.data["icon"]
        except: self.icon = None
        try: self.link = self.data["link"]
        except: self.link = None
        try: self.comId = self.data["ndcId"]
        except: self.comId = None
        try: self.modifiedTime = self.data["modifiedTime"]
        except: self.modifiedTime = None
        try: self.status = self.data["status"]
        except: self.status = None
        try: self.joinType = self.data["joinType"]
        except: self.joinType = None
        try: self.primaryLanguage = self.data["primaryLanguage"]
        except: self.primaryLanguage = None
        try: self.heat = self.data["communityHeat"]
        except: self.heat = None
        try: self.userAddedTopicList = self.data["userAddedTopicList"]
        except: self.userAddedTopicList = None
        try: self.probationStatus = self.data["probationStatus"]
        except: self.probationStatus = None
        try: self.listedStatus = self.data["listedStatus"]
        except: self.listedStatus = None
        try: self.themePack = self.data["themePack"]
        except: self.themePack = None
        try: self.themeColor = self.data["themePack"]["themeColor"]
        except: self.themeColor = None
        try: self.themeHash = self.data["themePack"]["themePackHash"]
        except: self.themeHash = None
        try: self.themeVersion = self.data["themePack"]["themePackRevision"]
        except: self.themeVersion = None
        try: self.themeUrl = self.data["themePack"]["themePackUrl"]
        except: self.themeUrl = None
        try: self.themeHomePageAppearance = self.data["configuration"]["appearance"]["homePage"]["navigation"]
        except: self.themeHomePageAppearance = None
        try: self.themeLeftSidePanelTop = self.data["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level1"]
        except: self.themeLeftSidePanelTop = None
        try: self.themeLeftSidePanelBottom = self.data["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level2"]
        except: self.themeLeftSidePanelBottom = None
        try: self.themeLeftSidePanelColor = self.data["configuration"]["appearance"]["leftSidePanel"]["style"]["iconColor"]
        except: self.themeLeftSidePanelColor = None
        try: self.customList = self.data["configuration"]["page"]["customList"]
        except: self.customList = None
        try: self.tagline = self.data["tagline"]
        except: self.tagline = None
        try: self.searchable = self.data["searchable"]
        except: self.searchable = None
        try: self.isStandaloneAppDeprecated = self.data["isStandaloneAppDeprecated"]
        except: self.isStandaloneAppDeprecated = None
        try: self.keywords = self.data["keywords"]
        except: self.keywords = None
        try: self.mediaList = self.data["mediaList"]
        except: self.mediaList = None
        try: self.description = self.data["content"]
        except: self.description = None
        try: self.isStandaloneAppMonetizationEnabled = self.data["isStandaloneAppMonetizationEnabled"]
        except: self.isStandaloneAppMonetizationEnabled = None
        try: self.advancedSettings = self.data["advancedSettings"]
        except: self.advancedSettings = None
        try: self.defaultRankingTypeInLeaderboard = self.data["advancedSettings"]["defaultRankingTypeInLeaderboard"]
        except: self.defaultRankingTypeInLeaderboard = None
        try: self.frontPageLayout = self.data["advancedSettings"]["frontPageLayout"]
        except: self.frontPageLayout = None
        try: self.hasPendingReviewRequest = self.data["advancedSettings"]["hasPendingReviewRequest"]
        except: self.hasPendingReviewRequest = None
        try: self.welcomeMessageEnabled = self.data["advancedSettings"]["welcomeMessageEnabled"]
        except: self.welcomeMessageEnabled = None
        try: self.welcomeMessage = self.data["advancedSettings"]["welcomeMessageText"]
        except: self.welcomeMessage = None
        try: self.pollMinFullBarVoteCount = self.data["advancedSettings"]["pollMinFullBarVoteCount"]
        except: self.pollMinFullBarVoteCount = None
        try: self.catalogEnabled = self.data["advancedSettings"]["catalogEnabled"]
        except: self.catalogEnabled = None
        try: self.leaderboardStyle = self.data["advancedSettings"]["leaderboardStyle"]
        except: self.leaderboardStyle = None
        try: self.newsfeedPages = self.data["advancedSettings"]["newsfeedPages"]
        except: self.newsfeedPages = None
        try: self.joinedBaselineCollectionIdList = self.data["advancedSettings"]["joinedBaselineCollectionIdList"]
        except: self.joinedBaselineCollectionIdList = None
        try: self.activeInfo = self.data["activeInfo"]
        except: self.activeInfo = None
        try: self.configuration = self.data["configuration"]
        except: self.configuration = None
        try: self.extensions = self.data["extensions"]
        except: self.extensions = None
        try: self.nameAliases = self.data["extensions"]["communityNameAliases"]
        except: self.nameAliases = None
        try: self.promotionalMediaList = self.data["promotionalMediaList"]
        except: self.promotionalMediaList = None
        return self

class Message:
    def __init__(self, data):
        self.data = data

    @property
    def Message(self):
        try: self.author: UserProfile = UserProfile(self.data["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([]).UserProfile
        try: self.content = self.data["content"]
        except: self.content = None
        try: self.includedInSummary = self.data["includedInSummary"]
        except: self.includedInSummary = None
        try: self.isHidden = self.data["isHidden"]
        except: self.isHidden = None
        try: self.messageId = self.data["messageId"]
        except: self.messageId = None
        try: self.messageType = self.data["messageType"]
        except: self.messageType = None
        try: self.type = self.data["type"]
        except: self.type = None
        try: self.mediaValue = self.data["mediaValue"]
        except: self.mediaValue = None
        try: self.extensions = self.data["extensions"]
        except: self.extensions = None
        try: self.originalStickerId = self.data["extensions"]["originalStickerId"]
        except: self.originalStickerId = None
        try: self.mentionUserIds = self.data["extensions"]["mentionUserIds"]
        except: self.mentionUserIds = None
        try: self.chatBubbleId = self.data["chatBubbleId"]
        except: self.chatBubbleId = None
        try: self.clientRefId = self.data["clientRefId"]
        except: self.clientRefId = None
        try: self.mentions = self.data["extensions"]["mentionedArray"]
        except: self.mentions = None
        try: self.tippingCoins = self.data["extensions"]["tippingCoins"]
        except: self.tippingCoins = None
        try: self.mediaType = self.data["mediaType"]
        except: self.mediaType = None
        try: self.chatId = self.data["threadId"]
        except: self.chatId = None
        try: self.createdTime = self.data["createdTime"]
        except: self.createdTime = None
        try: self.chatBubbleVersion = self.data["chatBubbleVersion"]
        except: self.chatBubbleVersion = None
        return self

class Event:
    def __init__(self, data):
        self.data = data

    @property
    def Event(self):
        try: self.comId = self.data["ndcId"]
        except: self.comId = None
        try: self.message   = Message(self.data["chatMessage"]).Message
        except: self.message = None
        try: self.alertOption = self.data["alertOption"]
        except: self.alertOption = None
        try: self.membershipStatus = self.data["membershipStatus"]
        except: self.membershipStatus = None
        
        return self

class FromCode:
    def __init__(self, data):
        self.data = data

    @property
    def FromCode(self):
        try: self.linkInfo = self.data["extensions"]["linkInfo"]
        except: self.linkInfo = None
        try: self.path = self.data["path"]
        except: self.path = None
        try: self.comId = self.data["path"][1:self.data["path"].index("/")]
        except: self.comId = None
        try: self.objectType = self.linkInfo["objectType"]
        except: self.objectType = None
        try: self.shortCode = self.linkInfo["shortCode"]
        except: self.shortCode = None
        try: self.fullPath = self.linkInfo["fullPath"]
        except: self.fullPath = None
        try: self.targetCode = self.linkInfo["targetCode"]
        except: self.targetCode = None
        try: self.objectId = self.linkInfo["objectId"]
        except: self.objectId = None
        try: self.shortUrl = self.linkInfo["shareURLShortCode"]
        except: self.shortUrl = None
        try: self.fullUrl = self.linkInfo["shareURLFullPath"]
        except: self.fullUrl = None
        return self