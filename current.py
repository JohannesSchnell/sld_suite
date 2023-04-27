input = dict(
    layerName = 'current_world',
    styleName = 'current_dir',
    scale = 0.01,
    u = 'uo',
    v = 'vo',
    filterCutoff = 3,
    catNums = [
        0.5,
        0.75,
        1,
        1.25,
        1.5,
        1.75,
        2,
        2.5
    ],
    catColors = [
        '#ffffff',
        '#1ce3ed',
        '#2040f7',
        '#148818',
        '#e2f720',
        '#f7b320',
        '#f77a20',
        '#f73620',
        '#000000'
    ],
    strokeWidth = 0.6,
    strokeCol = '#ffffff',
    markSize = 25

)


def categorize(nums, colors):
    res = [f"<ogc:Literal>{x}</ogc:Literal>" for y in zip(colors, nums) for x in y]+ [f"<ogc:Literal>{colors[-1]}</ogc:Literal>"]
    return "\n".join(res)



def current_dir(input):
    return(f"""
    <?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld"
  xmlns:ogc="http://www.opengis.net/ogc"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld
 http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd" version="1.0.0">
  <NamedLayer>
    <Name>{input['layerName']}</Name>
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
    """)

xml = current_dir(input)
file = open('current.xml', 'w')
file.write(xml)
file.close()