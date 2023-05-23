from sld import Heatmap
import os

print(os.getcwd())

wave_height = Heatmap(layerName="waveh", styleName="waveh", catNums=[-1, 2, 4, 7],
                      catColors=['#1ce3ed',
                                 '#148818',
                                 '#ba5802',
                                 '#ba0e02'])
wave_height.printSld()
wave_height.writeSld("345")
