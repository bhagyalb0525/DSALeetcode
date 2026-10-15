class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        match={}
        start='a'
        res=""
        for char in key:
            if char not in match and char!=" ":
                match[char]=start
                start=chr(ord(start)+1)
        for ch in message:
            if ch==" ":
                res+=ch
            else:
                res+=match[ch]
        return res