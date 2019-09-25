
Team:
  <cortiz20@amherst.edu bdudziak20@amherst.edu>
Heuristic for Q6:
  <We designed a heuristic that, for each of the pellets, kept a running counter
  final_path that was the manhattan distance from the current node to that pellet
  plus the manhattan distance from that pellet to the next closest pellet and
  so on for each pellet in the game state. Then, the lowest of these final_path
  counters was returned by the function. The algorithm is a little computationally
  taxing, but it is easily set to only calculate the final_path the first
  n (ex: n = 2) closest nodes, which exchanges optimality for more speed.>
Resources used:
  <We visited Billy's office hours!>
Time spent on assignment: <6>
On a scale from -2 to 2:
  How hard was the assignment?
  <0>
  How much did you learn from the assignment?
  <1>
  How much did you enjoy the assignment?
  <2>
Additional notes: <>
