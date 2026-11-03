from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0

        self.tweets = defaultdict(list)

        self.following = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        #Users are following users and self id
        users = self.following[userId] | {userId}

        for uid in users:
            if uid not in self.tweets or not self.tweets[uid]:
                continue
            index = len(self.tweets[uid])- 1
            timestamp, tweetId = self.tweets[uid][index]

            heapq.heappush(heap,
            (-timestamp, tweetId, uid, index - 1))

        result = []
        while heap and len(result) < 10:
            neg_timestamp, tweetId, uid, next_index = heapq.heappop(heap)
            result.append(tweetId)

            if next_index >= 0:
                timestamp, older_tweet_id = self.tweets[uid][next_index]

                heapq.heappush(heap, (-timestamp, older_tweet_id, uid, next_index - 1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)