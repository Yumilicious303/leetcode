#Design Twitter
import heapq
from collections import defaultdict

class Twitter(object):

    def __init__(self):
        self.followers = {}
        self.tweets = []
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets.append((userId, tweetId))
        self.follow(userId, userId)
        
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        feed = []
        i = len(self.tweets) - 1
        while len(feed) < 10:
            if i < 0:
                return feed
            if userId in self.followers[self.tweets[i][0]]:
                feed.append(self.tweets[i][1])
            i -= 1
        return feed



    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId not in self.followers:
            self.followers[followeeId] = {followerId}
        else:
            self.followers[followeeId].add(followerId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followers and followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)

class TwitterNeet(object):

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) #userId -> list of [count, tweetId]
        self.followMap = defaultdict(set) #userId -> set of followeeId
        

    def postTweet(self, userId, tweetId):
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId):
        res = [] 
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)




def case1():
    twitter = TwitterNeet()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))

def case10():
    twitter = TwitterNeet()
    twitter.postTweet(1,5)
    twitter.postTweet(1,3)
    twitter.postTweet(1,101)
    twitter.postTweet(1,13)
    twitter.postTweet(1,10)
    twitter.postTweet(1,2)
    twitter.postTweet(1,94)
    twitter.postTweet(1,505)
    twitter.postTweet(1,333)
    print(twitter.getNewsFeed(1))

case1()