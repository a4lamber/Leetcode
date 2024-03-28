"""
 # @ Author: Your name
 # @ Create Time: 2024-02-02 10:33:00
 # @ Modified by: Your name
 # @ Modified time: 2024-02-02 10:33:17
 # @ Description: very trashy code, need to be refactored
 """

from collections import defaultdict


class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        # rank by points descendingly, then by id ascendingly
        # 1. figure out a way to calculate the points
        # 2. figure out a way to store points for each student, hashmap
        positive_hash = set(positive_feedback)
        negative_hash = set(negative_feedback)

        # 算分
        student_hash = defaultdict(int)
        for i in range(len(student_id)):
            # split the report to list of string based on "space"
            words = report[i].split()
            for word in words:
                if word in negative_hash:
                    student_hash[student_id[i]] -= 1
                    continue
                if word in positive_hash:
                    student_hash[student_id[i]] += 3

        # bucket sort, populate it
        frequency = defaultdict(list)

        for student_id, count in student_hash.items():
            frequency[count].append(student_id)

        # sort first by occurence
        sorted(frequency, reverse=True)

        res = []
        # iterate the array from end to start,
        for _, students in frequency.items():
            if students:
                # sort by id ascendingly
                students.sort(reverse=False)
                for student in students:
                    res.append(student)
                    if len(res) == k:
                        return res
