# time: 1 -> 3^4
# space: 1 -> all address is finite
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(total_ip, cur_ip, level):
            if not is_valid(cur_ip):
                return

            if level == 4:
                if len(total_ip) == len(s) + 3:
                    res.append(total_ip)
                return

            start_index = len(total_ip) - level + 1 if level != 0 else len(total_ip) - level
            for i in range(3):
                if start_index + i < len(s):
                    next_ip = s[start_index:start_index + i + 1]
                    next_total_ip = total_ip + "." + next_ip if level != 0 else next_ip
                    dfs(next_total_ip, next_ip, level + 1)

        def is_valid(cur_ip):
            if cur_ip == "0" or cur_ip =="":
                return True
            if cur_ip[0] == "0":
                return False
            if int(cur_ip) > 255:
                return False
            return True

        dfs("","",0)
        return res