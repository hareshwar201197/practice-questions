class Solution:
    def find_median(self, v):
        # Code here
        v = sorted(v)
        v_len = len(v)
        if v_len % 2 != 0:
            a = int(v_len / 2)
            return v[a]
        else:
            if v_len == 2:
                return (v[0] + v[1]) / v_len
            p = int(v_len / 2)
            result = int((v[p] + v[p - 1]) / 2)
            return result

N = [18, 2, 10, 13, 8, 8]     #[90, 100, 78, 89, 67]
c = Solution()
print(c.find_median(N))