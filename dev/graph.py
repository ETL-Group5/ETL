import plotly.express as px
import dash
import dash_cytoscape as cyto
import dash_html_components as html
#import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
#from sklearn.manifold import TSNE
#import umap
#import json

def create_graph() :
    return 0

import dash
import dash_cytoscape as cyto
import dash_html_components as html

##app = dash.Dash(__name__)
app = dash.Dash()
app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '400px'},
        elements=[
            {'data': {'id': 'commandes', 'label': 'commandes'}, 'position': {'x': 75, 'y': 75}},
            {'data': {'id': 'details_commandes', 'label': 'details_commandes'}, 'position': {'x': 200, 'y': 200}},
            {'data': {'id': 'produits', 'label': 'produits'}, 'position': {'x': 20, 'y': 20}},
            {'data': {'source': 'commandes', 'target': 'details_commandes'}},
            {'data': {'source': 'details_commandes', 'target': 'produits'}}
        ]
    )
])
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# print(elements_graph)
# app = dash.Dash()
# app.layout = html.Div([
#     cyto.Cytoscape(
#         # id='cytoscape-two-nodes',
#         id='cytoscape-layout-1',
#         layout={'name': 'circle'},
#         # layout={'name': 'circle', "nodeDimensionsIncludeLabels":False, "startAngle": 3 / 2 * math.pi},
#         # style={'width': '100%', 'height': '900px'},
#         style={'width': '100%', 'height': '100vh'},
#         elements=elements_graph
#     )
# ])

if __name__ == '__main__':
    #app.run_server(host='0.0.0.0', port=8080, debug=True)
    app.run_server(debug=True)

