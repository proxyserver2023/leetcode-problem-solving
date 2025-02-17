class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = list(s)
        left = 0
        right = len(s) - 1
        is_palindrome = True

        while left < right:

            # Check ASCII
            if ord(chars[left]) >= 65 and ord(chars[left]) <= 92:
                chars[left] = chr(ord(chars[left]) + 32)

            if ord(chars[right]) >= 65 and ord(chars[right]) <= 92:
                chars[right] = chr(ord(chars[right]) + 32)

            if not (
                (ord(chars[left]) >= 97 and ord(chars[left]) <= 122)
                or (ord(chars[left]) >= 48 and ord(chars[left]) <= 57)
            ):
                left += 1
                continue

            if not (
                (ord(chars[right]) >= 97 and ord(chars[right]) <= 122)
                or (ord(chars[right]) >= 48 and ord(chars[right]) <= 57)
            ):
                right -= 1
                continue

            if chars[left] != chars[right]:
                is_palindrome = False
                return is_palindrome

            left += 1
            right -= 1

        return is_palindrome


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))  # False
