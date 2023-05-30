class DepthLine:
    layerName = ''
    layerStyle = ''
    _vals = dict(

    )

    def initvals(self):
        print(self._vals)
        return (self._vals)

    @staticmethod
    def categorize(catColors, catNums):
        res = [f"""<ColorMapEntry color = {col} quantity = '{catNums[i]}'/>""" for i, col in enumerate(catColors)]
        return "\n".join(res)

    def createSld(self):
        return f"""
                <?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor version="1.0.0" 
 xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd" 
 xmlns="http://www.opengis.net/sld" 
 xmlns:ogc="http://www.opengis.net/ogc" 
 xmlns:xlink="http://www.w3.org/1999/xlink" 
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <NamedLayer>
    <Name>default_line</Name>
    <UserStyle>  
      <Title>Blue Line</Title>
      <FeatureTypeStyle>

        
        <Rule>
          <Name>rule1</Name>
          
          
          
        <ogc:Filter>
          <ogc:PropertyIsEqualTo>
            <ogc:PropertyName>z</ogc:PropertyName>
              <ogc:Literal>-15</ogc:Literal>
          </ogc:PropertyIsEqualTo>
        </ogc:Filter>
        
          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">#000000</CssParameter>
              <CssParameter name="stroke-width">5</CssParameter>
            </Stroke>
          </LineSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>

                """

    def printSld(self):
        print(self.createSld())

    def writeSld(self, outfile=None):
        sld = self.createSld()

        with open(f'./xml/{outfile or self.layerName}.xml', 'w+') as file:
            file.write(sld)
