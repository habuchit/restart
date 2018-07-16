import random

def jyanken_01():
    print('あなたの手を教えて下さい。1 グー 2 チョキ 3 パー')
    yourhands = input('>> ')    
    cpunum = random.randrange(3) +1
    if yourhands == '1':
        print('あなたの手はグーです。')
    elif yourhands == '2':
        print('あなたの手はチョキです。')
    elif yourhands == '3':
        print('あなたの手はパーです。')
    if cpunum == 1:
        print('相手の手はグーです。')
        if yourhands == '1':
            print('引き分けです。')
            jyanken_01()
        elif yourhands == '2':
            print('あなたの負けです。')
        elif yourhands == '3':
            print('あなたの勝ちです。')
    elif cpunum == 2:
        print('相手の手はチョキです。')
        if yourhands == '1':
            print('あなたの勝ちです。')
        elif yourhands == '2':
            print('引き分けです。')
            jyanken_01()
        elif yourhands == '3':
            print('あなたの負けです。')
    elif cpunum == 3:
        print('相手の手はパーです。')
        if yourhands == '1':
            print('あなたの負けです。')
        elif yourhands == '2':
            print('あなたの勝ちです。')
        elif yourhands == '3':
            print('引き分けです。')
            jyanken_01()


jyanken_01()
