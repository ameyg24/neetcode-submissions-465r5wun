import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.maps = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.maps[userId].append([self.time, tweetId])
        self.time -= 1
        # if userId not in self.followers[userId]:
        #     self.followers[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.followers[userId].add(userId)
        res = []
        for el in self.followers[userId]:
            if el in self.maps:
                index = len(self.maps[el]) - 1
                count, tweetId = self.maps[el][index]
                heapq.heappush(heap, [count, tweetId, el, index - 1])
        while heap and len(res) < 10:
            count, tweetId, el, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.maps[el][index]
                heapq.heappush(heap, [count, tweetId, el, index - 1])
        return res
        # for el in self.followers[userId]:
        #     for tweet, time in self.maps[el]:
        #         heap.append((time, tweet))
        # heapq.heapify(heap)
        # while len(heap) > 10:
        #     heapq.heappop(heap)
        # print(heap)
        # heap.sort(reverse = True)
        # return [tweet for time, tweet in heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
