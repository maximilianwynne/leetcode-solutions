class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_str = str(x)
        return num_str == num_str[::-1]

        print(isPalindrome(121))   
        print(isPalindrome(123))   
        print(isPalindrome(1221))
