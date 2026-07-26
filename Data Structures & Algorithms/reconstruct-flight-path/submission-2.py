class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dest in tickets:
            adj[src].append(dest)
        for src, dests in adj.items():
            dests.sort()
        
        visit = set()
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                res.append(v)
                adj[src].pop(i)
                if dfs(v):
                    return True
                res.pop()
                adj[src].insert(i, v)
            return False
        dfs("JFK")
        return res