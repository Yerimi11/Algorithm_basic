def solution(survey, choices):
    # 사전순
    personal = {"A":0, "N":0, "C":0, "F":0, "J":0, "M":0, "R":0, "T":0}
    scores = {"1":3, "7":3, "2":2, "6":2, "3":1, "5":1, "4":0}
    answer = ''
    
    for i in range(len(survey)): # x = "AN"
        if choices[i] > 4:
            personal[survey[i][1]] += scores[choices[i]]
        else:
            personal[survey[i][0]] += scores[choices[i]]
    
    print(personal)
    return answer

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])