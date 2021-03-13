import copy
import random
# Consider using the modules imported above.


class Hat:

    # initialse a list of coloured balls
    def __init__(self, **balls):  # use **kwargs to create dict with values
        self.contents = []
        for ball in balls:  # loop through each colour
            x = balls[ball]  # number of that colour
            while x > 0:  # loop through x many times
                self.contents.append(ball)  # and append that colour to context
                x -= 1

    # draw x many balls from the contents bag
    def draw(self, number):
        thisdraw = []
        # first check if the number is greater than the number of balls
        if number > len(self.contents):
            thisdraw = self.contents
            self.contents = []
        else:
            #hat = self.contents.copy()
            while number > 0:  # loop through x many times
                index = random.randrange(0, len(self.contents))
                thisdraw.append(self.contents[index])
                self.contents.pop(index)
                number -= 1
        thisdraw.sort()  # sort to pass test
        return thisdraw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    x = num_experiments
    passes = 0
    while x > 0:  # loop through the number of experiments
        thishat = copy.deepcopy(hat)
        thisdraw = thishat.draw(num_balls_drawn)  # get a draw
        i = True  # var to store whether this run has the number of balls
        for ball in expected_balls:  # for each expected ball
            # check if the ballcount is less than expected
            if thisdraw.count(ball) < expected_balls[ball]:
                i = False
        # if i wasn't set to false during the check
        if i == True:
            passes += 1  # then this run passed

        x -= 1

    # passes over the total number of experiments gives the ratio
    return passes/num_experiments


hat = Hat(red=2, green=2)
probability = experiment(hat=hat,
                         expected_balls={"red": 1, "green": 1},
                         num_balls_drawn=2,
                         num_experiments=5)
print(probability)
