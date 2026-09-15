class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack problem n cars traveling to same destination in one-lane highway
        # two integer arrays: position and speed with length n
        # position[i] is position of ith car
        # speed[i] is speed of ith car

        #destination at position target miles

        #some stack
        
        """
        We're trying to find the number of fleets
        imagine we have pos = [1,2,3] and speed= [3,2,1]
        we have 1 fleet as it's capped at the first car's speed
        so the number of fleets is capped by the amount of 
        """
        desc_ord_list = []
        for i in range(0,len(position)):
            desc_ord_list.append([position[i], speed[i]])

        desc_ord_list = sorted(desc_ord_list,reverse=True)
        times = []
        for i in range(0, len(desc_ord_list)):
            position = desc_ord_list[i][0]
            speed = desc_ord_list[i][1]
            time = (target-position) /speed
            times.append(time)

        this_stack = []
        count = 0
        for i in range(0,len(times)):
            if not this_stack or times[i]>this_stack[-1]:
                this_stack.append(times[i])
            else:
                continue
        
        return(len(this_stack))