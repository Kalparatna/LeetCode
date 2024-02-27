class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrak(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] >target:
                    continue
                path.append(candidates[i])
                backtrak(i, target-candidates[i], path)
                path.pop()
        
        result = []
        candidates.sort()
        backtrak(0,target, [])
        return result
