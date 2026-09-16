class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        time1 = []
        for pos, speed1 in pairs:
            time = (target - pos) / speed1
            time1.append(time)
        stack = []
        for t in time1:
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)
