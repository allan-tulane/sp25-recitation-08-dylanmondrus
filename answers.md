# CMPS 2200 Recitation 08

## Answers

**Name:** Dylan Mondrus
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**

Each heappop takes O(log n) where n = number of vertices.
Each heappush takes O(log n).
So each edge causes a heappush which is O(E log V).
Each vertex causes a heappop which is O(V log V). 
So W(n) = O((V+E) log V)

Span is dominated by heappop since your can't explore a node until you find the best path/edges. Since heappop is O(V log V) then span is O(V log V). 



- **2b)**

