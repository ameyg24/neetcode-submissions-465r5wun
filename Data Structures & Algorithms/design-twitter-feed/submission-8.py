import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.maps = collections.defaultdict(list)
        self.followers = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.maps[userId].append((tweetId, self.time))
        self.time += 1
        if userId not in self.followers[userId]:
            self.followers[userId].append(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        visited = set()
        for el in self.followers[userId]:
            for tweet, time in self.maps[el]:
                if tweet not in visited:
                    heap.append((time, tweet))
                    visited.add(tweet)
        heapq.heapify(heap)
        while len(heap) > 10:
            heapq.heappop(heap)
        print(heap)
        heap.sort(reverse = True)
        return [tweet for time, tweet in heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId] and followeeId != followerId:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId] and followeeId != followerId:
            self.followers[followerId].remove(followeeId)
