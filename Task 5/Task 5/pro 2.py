class Solution:
    def sampleStats(self, count: list[float]) -> list[float]:
        minimum = -1.0
        maximum = -1.0
        total_sum = 0
        total_count = sum(count)
        mode = 0
        max_freq = 0
        
        for i in range(256):
            if count[i] > 0:
                if minimum == -1.0: minimum = float(i)
                maximum = float(i)
                total_sum += i * count[i]
                if count[i] > max_freq:
                    max_freq = count[i]
                    mode = i
        
        mean = total_sum / total_count
        
        median = 0.0
        if total_count % 2 == 1:
            mid = (total_count // 2) + 1
            curr = 0
            for i in range(256):
                curr += count[i]
                if curr >= mid:
                    median = float(i)
                    break
        else:
            mid1 = total_count // 2
            mid2 = mid1 + 1
            m1 = m2 = -1
            curr = 0
            for i in range(256):
                curr += count[i]
                if m1 == -1 and curr >= mid1: m1 = i
                if m2 == -1 and curr >= mid2: m2 = i
                if m1 != -1 and m2 != -1: break
            median = (m1 + m2) / 2.0
            
        return [minimum, maximum, mean, median, float(mode)]