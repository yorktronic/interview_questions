class TempTracker(object):
    # temps: dictionary of temperatures and their counts
    # max, min, mode, mean, sum: statistics based on temps

    def __init__(self, temps={}):
        self.temps = temps
        if temps:
            self.update_stats()
        else:
            self.max = None
            self.min = None
            self.mode = None
            self.mean = None
            self.sum = None

    def update_stats(self):
        self.max = self.get_max()
        self.min = self.get_min()
        self.mode = self.get_mode()
        self.mean = self.get_mean()
        self.sum = self.sum()

    def print_stats(self):
        print({'Min': self.min, 'Max': self.max, 'Sum':self.sum, 'Mean':self.mean, 'Mode':self.mode})

    def insert(self, temp):
        if temp in self.temps:
            self.temps[temp] += 1
        else:
            self.temps[temp] = 1

    def sum(self):
        return sum(self.temps.keys())

    def get_max(self):
        return max(self.temps.keys())

    def get_min(self):
        return min(self.temps.keys())

    def get_mean(self):
        return self.sum() / float(len(self.temps))

    def get_mode(self):
        max = (0,0)
        for key, value in self.temps.items():
            if value > max[1]:
                max = (key, value)
            else:
                continue

        return max[0]
