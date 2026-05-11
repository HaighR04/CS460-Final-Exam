# Development Log – The Torchbearer

**Student Name:** Ryan Haigh
**Student ID:** 130419637

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/10/26]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

This assignment focuses on the torchbearer, which is a robot that must begin at entrance S, then traverse through every relic chamber in set M at least once, then finally exit through T, all while using the minimum possible fuel. Since this dungeon is a weighted directed graph, edges will only go one way with a cost.

The important focus is first locating the shortest path to each room, as well as connections between them, and then once all paths are discovered, connect the shortest order of room traversals from start to finish
to ensure that the route is really the "shortest path"

I think the first thing that needs to be implemented is run_dijkstra, since this is what everything else relies on for the correct shortest-path distances. Looking at the program, _explore looks to be the most difficult part due to the pruning aspect, as getting that, backtracking, and the base case all correct at the same time will be tough. For testing, the four provided test cases would be a good start, then I will try some small graphs that I make so that I can verify the answers myself.

---

## Entry 2 – [5/10/26]: Work through Part 1, 2, and 3, as well as implementing the code for Part 2 and Part 3

I read through all the files and took notes on the order that I should complete everything. I reasoned through run_dijkstra's, and realized an edge case that I might have missed had I not fully read through it.
This edge case regarded nodes that do not have outgoing nodes, and are mentioned in other noes, ie 'B': [('C', 2)], where B would be considered a key, but C is not included in graph, and therefore might get ignored
I completed my goal of finishing Parts 1, 2, and 3 for both torchbearer and README, and will re-read over README and ASSIGNMENT today, and continue with Part 4 and 5 tomorrow.
---

## Entry 3 – [5/11/26]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | ~1 hour |
| Part 2: Precomputation Design | ~2 hours |
| Part 3: Algorithm Correctness | 30 minutes |
| Part 4: Search Design | ~ 45 minutes |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
