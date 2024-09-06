
'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.'''

'''(Sample Input 0

5
2 3 6 6 5
Sample Output 0

5'''


Solution 1:

if __name__ == '__main__':
    n = int(input())
    scores = map(int, input().split())
    unique_scores=sorted(set(scores), reverse=True)
    runnerup_score=unique_scores[1]
    print(runnerup_score)


Solution 2:

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores=list(arr)
    max_score=max(scores)
    
    while max_score in scores:
        scores.remove(max_score)
        
    runnerup_score=max(scores)
    print(runnerup_score)
