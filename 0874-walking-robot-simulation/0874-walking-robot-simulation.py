class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pos = {"at": [0, 0], "face": 0}

        obstacles_same_x = {}  # x -> list of y values
        obstacles_same_y = {}  # y -> list of x values

        for o in obstacles:
            if o[0] not in obstacles_same_x:
                obstacles_same_x[o[0]] = []
            if o[1] not in obstacles_same_y:
                obstacles_same_y[o[1]] = []
            obstacles_same_x[o[0]].append(o[1])
            obstacles_same_y[o[1]].append(o[0])

        res = 0

        for command in commands:
            if command == -1:
                pos["face"] = pos["face"] + 1 if pos["face"] < 3 else 0
            elif command == -2:
                pos["face"] = pos["face"] - 1 if pos["face"] > 0 else 3
            else:
                old_x = pos["at"][0]
                old_y = pos["at"][1]
                new_x = old_x + directions[pos["face"]][0] * command
                new_y = old_y + directions[pos["face"]][1] * command

                if directions[pos["face"]][0] != 0:  # moving in x
                    for o in obstacles_same_y.get(old_y, []):
                        if old_x < o <= new_x:
                            new_x = o - 1
                        elif old_x > o >= new_x:
                            new_x = o + 1
                else:  # moving in y
                    for o in obstacles_same_x.get(old_x, []):
                        if old_y < o <= new_y:
                            new_y = o - 1
                        elif old_y > o >= new_y:
                            new_y = o + 1

                pos["at"] = [new_x, new_y]
                res = max(res, new_x**2 + new_y**2)

        return res