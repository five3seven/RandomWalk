from random import randint, random
import turtle

class randomWalk:
    def __init__(self, moves):
        self.moves = moves

    def prob(self):
        prb = []
        for j in range(1000):
            S = 0
            for i in range(self.moves):
                u = randint(1, 8)
                if u == 1:
                    S += 1
            prb.append(S/self.moves)
        return prb

    def move(self, trtl, step=5):
        u = randint(1, 8)
        x = trtl.pos()[0]
        y = trtl.pos()[1]
        step += random()
        if u == 1:
            trtl.goto(x + step, y)
        elif u == 2:
            trtl.goto(x, y + step)
        elif u == 3:
            trtl.goto(x, y - step)
        elif u == 4:
            trtl.goto(x - step, y)
        elif u == 5:
            trtl.goto(x - step, y - step)
        elif u == 6:
            trtl.goto(x + step, y + step)
        elif u == 7:
            trtl.goto(x - step, y + step)
        elif u == 8:
            trtl.goto(x + step, y - step)

    def rWalk(self, size=2, bgcolor='#2A2A2A'):
        try:
            colors = ['#e3f252', '#07f9da', '#ff1a00', '#e6e6fa', '#de03f9', '#10e4ae', '#150efd', '#ff80ed']
            trcolor = colors[randint(0, len(colors) - 1)]

            screen = turtle.Screen()
            screen.bgcolor(bgcolor)
            screen.screensize(3000, 3000)

            pr = turtle.Turtle()
            pr.pensize(size)
            pr.speed(0)
            pr.color(trcolor)
            pr.hideturtle()

            for i in range(0, self.moves):
                u = randint(0, 500)
                if u == 0:
                    u = random() + randint(100, 200)
                    self.move(pr, step=u)
                else:
                    u = randint(1, 4)
                    self.move(pr, step=u)

            turtle.done()
        except:
            pass

    def histogram(self):
        from matplotlib import pyplot as plt
        import numpy as np

        plt.hist(self.prob(), bins = 20, log=True)

        median = np.median(self.prob())
        plt.axvline(median, color='#FF1A00', label='Probability Median')
        plt.title('Random Walk')
        plt.xlabel('Probability')
        plt.ylabel('Frequency')
        plt.show()

if __name__ == '__main__':
    randomWalk(int(input('Number of steps:\n'))).rWalk()