class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        '''

        '''
        
        n = len(positions)
        robots = []

        for i in range(n):
            robots.append({ 
                "idx": i,
                "p": positions[i],
                "h": healths[i],
                "d": directions[i]
            })

        sorted_robots = sorted(robots, key=lambda r: r["p"])
        stack = []

        for robot in sorted_robots:
            if robot["d"] == "R":
                stack.append(robot)
            else:
                while stack and stack[-1]["d"] == "R":
                    robot2 = stack.pop()
                    if robot2["h"] > robot["h"]:
                        robot2["h"] -= 1
                        stack.append(robot2)
                        break
                    elif robot2["h"] < robot["h"]:
                        robot["h"] -= 1
                    else:
                        break
                else:
                    stack.append(robot)

        stack.sort(key=lambda r: r["idx"])
        return [r["h"] for r in stack]