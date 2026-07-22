"""โปรแกรมจัดแถวตามสั่งแบบป่วยๆ"""
N, K = map(int, input().split())

queues = [0] * (K + 1)

ready_queues = 0
count = 0
while count < N:
    x = int(input())

    if not queues[x]:
        ready_queues += 1

    queues[x] += 1

    if ready_queues == K:
        ready_queues = 0
        for j in range(1, K + 1):
            queues[j] -= 1
            if queues[j] > 0:
                ready_queues += 1
    count += 1

print(sum(queues))
