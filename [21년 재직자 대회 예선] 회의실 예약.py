import sys

N, M = map(int,sys.stdin.readline().split())
conference_room = {} # dictionary 형태 회의실 이름과 시간을 저장하기 위해 사용

for __ in range(N):
    room_name = sys.stdin.readline().rstrip()
    conference_room[room_name] = [[i, i+1] for i in range(9, 18)] # 회의가 가능한 시간은 09 ~ 18 사이이고 최소 1시간 간격이므로 1시간 간격으로 시간 생성

for _ in range(M):
    r, s, t = sys.stdin.readline().split() # 회의실 이름, 시작 시각, 종료 시각
    
    # 시작 시각 ~ 종료 시각 구간안에 있는 1시간 간격의 시간들을 미리 만들어논 시간에서 제거시킴
    for i in range(int(s), int(t)): 
        if [i, i+1] not in conference_room[r]:
            pass
        
        else:
            conference_room[r].remove([i, i+1])

for value in sorted(conference_room.keys()): # 회의실 이름을 오름차순으로 출력시켜야 하므로 정렬시킴
    if len(conference_room[value]) == 0: # 회의실 예약이 불가능한 경우
        print("Room " + value + ":")
        print("Not available")
        
        if value == sorted(conference_room.keys())[-1]: # 마지막 value면 하이폰 다섯개를 출력을 안하고 종료
            break
    
        else:
            print("-----") # 마지막 value가 아니라면 하이폰 다섯개 출력
            
        continue # 다음 value값으로
    
    else: # 회의실 예약이 다 차지 않았을 경우
        tmp = [] # 임시
        answer= [] 
        
        for i in range(len(conference_room[value])):
            if len(conference_room[value]) == 1: # 회의 예약이 가능한 시간이 딱 하나만 있을 경우 
                tmp.append(conference_room[value][i])

            # 회의 예약이 가능한 시간이 여러 개 일 경우
            if i == len(conference_room[value])-1: # IndexError를 방지하기 위해 따로 선언
                tmp.append(conference_room[value][i])
            
            elif 0 <= i < len(conference_room[value])-1: 
                if conference_room[value][i][1] == conference_room[value][i+1][0]: # 현재 회의가 끝나는 시간이랑 다음 회의가 시작하는 시간이랑 같을 때
                    tmp.append(conference_room[value][i]) 
                
                else: # 
                    tmp.append(conference_room[value][i])
                    answer.append([tmp[0][0], tmp[-1][1]])
                    tmp = [] 
   
        if tmp == []: 
            pass
        
        else:
            answer.append([tmp[0][0], tmp[-1][1]]) # 회의예약이 가능한 구간의 시작시간이랑 끝나는시간을 넣어준다

        print("Room " + value + ":")
        print(len(answer), "available:")
        for i in range(len(answer)):
            if answer[i][0] == 9:
                answer[i][0] = "09" # 유일한 한 자릿수 9는 앞에 0을 붙혀서 출력
                print(answer[i][0]+"-"+str(answer[i][1]))
        
            else:
                print(str(answer[i][0])+"-"+str(answer[i][1]))
        
        if value == sorted(conference_room.keys())[-1]:
            break
        
        else:
            print("-----")