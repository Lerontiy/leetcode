from icecream import ic  # noqa: F401


class Solution(object):
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """

        # reverse_x = []
        # multiple = 1
        negative = False
        if x < 0:
            x = -x
            negative = True
        # while x != 0:
        #    reverse_x += 1 * multiple
        #    x -= 1 * multiple
        #    if x % 1 * multiple * 10 == 0:
        #        multiple += 1

        x_list = list(str(x))
        x_list.reverse()
        x_list = "".join(x_list)
        x_list = int(x_list)

        if x_list < -(2**31) or x_list > 2**31 - 1:
            return 0
        elif negative:
            return -x_list

        return x_list


solution_obj = Solution()
