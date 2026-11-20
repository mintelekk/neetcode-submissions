class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans_a = False
        ans_b = False
        ans_c = False
        triplets_filtered = []
        for a, b, c in triplets:
            #Filter out all unusable triplets
            if not (a > target[0] or b > target[1] or c > target[2]):
                triplets_filtered.append([a,b,c])
            #Check match
        for a,b,c in triplets_filtered:
            if a == target[0]:
                ans_a = True
            if b == target[1]:
                ans_b = True
            if c == target[2]:
                ans_c = True
        return ans_a and ans_b and ans_c