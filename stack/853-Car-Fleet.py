# Problem: https://leetcode.com/problems/car-fleet/
# Approach: Create a new list of tuples representing cars with pos and speed, sort in descending order. Maintain stack to represent number of fleets and to peek most recent/furthest back fleet.
#           Use time helper function to return (target - position) / speed, if this value is less than the car on top of stack it will join that fleet. If less than it starts a new fleet, so append to stack.
# Complexity: O(n log n) time, O(n) space
# Enjoyment: 4/5

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = []
        for car in cars:
            if not stack:
                stack.append(car)
                continue
            
            # new fleet starts if car cannot catch up to previous fleet
            if self.getTime(car, target) > self.getTime(stack[-1], target):
                stack.append(car)
        
        return len(stack)
    
    def getTime(self, car: tuple, target: int) -> int:
        return (target - car[0]) / car[1]
