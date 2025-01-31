class Solution_best:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # sliding window to pick out the pattern
        # Step 1: Sort and group by user
        visits = sorted(zip(timestamp, username, website))
        user_visits = {}
        for _, user, site in visits:
            if user not in user_visits:
                user_visits[user] = []
            user_visits[user].append(site)
        
        # Step 2: Count patterns
        pattern_count = {}
        for user, sites in user_visits.items():
            if len(sites) >= 3:
                # Generate all 3-website patterns
                seen = set()
                for i in range(len(sites) - 2):
                    for j in range(i + 1, len(sites) - 1):
                        for k in range(j + 1, len(sites)):
                            pattern = (sites[i], sites[j], sites[k])
                            if pattern not in seen:
                                seen.add(pattern)
                                if pattern not in pattern_count:
                                    pattern_count[pattern] = 0
                                pattern_count[pattern] += 1
        
        # Step 3: Find the most frequent pattern
        most_frequent = None
        max_count = 0
        for pattern, count in pattern_count.items():
            if count > max_count or (count == max_count and pattern < most_frequent):
                most_frequent = pattern
                max_count = count
        
        return list(most_frequent)



            
