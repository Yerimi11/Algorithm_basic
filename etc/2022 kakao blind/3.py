def solution(users, emoticons):
    emoticon_cnt = len(emoticons)
    discounts = [10, 20, 30, 40]
    emo_discounts = [0] * emoticon_cnt
    max_result = [0, 0]

    def check_result(emo_discounts):
        nonlocal max_result
        result = [0, 0]
        for target_discount, budget in users:
            emo_plus = False
            charge = 0
            for idx, discount in enumerate(emo_discounts):
                if discount >= target_discount:
                    charge += int(emoticons[idx] * (100 - discount) / 100)
                    print("charge : ", charge)
                    if charge >= budget:
                        emo_plus = True
                        charge = 0
                        break
            if emo_plus:
                result[0] += 1
            else:
                result[1] += charge
        print("result: ", result)
        if max_result[0] < result[0]:
            max_result = result
        elif max_result[0] == result[0] and max_result[1] <= result[1]:
            max_result = result
        
    def find_discounts(i) :
        if i >= emoticon_cnt:
            print("emo_discounts: ", emo_discounts)
            check_result(emo_discounts)
            return
        for discount in discounts:
            emo_discounts[i] = discount
            find_discounts(i+1)

    find_discounts(0)
    return max_result


[[40, 10000], [25, 10000]]
[7000, 9000]
# [1, 5400]

[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
[1300, 1500, 1600, 4900]
# [4, 13860]