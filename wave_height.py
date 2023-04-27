input = dict(
    layerName = 'waves_height',
    styleName = 'vhm0',
    nums = [
        -1,
        3,
        5,
        7,
        9

    ],
    colors = [
        '#1ce3ed',
        '#148818',
        '#ebab36',
        '#ba0e02',
        '#000000'
    ]
)

def categories(nums, colors):
    res = [f"<ColorMapEntry color = '{colors[i]}' quantity = '{nums[i]}'/>" for i in range(len(nums))]
    "\n".join(res)
    return "\n".join(res)

def wave_height(input):
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
            
                    <Rule>
                        <RasterSymbolizer>
                            <ColorMap extended = 'true'>
                            {categories(input['nums'], input['colors'])}
                            </ColorMap>
                        </RasterSymbolizer>
                    </Rule>
                    
                  </FeatureTypeStyle>
                </UserStyle>
              </NamedLayer>
            </StyledLayerDescriptor>

        """
    )

xml = wave_height(input)
file = open('wave_height.xml', 'w')
file.write(xml)
file.close()