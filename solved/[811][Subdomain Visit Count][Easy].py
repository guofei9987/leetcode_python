# https://leetcode.com/problems/subdomain-visit-count
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        def parse_domain(cpdomain):
            num_counts, domain_str = cpdomain.split(sep=' ')
            domain_split_list = domain_str.split(sep='.')
            domain_list = ['.'.join(domain_split_list[i:]) for i in range(len(domain_split_list))]
            return {i: int(num_counts) for i in domain_list}
        domain_dict_all = dict()
        for cpdomain in cpdomains:
            domain_dict = parse_domain(cpdomain)
            for i in domain_dict:
                if i in domain_dict_all:
                    domain_dict_all[i] += domain_dict[i]
                else:
                    domain_dict_all[i] = domain_dict[i]
        output = []
        for i in domain_dict_all:
            output.append(str(domain_dict_all[i]) + ' ' + i)
        return output


# :guofei: a better solution
output_dict=dict()
cpdomains=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
for cpdomain in cpdomains:
    n,domain =cpdomain.split(' ')
    n,domain=int(n),domain.split('.')
    for i in range(len(domain)):
        tmp_domain_str='.'.join(domain[i:])
        output_dict[tmp_domain_str]=output[tmp_domain_str]+n if tmp_domain_str in output else n # trick 1
    output=['{} {}'.format(output_dict[i],i) for i in output_dict] # trick 2

output
