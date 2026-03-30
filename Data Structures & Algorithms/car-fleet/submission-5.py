class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position.sort(reverse = True)
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        times = []
        # for i in range(len(position)):
        #     tmp = (target-cars[i][0])/cars[i][1]
        #     times.append(tmp)
        print(cars)
        fleets = 0
        for pos, spe in cars:
            time = (target-pos)/spe
            times.append(time)
            if len(times) >=2 and times[-1] <= times[-2]:
                times.pop()
            else:
                fleets +=1
        return fleets
        # for i in range(1, len(position)):
        #     if speed[i] <= speed[i-1] and :
        #         fleets+=1
        # return fleets
# 3,3
# 3 : 4,4.5 : 1,10 : 0,3 : 7
# 3:4, 3:7, 4.5:10, 10:0
# speed = 4,2,1,1
# if 
# 4,6,8,10
# 1,3,5,7,9,11
# 0,1,2,3,4,5,6,7,8,9,10
# 7,8,9,10
        