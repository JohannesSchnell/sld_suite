class WaveHeight:
    layerName = 'wave_height_world'
    styleName = 'wave_height'
    #logic here is 'bigger than' so first val needs to be smaller than 0
    catNums=[-1,
             3,
             5,
             7,
             15]
    #1:1 mapping of Num and Colors length
    catColors = ['#1ce3ed',
                 '#148818',
                 '#ba5802',
                 '#ba0e02',
                 '#000000']

    _vals = dict(
        layerName = layerName,
        styleName = styleName,
        catNums = catNums,
        catColors = catColors
    )

    def initvals(self):
        print(self._vals)
        return (self._vals)

    @staticmethod
    def categorize(catColors, catNums):
        res = [f"""<ColorMapEntry color = {col} quantity = '{catNums[i]}'/>"""for i, col in enumerate(catColors)]
        return "\n".join(res)

    def createSld(self):
        return(f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <StyledLayerDescriptor xmlns="http://www.opengis.net/sld"
          xmlns:ogc="http://www.opengis.net/ogc"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld
         http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd" version="1.0.0">
          <NamedLayer>
            <Name>{self.layerName}</Name>
            <UserStyle>
              <FeatureTypeStyle>
                <Title>{self.styleName}</Title>
        
                <Rule>
                    <RasterSymbolizer>
                        <ColorMap extended = 'true'>
                    {self.categorize(self.catColors, self.catNums)}
                        </ColorMap>
                    </RasterSymbolizer>
                </Rule>
              </FeatureTypeStyle>
            </UserStyle>
          </NamedLayer>
        </StyledLayerDescriptor>   
        """)

    def printSld(self):
        print(self.createSld())

    def writeSld(self, outfile='current_world'):
        current = self.createSld()

        file = open(f'./xml/{outfile}.xml', 'w')
        file.write(current)
        file.close()