

'''Depth First Search uses STACK AND RECURSION
'''
#import defaultdict
from collections import defaultdict
def dfs(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for neighbour in graph[start]:
    return path
graph=defaultdict(list)
n,e=map(int,input().split())
for i in range(e):
    graph[v].append(u)
#print(graph)
start='A'
visited=defaultdict(bool)
traversedpath=dfs(graph,start,visited,path)
print(traversedpath)
