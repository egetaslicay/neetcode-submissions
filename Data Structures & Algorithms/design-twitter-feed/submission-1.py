class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        heap.extend(self.posts[userId])

        for user in self.following[userId]: 
            heap.extend(self.posts[user])

        heapq.heapify(heap)
        res = [] 
        
        k = 10 

        while k > 0 and heap: 
            poppedTweet = heapq.heappop(heap)
            res.append(poppedTweet[1])
            k -= 1

        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
