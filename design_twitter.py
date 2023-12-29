class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.twitts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitts.insert(0, [userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for user, tweet in self.twitts:
            if user in self.followers[userId] or user == userId:
                res.append(tweet)
            if len(res) == 10:
                return res
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].remove(followeeId)