from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    user_dict = defaultdict(str)
    reported_name = defaultdict(int)
    finish_user = set()
    for name in report:
        user, report_user = name.split()
        if user not in user_dict:
            user_dict[user] = set()
            reported_name[user] = 0
        user_dict[user].add(report_user)
    for user_name in user_dict:
        for user in user_dict[user_name]:
            reported_name[user] = reported_name[user] + 1
            if (reported_name[user] >= k):
                finish_user.add(user)
                
    for k in id_list:
        num = 0
        for j in user_dict[k]:
            if j in finish_user:
                num+=1
        answer.append(num)
        

    return answer