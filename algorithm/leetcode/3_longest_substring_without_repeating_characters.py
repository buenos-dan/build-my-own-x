

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start_ptr = 0
        end_ptr = 0

        longest_length = 0
        while end_ptr < len(s):
            if s[end_ptr] in s[start_ptr:end_ptr]:
                longest_length = max(longest_length, end_ptr - start_ptr)
                while s[start_ptr] != s[end_ptr]:
                    start_ptr += 1
                start_ptr += 1

            end_ptr += 1

        longest_length = max(longest_length, end_ptr - start_ptr)

        return longest_length

    def benchmark(self):
        test_cases = [
            ("abcabccbb", 3),
            ("abcdefghijklmn", 14),
            ("pwwkew", 3),
            ("", 0),
            ("dvdf", 3),
        ]

        for case in test_cases:
            yield case


if __name__=="__main__":
    sol = Solution()

    for s, gt in sol.benchmark():
        length = sol.lengthOfLongestSubstring(s)
        assert length == gt, f"{s=}, {length=} != {gt=}"
