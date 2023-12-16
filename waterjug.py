from collections import defaultdict
jug1 = int(input("Capacity of the first jug j1 : "))
jug2 = int(input("Capacity of the second jug j2 : "))
target = int(input("Enter the required capacity : "))

visited = defaultdict(lambda: False)

def waterJugSolver(cap1, cap2):

  if (cap1 == target and cap2 == 0) or (cap2 == target and cap1 == 0):
    print(cap1, cap2)
    return True

  if visited[(cap1, cap2)] == False:
    print(cap1, cap2)
    visited[(cap1, cap2)] = True
  
    return (waterJugSolver(0, cap2) or
        waterJugSolver(cap1, 0) or
        waterJugSolver(jug1, cap2) or
        waterJugSolver(cap1, jug2) or
        waterJugSolver(cap1 + min(cap2, (jug1-cap1)),
        cap2 - min(cap2, (jug1-cap1))) or
        waterJugSolver(cap1 - min(cap1, (jug2-cap2)),
        cap2 + min(cap1, (jug2-cap2))))
  else:
    return False
print("Steps: ")
waterJugSolver(0, 0)