import ConstDF
import NodesRelations
import construct_allnodes
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_reusable_components as drc
import plotly.express as px
import Listsuccessorpredecesseurs
from dash.dependencies import Input, Output, State
import dash_cytoscape as cyto
import json

# Load extra layouts
cyto.load_extra_layouts()

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

metadata=ConstDF.readbd()
default_elements=NodesRelations.elements(metadata)
list_dict_successors_predecessors=Listsuccessorpredecesseurs.successors_predecesseurs(metadata['table_columns_relations'])
# genesis_node ={}
joined_list = [*list_dict_successors_predecessors[4], *list_dict_successors_predecessors[5]]
default_elements=joined_list
print(list_dict_successors_predecessors)
# {'data': {'id': '108082478497335384404', 'label': 'User #84404'}, 'classes': 'genesis'}
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    },
    'json-output': {
        'overflow-y': 'scroll',
        'height': 'calc(50% - 25px)',
        'border': 'thin lightgrey solid'
    },
    'tab': {'height': 'calc(98vh - 80px)'},
}
default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': '#BFD7B5',
            'content': 'data(label)'
        }
    },
    {
        "selector": 'edge',
        'style': {
            "curve-style": "bezier",
            'background-color': '#BFD7B5',
            "opacity": 1.0,
            'z-index': 5000
        }
    },
    {
        'selector': '.followerNode',
        'style': {
            'background-color': '#0074D9'
        }
    },
    {
        'selector': '.ffNodes',
        'style': {
            'background-color': '#407294'
        }
    },
    {
        'selector': '.followerEdge',
        "style": {
            "mid-target-arrow-color": "blue",
            "mid-target-arrow-shape": "vee",
            "line-color": "#0074D9"
        }
    },
    {
        'selector': '.followingNode',
        'style': {
            'background-color': '#FF4136'
        }
    },
    {
        'selector': '.followingEdge',
        "style": {
            "mid-target-arrow-color": "red",
            "mid-target-arrow-shape": "vee",
            "line-color": "#FF4136",
        }
    },
    {
        "selector": '.genesis',
        "style": {
            'background-color': '#B10DC9',
            "border-width": 2,
            "border-color": "purple",
            "border-opacity": 1,
            "opacity": 1,

            "label": "data(label)",
            "color": "#B10DC9",
            "text-opacity": 1,
            "font-size": 12,
            'z-index': 9999
        }
    },
    {
        'selector': ':selected',
        "style": {
            "border-width": 2,
            "border-color": "black",
            "border-opacity": 1,
            "opacity": 1,
            "label": "data(label)",
            "color": "black",
            "font-size": 12,
            'z-index': 9999
        }
    }
]

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True


# Define the app
app.layout = html.Div()

app.layout = html.Div(children=[
    html.Div(className='row',  # Define the row element
             children=[
                 html.Div(className='four columns div-user-controls',
                          children=[
                              html.H2('Magic Automatic SQL Queries Generator'),
                              html.H5('''Visualising the data base with Plotly - Dash'''),
                              html.P('''Select the relations you would like to keep.'''),
                              dcc.Dropdown(
                                  options=[
                                      {'label': 'New York City', 'value': 'NYC'},
                                      {'label': u'Montréal', 'value': 'MTL'},
                                      {'label': 'San Francisco', 'value': 'SF'}
                                  ],
                                  value=['MTL', 'SF'],
                                  multi=True
                              ),
                              # dcc.Checklist(
                              #     options=[
                              #         {'label': 'New York City', 'value': 'NYC'},
                              #         {'label': u'Montréal', 'value': 'MTL'},
                              #         {'label': 'San Francisco', 'value': 'SF'}
                              #     ],
                              #     value=['MTL', 'SF']
                              # ),
                              dcc.Tabs(id='tabs', children=[
                                  dcc.Tab(label='Control Panel', children=[
                                      drc.NamedDropdown(
                                          name='Layout',
                                          id='dropdown-layout',
                                          options=drc.DropdownOptionsList(
                                              'random',
                                              'grid',
                                              'circle',
                                              'concentric',
                                              'breadthfirst',
                                              'cose'
                                          ),
                                          value='grid',
                                          clearable=False
                                      ),
                                      drc.NamedRadioItems(
                                          name='Expand',
                                          id='radio-expand',
                                          options=drc.DropdownOptionsList(
                                              'predecessors',
                                              'successors',
                                              'All for the node'
                                          ),
                                          value='All for the node'
                                      )

                                  ]),

                                  dcc.Tab(label='JSON', children=[
                                      html.Div(style=styles['tab'], children=[
                                          html.P('Node Object JSON:'),
                                          html.Pre(
                                              id='tap-node-json-output',
                                              style=styles['json-output']
                                          ),
                                          html.P('Edge Object JSON:'),
                                          html.Pre(
                                              id='tap-edge-json-output',
                                              style=styles['json-output']
                                          )
                                      ])
                                  ])
                              ]),

                          ]

                          ),  # Define the left element
                 html.Div(className='eight columns div-for-charts bg-grey',
                          children=[
                              cyto.Cytoscape(
                                          # id='cytoscape-two-nodes',
                                          #id='cytoscape-callbacks-1',
                                          id='cytoscape-event-callbacks-1',
                                          stylesheet=default_stylesheet,
                                          # layout={'name': 'circle'},
                                          layout={
                                              'name': 'cose',
                                              'idealEdgeLength': 100,
                                              'nodeOverlap': 20,
                                              'refresh': 20,
                                              'fit': True,
                                              'padding': 30,
                                              'randomize': False,
                                              'componentSpacing': 100,
                                              'nodeRepulsion': 400000,
                                              'edgeElasticity': 100,
                                              'nestingFactor': 5,
                                              'gravity': 80,
                                              'numIter': 1000,
                                              'initialTemp': 200,
                                              'coolingFactor': 0.95,
                                              'minTemp': 1.0
                                          },
                                  responsive=True,
                                          # layout={'name': 'circle', "nodeDimensionsIncludeLabels":False, "startAngle": 3 / 2 * math.pi},
                                          # style={'width': '100%', 'height': '900px'},
                                          style={'width': '100%', 'height': '100vh'},
                                          elements=default_elements
                                      ),
                                # html.Pre(id='cytoscape-tapNodeData-json', style=styles['pre']),
                                html.P(id='cytoscape-tapNodeData-output'),
                                html.P(id='cytoscape-mouseoverNodeData-output'),
                                dcc.Textarea(
                                    placeholder='Enter a value...',
                                    value='This is a TextArea component',
                                    style={'width': '70%'}
                                )
                          ])  # Define the right element
             ])
])

# @app.callback(Output('cytoscape-tapNodeData-json', 'children'),
#               [Input('cytoscape-event-callbacks-1', 'tapNodeData')])
# def displayTapNodeData(data):
#     return json.dumps(data, indent=2)

# @app.callback(Output('cytoscape-tapNodeData-output', 'children'),
#                   [Input('cytoscape-event-callbacks-1', 'tapNodeData')])
# def displayTapNodeData(data):
#     if data:
#         return "You recently clicked/tapped the city: " + data['label']

@app.callback(Output('tap-node-json-output', 'children'),
              [Input('cytoscape-event-callbacks-1', 'tapNode')])
def display_tap_node(data):
    return json.dumps(data, indent=2)

@app.callback(Output('tap-edge-json-output', 'children'),
              [Input('cytoscape-event-callbacks-1', 'tapEdge')])
def display_tap_edge(data):
    return json.dumps(data, indent=2)

@app.callback(Output('cytoscape-mouseoverNodeData-output', 'children'),
                    Input('cytoscape-event-callbacks-1', 'mouseoverNodeData'))
def displayMouseonNodeData(data):
    if data:
        return "You are hovering on the node: " + data['label']

@app.callback(Output('cytoscape-event-callbacks-1', 'layout'),
              [Input('dropdown-layout', 'value')])
def update_cytoscape_layout(layout):
    return {'name': layout}


@app.callback(Output('cytoscape-event-callbacks-1', 'elements'),
              Output('cytoscape-event-callbacks-1','stylesheet'),
              [Input('cytoscape-event-callbacks-1', 'tapNodeData')],
              [State('cytoscape-event-callbacks-1', 'elements'),
               State('radio-expand', 'value')])

def generate_elements(nodeData, elements, expansion_mode):
    if not nodeData:
        return default_elements, default_stylesheet

    # If the node has already been expanded, we don't expand it again
    # if nodeData.get('expanded'):
    #     return elements

    # This retrieves the currently selected element, and tag it as expanded
    for element in elements:
        if nodeData['id'] == element.get('data').get('id'):
            element['data']['expanded'] = True
            break

    all_nodes=construct_allnodes.allnodes_of_a_node(list_dict_successors_predecessors[2].get(nodeData['id'])
                                                    ,list_dict_successors_predecessors[0].get(nodeData['id']))

    # if((list_dict_successors_predecessors[2].get(nodeData['id']) is None)
    #     and list_dict_successors_predecessors[0].get(nodeData['id']) is not None):
    #     all_nodes=list_dict_successors_predecessors[0].get(nodeData['id'])
    # elif((list_dict_successors_predecessors[0].get(nodeData['id']) is None) and
    #       (list_dict_successors_predecessors[2].get(nodeData['id']) is not None)):
    #     all_nodes=list_dict_successors_predecessors[2].get(nodeData['id'])
    # elif((list_dict_successors_predecessors[0].get(nodeData['id']) is None) and
    #       (list_dict_successors_predecessors[2].get(nodeData['id']) is None)):
    #     all_nodes=None
    # else:
    #     all_nodes=list_dict_successors_predecessors[2].get(nodeData['id'])+\
    #     list_dict_successors_predecessors[0].get(nodeData['id'])

    print(all_nodes)

    # [x for x in L if x is not None]

    # print(list_dict_successors_predecessors[2].get(nodeData['id']))
    # print(list_dict_successors_predecessors[0].get(nodeData['id']))
    # print(type(list_dict_successors_predecessors[3].get(nodeData['id'])))
    # print(type(list_dict_successors_predecessors[1].get(nodeData['id'])))

    if expansion_mode == 'predecessors':

        followers_nodes = list_dict_successors_predecessors[2].get(nodeData['id'])
        followers_arcs = list_dict_successors_predecessors[3].get(nodeData['id'])

        if followers_nodes:
            for node in followers_nodes:
                node['classes'] = 'followerNode'
            elements.extend(followers_nodes)

        if followers_arcs:
            for follower_edge in followers_arcs:
                follower_edge['classes'] = 'followerEdge'
            elements.extend(followers_arcs)

    elif expansion_mode == 'successors':

        following_nodes = list_dict_successors_predecessors[0].get(nodeData['id'])
        following_arcs = list_dict_successors_predecessors[1].get(nodeData['id'])

        if following_nodes:
            for node in following_nodes:
                # if node['data']['id'] != genesis_node['data']['id']:
                    node['classes'] = 'followingNode'
                    elements.append(node)

        if following_arcs:
            for follower_edge in following_arcs:
                follower_edge['classes'] = 'followingEdge'
            elements.extend(following_arcs)

    elif expansion_mode == 'All for the node':
        if all_nodes:
            for node in all_nodes:
                node['classes'] ='ffNodes'
                # elements.append(node)
                for i in range(0, len(elements)):
                    if(elements[i].get('data').get("id") == node['data']['id']):
                        elements[i]=node
                        # elements[i]['classes']='ffNodes'
                        break

        for element in elements:
            if (element.get('classes')!='ffNodes'):
                element['classes'] ='notSelect'
                element['selectable']=False
            else:
                element['selectable']=True


        for element in elements:
             if(element['selectable']==False):
                print(element)

    def new_stylesheet(stylesheet):
        stylesheet.append(
            {
            'selector': '.notSelect',
                'style': {
                    'background-color': '#dc7699'
                }
            }
        )
        # print('This is {}'.format(stylesheet))
        return stylesheet


    stylesheet=new_stylesheet(default_stylesheet)
    # print('This is {}'.format(stylesheet))

    return elements, stylesheet

if __name__ == '__main__':
    # metadata = ConstDF.readbd()
    # elements_graph = NodesRelations.elements(metadata)
    app.run_server(host='0.0.0.0', port=8080, debug=True)


