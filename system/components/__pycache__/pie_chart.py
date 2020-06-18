import matplotlib.pyplot as plt
from easygui import enterbox

labels = ['against', 'pro', 'neutral', 'unknown']


def plot():
    print("Are you a well supported leader?")
    against = enterbox("How many people are against you?")
    pro = enterbox("How many people voted for you?")
    neutral = enterbox("How many people decided to stay neutral?")
    unknown = enterbox("Any unknown?")
    sizes = [against, pro, neutral, unknown]
    explode = (0, 0.1, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()
