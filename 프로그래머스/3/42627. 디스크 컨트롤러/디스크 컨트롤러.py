def solution(jobs):
    # 작업의 요청 시점과 소요 시간으로 정렬 (소요 시간이 같은 경우 요청 시점 기준으로 정렬)
    jobs.sort(key=lambda x: (x[0], x[1]))

    total_time = 0
    current_time = 0
    n = len(jobs)
    index = 0
    job_queue = []
    
    # 작업이 모두 처리될 때까지 반복
    while index < n or job_queue:
        # 현재 시점에서 처리할 수 있는 작업을 job_queue에 추가
        while index < n and jobs[index][0] <= current_time:
            job_queue.append(jobs[index])
            index += 1
            
        # job_queue에서 소요 시간이 가장 짧은 작업을 선택
        if job_queue:
            job_queue.sort(key=lambda x: x[1])  # 소요 시간 기준으로 정렬
            job = job_queue.pop(0)
            start_time = current_time
            end_time = start_time + job[1]
            total_time += (end_time - job[0])
            current_time = end_time
        else:
            # 대기 중인 작업이 없으면 시점을 다음 작업의 요청 시점으로 이동
            if index < n:
                current_time = jobs[index][0]

    # 평균 대기 시간 계산
    return total_time // n