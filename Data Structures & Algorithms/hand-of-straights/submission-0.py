import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        
        counter = defaultdict(int)
        for h in hand:
            counter[h] += 1
        minh = list(counter.keys())
        heapq.heapify(minh)
        while minh:
            curr = minh[0]
            for i in range(curr, curr + groupSize):
                print(minh)
                print(counter)
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != minh[0]:
                        return False
                    heapq.heappop(minh)
        return True