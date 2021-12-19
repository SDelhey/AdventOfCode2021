import numpy as np
filename = 'data.txt'


def part_1():
    days = 80
    with open(filename) as file:
        fishes = np.array(list(map(int, file.readlines()[0].split(','))))

        for i in range(days):
            for idx in range(len(fishes)):
                if fishes[idx] > 0:
                    fishes[idx] -= 1
                else:
                    fishes[idx] = 6
                    fishes = np.append(fishes, 8)

        print(len(fishes))


def part_2():
    days = 256
    with open(filename) as file:
        starting_fish = list(map(int, file.readlines()[0].split(',')))
        current_states = {
            0: starting_fish.count(0),
            1: starting_fish.count(1),
            2: starting_fish.count(2),
            3: starting_fish.count(3),
            4: starting_fish.count(4),
            5: starting_fish.count(5),
            6: starting_fish.count(6),
            7: starting_fish.count(7),
            8: starting_fish.count(8)
        }

        # Repeat once per 'day'
        for i in range(days):
            next_states = {
                0: current_states[1],
                1: current_states[2],
                2: current_states[3],
                3: current_states[4],
                4: current_states[5],
                5: current_states[6],
                6: current_states[7],
                7: current_states[8],
                8: current_states[0]
            }

            # Reset adult fish at 0 to 6
            next_states[6] += current_states[0]

            # Move value of new_states to current_states, reset value new_states
            current_states = next_states

        print(current_states)
        print(sum(current_states.values()))


if __name__ == '__main__':
    part_1()
    part_2()
