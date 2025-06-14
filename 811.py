# time: n * len(word)
# space: n * len(word)

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # dict
        dic = {}
        for cpdomain in cpdomains: 
            str_list = cpdomain.split(" ")
            count = int(str_list[0])
            domain_list = str_list[1].split(".")
            
            for i in range(len(domain_list) - 1, -1, -1):
                if i == len(domain_list) - 1:
                    cur_string = domain_list[i]
                else:
                    cur_string = domain_list[i] + "." + cur_string
                if cur_string in dic:
                    dic[cur_string] += count
                else:
                    dic[cur_string] = count
        res = []
        for key, value in dic.items():
            tmp = str(value) + " " + key
            res.append(tmp)
        return res