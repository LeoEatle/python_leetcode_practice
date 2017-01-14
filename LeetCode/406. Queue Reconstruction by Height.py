class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        queue = []
        for h, k in sorted(people, key=lambda (h, k): (-h, k)):
            queue.insert(k, [h , k])
        return queue