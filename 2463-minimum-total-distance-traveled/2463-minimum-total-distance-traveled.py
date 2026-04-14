class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        factory_pos = []

        for f in factory:
            for _ in range(f[1]):
                factory_pos.append(f[0])
        
        m = len(robot)
        n = len(factory_pos)

        self.dp = [[None] * (n + 1) for _ in range(m + 1)]
            
        return self.helper(0, 0, robot, factory_pos)
        
        
    def helper(self, robot_idx, factory_idx, robot, factory_pos):
        if self.dp[robot_idx][factory_idx] is not None:
            return self.dp[robot_idx][factory_idx]

        if robot_idx == len(robot):
            self.dp[robot_idx][factory_idx] = 0
            return 0
        
        if factory_idx == len(factory_pos):
            self.dp[robot_idx][factory_idx] = float('inf')
            return float('inf')
        
        assign = abs(robot[robot_idx] - factory_pos[factory_idx]) + self.helper(robot_idx + 1, factory_idx + 1, robot, factory_pos)
        skip = self.helper(robot_idx, factory_idx + 1, robot, factory_pos)

        self.dp[robot_idx][factory_idx] = min(assign, skip)

        return  self.dp[robot_idx][factory_idx]