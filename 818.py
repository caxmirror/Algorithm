class Solution:
    def racecar(self, target: int) -> int:
        # 1 2 4 8 16
        # 1 3 7 15 31
        # 4 AARRA 13334 AAARA
        # BFS way to solve this
        top = 1
        while top <= target: 
            top *= 2

        # search the number in top
        vis = set()
        res = [0] * top
        count = 1
        dq = deque()
        dq.append([0, 1]) #position, speed
        level = 0
        while count < top and dq:
            length = len(dq)
            level += 1
            for i in range(length):
                position, speed = dq.popleft()
                if 0 < position + speed < top:
                    if (position + speed, speed * 2) not in vis:
                        dq.append([position + speed, speed * 2])
                        vis.add((position + speed, speed * 2))
                    if res[position + speed] == 0:
                        res[position + speed] = level
                        count += 1
                if 0 < position < top:
                    new_speed = -1 if speed > 0 else 1
                    if (position, new_speed) not in vis:
                        dq.append([position, new_speed])
                        vis.add((position, new_speed))
                    if res[position] == 0:
                        res[position] = level
                        count += 1
        return res[target]
    