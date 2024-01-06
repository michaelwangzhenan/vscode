import json
import plotly.express as px


def get_data():
    # file = "data/eq_data_1_day_m1.json"
    file = "data/eq_data_7_day_m1.json"
    with open(file) as f:
        content = json.load(f)

    metadata = content['metadata']
    features = content['features']

    print(metadata['count'])
    print(len(features))

    print(px.colors.named_colorscales())

    mags, titles, lons, lats = [], [], [], []
    for feature in features:
        mags.append(feature['properties']['mag'])
        titles.append(feature['properties']['title'])
        lons.append(feature['geometry']['coordinates'][0])
        lats.append(feature['geometry']['coordinates'][1])

    return mags, titles, lons, lats


def draw(inputs):
    fig = px.scatter(x=inputs[2],
                     y=inputs[3],
                     labels={"x": "longitude", "y": "latitude"},
                     range_x=[-200, 200],
                     range_y=[-90, 90],
                     width=800,
                     height=800,
                     title="Earthquake Scatter",
                     hover_name=inputs[1],
                     color=inputs[0],
                     size=inputs[0],
                     size_max=10
                     )
    # fig.write_html("eq.html")
    fig.show()


draw(get_data())
