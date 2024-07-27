import heapq

def solution(scoville, K):
    # 스코빌 지수 배열을 최소 힙으로 변환
    heapq.heapify(scoville)
    
    mix_count = 0
    
    while scoville and scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        # 가장 낮은 스코빌 지수를 가진 두 음식을 꺼낸다
        least1 = heapq.heappop(scoville)
        least2 = heapq.heappop(scoville)
        
        # 새로운 음식의 스코빌 지수 계산
        new_scoville = least1 + (least2 * 2)
        
        # 새 음식의 스코빌 지수를 힙에 추가
        heapq.heappush(scoville, new_scoville)
        
        # 혼합 횟수 증가
        mix_count += 1
        
    # 모든 음식의 스코빌 지수가 K 이상이 되었는지 확인
    if all(x >= K for x in scoville):
        return mix_count
    else:
        return -1