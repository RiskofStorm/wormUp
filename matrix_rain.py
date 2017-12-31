import random as rd
import time


class MatrixRain:

    def __init__(self):
        self.alphabet = [chr(i) for i in range(0x30a0, 0x3100)]
        self.digit = [str(i) for i in range(0, 10)]
        self.model = self.alphabet + self.digit * 5

    def endless_matrix_rain(self, time_speed):
        rd.seed()
        screen_line = 70

        train = [rd.randint(0, len(self.model)-1) for _ in range(screen_line)]
        ind_model = [self.model[i] for i in train]

        space_model = list()
        for i in range(screen_line):
            if space_model.count(0) < rd.randint(5, 35):
                space_model.append(rd.randint(0, 1))
            else:
                space_model.append(1)

        final_model = list()
        for i in range(len(space_model)):
            if space_model[i] != 0:
                final_model.append(ind_model[i])
            else:
                final_model.append(' ')

        rd.shuffle(final_model)

        time.sleep(time_speed)

        print("\033[32m", *final_model, "\033[0m")

    def intro(self, time_sleep):
        print(' ')
        print(' ')
        print('\033[32m Wake up, Neo... \033[0m')
        time.sleep(4)
        print(' ')
        print("\033[32m The Matrix has You... \033[0m")
        time.sleep(4)
        print(' ')
        print('\033[32m Follow the white rabbit \033[0m')
        time.sleep(6)
        print(' ')
        print(' ')
        print('\033[32m Knock, knock, Neo. \033[0m')
        time.sleep(2)
        print(' ')
        print(' ')
        self.intro = self.endless_matrix_rain

    def start_change_seed_matrix(self):

        time_speed = round(rd.uniform(0.05, 0.1), 2)

        for i in range(100):
            self.intro(time_speed)
            self.endless_matrix_rain(time_speed)

        return self.start_change_seed_matrix()


enter_the_matrix = MatrixRain()
enter_the_matrix.start_change_seed_matrix()



