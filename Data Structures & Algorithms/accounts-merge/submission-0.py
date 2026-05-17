class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return
        email_to_acc = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e not in email_to_acc:
                    email_to_acc[e] = i
                else:
                    union(i, email_to_acc[e])
        acc_to_email = defaultdict(list)
        for e, i in email_to_acc.items():
            acc_to_email[find(i)].append(e)
        res = []
        for i, emails in acc_to_email.items():
            tmp = [accounts[i][0]] + sorted(emails)
            res.append(tmp)
        return res
        
