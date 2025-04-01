# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack_number, stack_string = [], []
        string, number = "", 0
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == "[":
                stack_number.append(number)
                stack_string.append(string)
                number, string = 0, ""
            elif c == "]":
                temp = stack_string.pop() + stack_number.pop() * string
                string = temp
            else:
                string += c
        return string
