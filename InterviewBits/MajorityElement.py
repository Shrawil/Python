class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        dict = {}
        for i in A:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        # print(dict)
        # print(max(dict, key=dict.get))
        return max(dict, key=dict.get)