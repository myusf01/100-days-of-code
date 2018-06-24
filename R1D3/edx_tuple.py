#There are codes for exercises in edX


def get_Da(atpl):
        nums = ()
        words = ()
        for t in atpl:
            nums = nums + (t[0],)
            if t[1] not  in words:
                words = words + (t[1],)
        max_nums = max(nums)
        min_nums = min(nums)
        unq_words = len(words)
        return (min_nums,max_nums,unq_words)

def oddTuples(aTup):
    tp = ()
    for t in range(len(aTup)):
        if t % 2 == 0:
            tp = tp + (aTup[t],)
    return tp
x = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(x))