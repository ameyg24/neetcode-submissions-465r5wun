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
        for followed in self.followers[userId]:
            if followed in self.maps:
                idx = len(self.maps[followed]) - 1
                time, tweetId = self.maps[followed][idx]
                heapq.heappush(heap, [time, tweetId, followed, idx - 1])
        while heap and len(res) < 10:
            time, tweetId, followed, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.maps[followed][idx]
                heapq.heappush(heap, [time, tweetId, followed, idx - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
