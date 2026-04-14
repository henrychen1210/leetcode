class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        '''
        robot = [0,4,6], factory = [[2,2],[6,2]]
        robot = [-1, 1], factory = [[-2,1],[2,1]]
        '''
        robot.sort()
        factory.sort()

        factory_positions = []
        
        for f in factory:
            for i in range(f[1]):
                factory_positions.append(f[0])

        robot_count = len(robot)
        factory_count = len(factory_positions)

        self.dp = [[None] * (factory_count + 1) for _ in range(robot_count + 1)]

        
        return self.helper(0, 0, robot, factory_positions)

    
    def helper(self, robot_idx, factory_idx, robot, factory_positions):
        if self.dp[robot_idx][factory_idx] is not None:
            return self.dp[robot_idx][factory_idx]

        if robot_idx == len(robot):
            self.dp[robot_idx][factory_idx] = 0
            return 0
        
        if factory_idx == len(factory_positions):
            self.dp[robot_idx][factory_idx] = float('inf')
            return float('inf')
        
        assign = abs(robot[robot_idx] - factory_positions[factory_idx]) + self.helper(robot_idx + 1, factory_idx + 1, robot, factory_positions)

        skip = self.helper(robot_idx, factory_idx + 1, robot, factory_positions)

        self.dp[robot_idx][factory_idx] = min(assign, skip)
    
        return self.dp[robot_idx][factory_idx]