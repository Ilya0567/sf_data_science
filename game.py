import numpy as np
def random_predict() -> int:
    """_summary_

    Returns:
        int: _description_
    """
    predict = np.random.randint(1, 100)
    count = 0
    low = 1
    high = 99
    while True:
        count += 1 
        guess = (low + high) // 2
        if guess > predict:
            high = guess - 1
        elif guess < predict:
            low = guess + 1
        if predict == guess:
            break
    return count

def scope():
    l = []
    for i in range(1000):
        l.append(random_predict())
    print(f"Averege  frequency {sum(l)/len(l)}")
    return sum(l)/len(l)


if __name__ == '__main__':
    scope()