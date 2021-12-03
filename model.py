from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from agent import tile, vaccum

class FloorTiles(Model):

    def __init__(self, height=100, width=100, density=0.65, numberVaccums=1, maxT = 100):
        
        # Set up model objects
        self.num_vacs = numberVaccums
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(height, width, torus=False)
        self.tm = 0
        self.maxT = maxT


        self.datacollector = DataCollector(
            {
                "Dirty": lambda m: self.count_type(m, "Dirty"),
                "Clean": lambda m: self.count_type(m, "Clean"),
            }
        )

        startingPos = [(x,y) for y in range(height) for x in range(width) if y == 1 and x == 1]

        for i in range(numberVaccums):
            agent = vaccum(i, (1,1), self)
            self.schedule.add(agent)
            self.grid.place_agent(agent, (1,1))


        # Place a cell according to probability
        for (contents, x, y) in self.grid.coord_iter():
            new_tile = tile((x, y), self)
            if self.random.random() < density:
                new_tile.condition = "Dirty"
            self.schedule.add(new_tile)
            self.grid.place_agent(new_tile, (x, y))
            
    

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

        if self.count_type(self, "Dirty") == 0:
            self.running = False
        if self.tm >= self.maxT:
            print("Maxxed time, stopped")
            self.running = False
        else:
            self.tm += 1

    @staticmethod
    def count_type(model, cond):
        count = 0
        for ft in model.schedule.agents:
            if(isinstance(ft, tile)):
                if ft.condition == cond:
                    count += 1
        return count





