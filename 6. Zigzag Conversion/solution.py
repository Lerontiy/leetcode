from icecream import ic


class Solution(object):
    def convert(self, s: str, numRows: int):
        ret_list = ["" for _ in range(numRows)]
        write_line = 1
        normal_write = True
        for el in s:
            # ic(write_line, el)
            ret_list[write_line - 1] += el

            if numRows > 1:
                if write_line in {numRows} or (
                    write_line in {1} and normal_write is False
                ):
                    normal_write = not normal_write

                if normal_write:
                    write_line += 1
                else:
                    write_line -= 1

        return "".join(ret_list)


solution_obj = Solution()
