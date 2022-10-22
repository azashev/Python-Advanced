from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = deque([int(x) for x in input().split(', ')])
box_size = 50
filled_boxes = 0

while eggs and papers:
    egg = eggs[0]
    paper = papers[-1]
    current_sum = egg + paper

    if egg <= 0:
        eggs.popleft()
        continue
    if egg == 13:
        eggs.popleft()
        paper = papers.pop()
        papers.append(papers.popleft())
        papers.appendleft(paper)
        continue

    if current_sum <= box_size:
        filled_boxes += 1
        eggs.popleft()
        papers.pop()
    else:
        eggs.popleft()
        papers.pop()

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
