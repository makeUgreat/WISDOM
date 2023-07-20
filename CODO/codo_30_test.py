korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    min_score = min(args)
    max_score = max(args)
    return min_score, max_score

def get_average(**kwargs):
    total_score = sum(kwargs.values())
    average_score = total_score / len(kwargs)
    return average_score

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))