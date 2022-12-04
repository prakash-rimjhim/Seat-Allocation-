from array import *


class FlightSeatAllocation:
    def __init__(self):
        self.passenger_count = 30
        self.cols_rows_list = [[3, 2], [4, 3], [2, 3], [3, 4]]
        self.seating_arrangement = []
        self.counter = 0
        self.max_row_count = 0
        self.empty_seat = -1
        for l in self.cols_rows_list:
            c = l[0]
            r = l[1]
            grid = []
            if (self.max_row_count < r):
                self.max_row_count = r
            for i in range(r):
                grid_row = []
                for j in range(c):
                    grid_row.append(self.empty_seat)
                grid.append(grid_row)
            self.seating_arrangement.append(grid)

    def seat(self):
        self.seat_aisle()
        self.seat_window()
        self.seat_middle()
        # return self.seating_arrangement

    def seat_aisle(self):
        seat_group_count = len(self.seating_arrangement)

        if (seat_group_count > 1):
            for i in range(self.max_row_count):
                if (self.counter >= self.passenger_count):
                    break

                for j in range(seat_group_count):
                    if (self.counter >= self.passenger_count):
                        break

                    seat_group = self.seating_arrangement[j]
                    if (i < len(seat_group)):
                        r = seat_group[i]
                        if (j == 0):
                            right_column_index = len(seat_group[0]) - 1
                            if (right_column_index > 0):
                                self.counter = self.counter + 1
                                r[right_column_index] = self.counter
                        elif (j == seat_group_count - 1):
                            right_column_index = len(seat_group[0]) - 1
                            if (right_column_index > 0):
                                self.counter = self.counter + 1
                                r[0] = self.counter
                        else:
                            seat_count = len(r)
                            if (seat_count == 1):
                                self.counter = self.counter + 1
                                r[0] = self.counter
                            else:
                                self.counter = self.counter + 1
                                r[0] = self.counter
                                self.counter = self.counter + 1
                                r[seat_count - 1] = self.counter

    def seat_window(self):
        seat_group_count = len(self.seating_arrangement)

        if (seat_group_count > 1):
            for i in range(self.max_row_count):
                if (self.counter >= self.passenger_count):
                    break

                for j in range(seat_group_count):
                    if (self.counter >= self.passenger_count):
                        break

                    seat_group = self.seating_arrangement[j]
                    if (i < len(seat_group)):
                        row = seat_group[i]
                        if (j == 0):
                            self.counter = self.counter + 1
                            row[0] = self.counter
                        elif (j == seat_group_count - 1):
                            self.counter = self.counter + 1
                            row[-1] = self.counter

    def seat_middle(self):
        seat_group_count = len(self.seating_arrangement)
        for i in range(self.max_row_count):
            if (self.counter >= self.passenger_count):
                break
            for seat_group in self.seating_arrangement:
                if (self.counter >= self.passenger_count):
                    break
                if (i < len(seat_group)):
                    r = seat_group[i]
                    seat_count = len(r)
                    for c in range(seat_count):
                        if (self.counter >= self.passenger_count):
                            break
                        if (r[c] == self.empty_seat):
                            self.counter = self.counter + 1
                            r[c] = self.counter

    def printSA(self):
        print(self.seating_arrangement)


if __name__ == '__main__':
    f = FlightSeatAllocation()
    f.seat()
    f.printSA()





