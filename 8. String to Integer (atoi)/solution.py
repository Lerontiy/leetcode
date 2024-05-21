from icecream import ic


class Solution(object):
    def __init__(self):
        self.nums = [str(i) for i in range(0, 10)]

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        ret_str = ""
        for i in s:
            ic(i, ret_str)
            if len(ret_str) == 0:
                if i not in self.nums + [" ", "-", "+"]:
                    return 0
                elif i == " ":
                    continue
                elif i in ["0"] and ("-" in s or "+" in s):
                    ret_str += i
                else:
                    ret_str += i
            else:
                if "+" in ret_str or "-" in ret_str:
                    if len(ret_str) == 1 and i == "0":
                        continue
                    if i in self.nums:
                        ret_str += i
                    else:
                        break
                elif i in self.nums + ["0"]:
                    ret_str += i
                else:
                    break

        try:
            ret_str = int(float(ret_str))
        except:  # noqa: E722
            ret_str = 0

        if ret_str < (-(2**31)):
            return -(2**31)
        elif ret_str > 2**31 - 1:
            return 2**31 - 1
        else:
            return ret_str


solution_obj = Solution()
