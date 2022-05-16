# 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방

def solution(record):
    answer = []
    # 입장 : "Enter [유저 아이디] [닉네임]"
    # 퇴장 : "Leave [유저 아이디]"
    # 변경 : "Change [유저 아이디] [닉네임]"
    # 닉네임 바꼈으면 이전 닉네임도 바뀐 닉네임으로 표시
    # 중복닉네임 허용
    id_dict = {}        # 유저아이디 : 닉네임 관리위한 딕셔너리
    
    for r in record:
        # 입장/퇴장/변경여부 구분
        if r.split()[0] == 'Enter':
            id_dict[r.split()[1]] =  r.split()[2]       # 유저아이디-닉네임 등록
            answer.append(r.split()[1] + '님이 들어왔습니다.')
        elif r.split()[0] == 'Leave':
            answer.append(r.split()[1] + '님이 나갔습니다.')
        elif r.split()[0] == 'Change':
            id_dict[r.split()[1]] =  r.split()[2]       # 닉네임 변경 
    
    for i in range(len(answer)):
        user_id = answer[i][:answer[i].index('님')]
        answer[i] = answer[i].replace(user_id, id_dict[user_id])        # 유저아이디를 닉네임으로 치환

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))