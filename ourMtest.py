# input :geeksforgeek’
# Output : geeksfORGEEK
"""
s = "geeksforgeek"
s1 = len(s) // 2
# s2 = s[:s1] + s[s1:].upper()
# print(s2)
s3 = ""
for i in range(len(s)):
    if i >= s1:
        s3 += s[i].upper()
    else:
        s3 += s[i]
print(s3)
--------------------------------------------------------------------------------------------------------------------------------
"""
# Given a string str. The task is to check whether it is a binary string or not.
# Examples:
#
#
# Input: str = "01010101010"
# Output: Yes
#
# Input: str = "geeks101"
# Output: No

s1 = "010101010"
s2 = {"0", "1"}
s3 = set(s1)
if s2 == s3 or s3 == {"0"} or s3 == {"1"}:
    print("Yes")

else:
    print("No")
