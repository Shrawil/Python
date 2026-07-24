class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if ((a >= 0) != (b >= 0)) and flag == False:
            return True
        elif (a < 0 and b < 0 and flag == True):
            return True
        return False