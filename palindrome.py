class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev=0
        org=x
        if x<0:
            return False
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        return rev==org