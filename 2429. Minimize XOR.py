class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        bin_num1 = str(bin(num1))[2:]
        bin_num2 = str(bin(num2))[2:]
        num2_count = list(bin_num2).count('1')
        if list(bin_num1).count('1') == num2_count:
            return num1
        num1_len = len(bin_num1)
        sol_chars = ["1" for x in range(num2_count)]
        sol_len = len(sol_chars)
        if sol_len>num1_len:
            bin_num1 = (sol_len-num1_len)*'0'+bin_num1
        else:
            sol_chars.extend(["0" for x in range(num1_len-num2_count)])
        sol = ""
        for x in bin_num1[:]:
            if x =='1':
                if x in sol_chars:
                    sol+=x
                    sol_chars.remove(x)
                else:
                    sol+='0'
                    sol_chars.remove("0")
            elif x=='0':
                if x in sol_chars:
                    sol+=x
                    sol_chars.remove(x)
                else:
                    sol+='1'
                    sol_chars.remove("1")
        return int(('0b'+sol),2)
