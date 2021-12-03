from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from model import FloorTiles 
from agent import vaccum, tile

COLORS = {"Dirty": "#76552B", "Clean": "#A8C0D3"}


def floor_portrayal(agent):
    if agent is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}

    if(isinstance(agent, tile)):
    	(x, y) = agent.pos
    	portrayal["x"] = x
    	portrayal["y"] = y
    	portrayal["Color"] = COLORS[agent.condition]

    elif(isinstance(agent, vaccum)):
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
        portrayal["Shape"] = "circle"
        portrayal["r"] = 1        

    return portrayal

canvas_element = CanvasGrid(floor_portrayal, 10, 10, 500, 500)

tree_chart = ChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)
pie_chart = PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)

model_params = {
	"height": UserSettableParameter("slider", "Height", 10, 100, 500, 1),
	"width": UserSettableParameter("slider", "Width", 10, 100, 500, 1),
    "density": UserSettableParameter("slider", "Dirt density", 0.65, 0.01, 1.0, 0.01),
    "numberVaccums": UserSettableParameter("slider", "Vaccum number", 1, 1, 10, 1),
    "maxT": UserSettableParameter("slider", "Max time", 120, 100, 700, 10),
}

server = ModularServer(FloorTiles, [canvas_element, tree_chart, pie_chart], "Vaccum cleaning", model_params)

server.launch()