class Sld:
    def __init__(self, test='martin'):
        self.test = test
        # self.name = "peter"\
        xml = self.createSld()

    name = 'wave_height'
    scale = 0.01
    catNums = [1,2,3,4]
    colors = []
    _vals = dict(name = name,
                scale= scale,
                catNums = catNums,
                test= test
                )



    @classmethod
    def initvals(cls):
        return cls._vals

    def createSld(self, colors= None):
        if not colors:
            color = self.colors
        self.xml = f"""
    <?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld"
  xmlns:ogc="http://www.opengis.net/ogc"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld
 http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd" version="1.0.0">
  <NamedLayer>
    <Name>{self.name}</Name>
    <UserStyle>
      <FeatureTypeStyle>
        <Title>{input['styleName']}</Title>
        <Transformation>
          <ogc:Function name="ras:RasterAsPointCollection">
            <ogc:Function name="parameter">
              <ogc:Literal>data</ogc:Literal>
            </ogc:Function>
            <ogc:Function name="parameter">
              <ogc:Literal>scale</ogc:Literal>
              <ogc:Literal>{input['scale']}</ogc:Literal>
            </ogc:Function>
            <ogc:Function name="parameter">
              <ogc:Literal>emisphere</ogc:Literal>
              <ogc:Literal>True</ogc:Literal>
            </ogc:Function>
          </ogc:Function>
        </Transformation>
        <Rule>

          <ogc:Filter>
            <ogc:PropertyIsLessThan>
              <ogc:Function name="sqrt">
                <ogc:Add>
                  <ogc:Mul>
                    <ogc:PropertyName>{input['u']}</ogc:PropertyName>
                    <ogc:PropertyName>{input['u']}</ogc:PropertyName>
                  </ogc:Mul>
                  <ogc:Mul>
                    <ogc:PropertyName>{input['v']}</ogc:PropertyName>
                    <ogc:PropertyName>{input['v']}</ogc:PropertyName>
                  </ogc:Mul>
                </ogc:Add>
              </ogc:Function>
              <ogc:Literal>{input['filterCutoff']}</ogc:Literal>
            </ogc:PropertyIsLessThan>
          </ogc:Filter>

          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>
                extshape://narrow              
                </WellKnownName>
                <Fill>
                  <CssParameter name ="fill">

                    <ogc:Function name ="Categorize">
                      <ogc:Function name="sqrt">
                        <ogc:Add>
                          <ogc:Mul>
                            <ogc:PropertyName>{input['u']}</ogc:PropertyName>
                            <ogc:PropertyName>{input['u']}</ogc:PropertyName>
                          </ogc:Mul>
                          <ogc:Mul>
                            <ogc:PropertyName>{input['v']}</ogc:PropertyName>
                            <ogc:PropertyName>{input['v']}</ogc:PropertyName>
                          </ogc:Mul>
                        </ogc:Add>
                      </ogc:Function>
                     {categorize(input['catNums'], input['catColors'])}
                    </ogc:Function >

                  </CssParameter>
                </Fill>
                <Stroke>
                  <CssParameter name="stroke-width">{input['strokeWidth']}</CssParameter>
                  <CssParameter name="stroke">{input['strokeCol']}</CssParameter>
                </Stroke>
              </Mark>
              <Size>{input['markSize']}</Size>
              <Rotation>
                <ogc:Function name="toDegrees">
                  <ogc:Function name="atan2">
                    <ogc:PropertyName>{input['u']}</ogc:PropertyName>
                    <ogc:PropertyName>{input['v']}</ogc:PropertyName>
                  </ogc:Function>
                </ogc:Function>
              </Rotation>
            </Graphic>
          </PointSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
    """
        print(f"""mein name ist {cls.name} ich skaliere {cls.scale} nummern: {" ".join([str(e) for e in cls.catNums])}""")
        return f"""mein name ist {cls.name} ich skaliere {cls.scale} nummern: {" ".join([str(e) for e in cls.catNums])}"""
    @classmethod
    def writeSld(cls, outfile):
        sld = cls.createSLd()

        file = open(f'./{outfile}.xml', 'w')
        file.write(sld)
        file.close()




Sld.createSld()
k = Sld()