import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_reusable_components as drc
import plotly.express as px
from dash.dependencies import Input, Output, State
import json


import dash_cytoscape as cyto

import Query
import Listsuccessorpredecesseurs
import ConstDF
import NodesRelations
import construct_allnodes


#functions to call
metadata=ConstDF.readbd()
default_elements=NodesRelations.elements(metadata)
list_dict_successors_predecessors=Listsuccessorpredecesseurs.successors_predecesseurs(metadata['table_columns_relations'])
joined_list = [*list_dict_successors_predecessors[4], *list_dict_successors_predecessors[5]]
default_elements=joined_list
default_elements=construct_allnodes.set_all_nodes_arcs(default_elements)
list_relations=construct_allnodes.set_list_relations([],'')
relations_drop_menu=[]




#### VARIABLES / STYLE

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
            'background-color': '$secondary',
            'content': 'data(label)'
        }
    },
    {
        "selector": 'edge',
        'style': {
            "curve-style": "bezier",
            'background-color': '$secondary',
            "opacity": 0.75,
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
            'background-color': '#2c3e50',
            'opacity' : '1'
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
            "border-width": 3,
            "border-color": "#2c3e50",
            "border-opacity": "1!important",
            "background-color" : "#18bc9c",
            "opacity": 1,
            "label": "data(label)",
            "color": "black",
            'z-index': 9999,
            'font-weight' : '900'
        }
    }
]




APP_NAME = "SQL Magic Query Generator"
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
ITEMS = [
                dbc.DropdownMenuItem("Fonctionnalités", header=True),
                dbc.DropdownMenuItem("Visualiser requête", href="#"),
                dbc.DropdownMenuItem("Query Builder", href="#"),
                dbc.DropdownMenuItem("Faire du pain", href="#"),
            ]
LINK1 = [dbc.NavLink("Query Builder")]
FA1 = html.I(className='fas fa-chevron-right mr-3')
SIDEBAR_STYLE = {
    "position": "relative",
    "top": 0,
    "left": 0,
    "bottom": 0,
    # "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "height" : "100%"
}
CONTENT_STYLE = {
    # "margin-left": "18rem",
    # "margin-right": "2rem",
    "padding": "2rem 1rem",
}
SECTION1_STYLE = {
    "height": "auto"
}
WIDTH100 = {
    "width" : "100%"
}



# test_modal = dbc.Row(
#     [
#     dbc.Col(html.Div("One of three columns")),
#     dbc.Col(html.Div("One of three columns")),
#     dbc.Col(html.Div("One of three columns"))
#     ])


dropdown_layout_items = [
                dbc.DropdownMenuItem("First"),
                dbc.DropdownMenuItem("Second"),
]

navbar2 = \
dbc.Row(
    [
    dbc.Col(
    dbc.Navbar([
        html.Img(src=PLOTLY_LOGO, height="30px"),
        dbc.NavbarBrand(APP_NAME, className="ml-2"),

        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Query Builder", disabled=True))
        ],navbar=True, horizontal='end'),
        dbc.DropdownMenu(
            ITEMS, label="Fonctionnalités", color="primary", className="m-1"
        ),
    ],
    color="primary",
    className="navBarContainer",
    dark=True,
    ),width=12
    )
    ],align="center",
     no_gutters=True,
)

section1 = dbc.Row(
    [
        dbc.Col(
            html.Div(
    [
        html.H2("StagBI25", className="display-5"),
        html.Hr(),
        html.P("Graph view : ", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Full size", href="/page-1", id="page-1-link"),
                dbc.NavLink("Reduced", href="/page-2", id="page-2-link"),
                dbc.NavLink("Circle", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        html.P("Schema connexion : ", className="lead"),
html.Div(
    [
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("Host", addon_type="prepend"),
                dbc.Input(placeholder="127.25.94.52:8080"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.Input(placeholder="User Identifient"),
                dbc.InputGroupAddon("Id", addon_type="append"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("Pass", addon_type="prepend"),
                dbc.Input(placeholder="Alcyon#Dedale68", type="number"),
            ],
            className="mb-3",
        ),
        dbc.ButtonGroup(
            [dbc.Button("Connect",className="bg-primary"), dbc.Button("Reset",className="bg-secondary")],style=WIDTH100
        ),
        html.Hr(),
        html.P("Expansion mode : ", className="lead"),

        dbc.FormGroup(
        [
        dbc.Col(
            dbc.RadioItems(
                id="radio-expand2",
                options=[
                    {"label": "Childrens", "value": 'predecessors'},
                    {"label": "Parents", "value": 'successors'},
                    {"label": "All relations","value": 'All for the node'},
                ],value='All for the node'
            ),width=12,
        ),
        html.Hr(),
        dbc.Col([
            html.Hr(),
            drc.NamedDropdown(
                name='Layout type',
                id='dropdown-layout',
                options=drc.DropdownOptionsList(
                    'grid',
                    'breadthfirst',
                    'cose'
                ),
                value='grid',
                clearable=False,
            )
        ],width=12, className="dropdownColumn"),
        ],row=True,
        ),
        dbc.Col([
            html.Hr(),
            html.P("Layout type : ", className="lead"),
            dbc.DropdownMenu(label="Dropup", children=dropdown_layout_items, direction="up")
        ])
      #   drc.NamedRadioItems(
      #     name='Expand',
      #     id='radio-expand',
      #     options=drc.DropdownOptionsList(
      #         'predecessors',
      #         'successors',
      #         'All for the node'
      #     ),
      #     value='All for the node'
      # )
    ]
)
    ],style=SIDEBAR_STYLE,
),width=2, className="bg-light"),

        # dbc.Col(
        #     dbc.Row(
        #         [], className="bg-light", id="page-content", style=CONTENT_STYLE
        #     ),
        #
        # ),

        dbc.Col([
            dbc.Row(
                [

                ], className="bg-light", id="page-content",

            ),
            dbc.Row(
                [
                dbc.Col([dbc.Button("Generate SQL Query", color="primary", className="mr-2 btn btn-outline btn-lg", id="generate_button"),
                         dbc.Button("Execute query", className="mr-3 btn-outline-secondary btn-lg"),
                         ],width=8,className="mainButtonsContainer"),
                dbc.Col([dbc.Textarea(id='sql-querry',bs_size="md",contentEditable=False,className="mb-3 textareaQuery", placeholder="SELECT ... \nFROM ... \nWHERE ...")],width=12, className="queryContainer"),
                ], className="bg-light generateQueryContainer", id="page-content-main",

            )




        ]),

















        ##RIGHT

        dbc.Col(
             dbc.Row(
            [
                html.P("Choose your relations : ", className="lead"),
                dcc.Dropdown(
                    id='tables-relation',
                    clearable=True,
                    placeholder="Select relations tables",
                    multi=True,
                ),
                html.Hr(),
                dcc.Tabs(id='tabs', children=[
                    dcc.Tab(label='Control Panel', children=[
                        drc.NamedDropdown(
                            name='Layout',
                            id='dropdown-layout2',
                            options=drc.DropdownOptionsList(
                                'random',
                                'grid',
                                'circle',
                                'concentric',
                                'breadthfirst',
                                'cose'
                            ),
                            value='grid',
                            clearable=False,
                        )

                    ]),
                    dcc.Tab(label='JSON', children=[
                        html.Div(style=styles['tab'], children=[
                            html.P('Table-Relations Object JSON:'),
                            html.Pre(
                                id='tab-relation-json-output',
                                style=styles['json-output']
                            )
                        ])
                    ])
                ]),
                                # dcc.ConfirmDialogProvider(
                                #     children=html.Button(
                                #         children='Create the query',
                                #         id='id-button-query',
                                #         n_clicks=0,
                                #         className='button-querry',
                                #         style={'background-color': '#4CAF50',
                                #                 'color':'white',
                                #                 'width': '250px',
                                #                 'box-shadow': '0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)'
                                #                }
                                #     ),
                                #   id='create_the_query',
                                #   message='You have selected the tables relations. '
                                #           'Your SQL query will be created'
                                # ),
                                # dcc.Textarea(
                                #     id='sql-querry2',
                                #     placeholder='Correct the query',
                                #     # value='This is a TextArea component',
                                #     style={'width': '100%'}
                                # ),
                                # dcc.ConfirmDialogProvider(
                                #     children=html.Button(
                                #         'Execute the Query',
                                #         n_clicks=0,
                                #         className='button-execute-querry',
                                #         style={'background-color': '#4CAF50',
                                #                 'color':'white',
                                #                 'width': '250px',
                                #                 'box-shadow': '0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)',
                                #                 'position':'absolute'
                                #                }
                                #     ),
                                #   id='execute_the_query',
                                #   message='Your query will be executed'
                                # ),
            ], className="nicebg",id="right-bar",style=CONTENT_STYLE
        ),
        width=2, className="bg-light niceBackground"
        )



    ],align="left",
     no_gutters=False,
     style=SECTION1_STYLE
)



# Load extra layouts
cyto.load_extra_layouts()
# link fontawesome for icons font
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
external_stylesheets = [dbc.themes.FLATLY, FA]
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)
app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([dcc.Location(id="url"),navbar2,section1
                          # , section2
], className="mainContainer")


graph_full = cyto.Cytoscape(
      id='cytoscape-event-callbacks-1',
      stylesheet=default_stylesheet,
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
      style={'width': '100%', 'height': '70vh', 'max-height':'70vh'},
      elements=default_elements
  )


@app.callback(Output('tables-relation','options'),
              [Input('tab-relation-json-output', 'children')])
def add_relations_to_DropdownOptions(jsonified_cleaned_data):
    relations = json.loads(jsonified_cleaned_data)
    relations_flatten = [item for sublist in relations for item in sublist]
    relations_items = [{'label': nom_relation,
         'value':nom_relation} for nom_relation in relations_flatten]
    relations_drop_menu.extend(relations_items)
    return relations_drop_menu

@app.callback(Output('sql-querry', 'value'),
              [Input('generate_button', 'n_clicks')],
              [Input('tables-relation', 'value')])
def create_query(submit_n_clicks, value):
    if not submit_n_clicks:
        return ''
    # return """
    #     Submitted "{}" times,
    #     values is "{}"
    #     """.format(submit_n_clicks, Query.query_and_store(value, list_dict_successors_predecessors[5]))
    return Query.query_and_store(value, list_dict_successors_predecessors[5])




@app.callback(Output('tap-edge-json-output', 'children'),
              [Input('cytoscape-event-callbacks-1', 'tapEdge')])
def display_tap_edge(data):
    return json.dumps(data, indent=2)

@app.callback(Output('cytoscape-mouseoverNodeData-output', 'children'),
                    Input('cytoscape-event-callbacks-1', 'mouseoverNodeData'))
def displayMouseonNodeData(data):
    if data:
        return "You are hovering on the table: " + data['label']

@app.callback(Output('cytoscape-event-callbacks-1', 'layout'),
              [Input('dropdown-layout', 'value')])
def update_cytoscape_layout(layout):
    return {'name': layout}




@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return graph_full
    elif pathname == "/page-2":
        return graph_full
    elif pathname == "/page-3":
        return html.P("Graph view 3")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )



@app.callback(Output('cytoscape-event-callbacks-1', 'elements'),
              Output('cytoscape-event-callbacks-1','stylesheet'),
              Output('tab-relation-json-output', 'children'),
              [Input('cytoscape-event-callbacks-1', 'tapNodeData')],
              [State('cytoscape-event-callbacks-1', 'elements'),
               State('radio-expand2', 'value')])

def generate_elements(nodeData, elements, expansion_mode):
    if not nodeData:
        return default_elements, default_stylesheet, json.dumps([])
    a,b=[],[]
    for element in elements:
        if (nodeData['id'] == element.get('data').get('id')):
            if (element.get('selectable')==True):
                element['data']['expanded'] = True
                break
            else:
                return elements,default_stylesheet,json.dumps([])
    all_nodes=construct_allnodes.allnodes_of_a_node\
        (list_dict_successors_predecessors[2].get(nodeData['id']),
         list_dict_successors_predecessors[0].get(nodeData['id']))
    followers_nodes = list_dict_successors_predecessors[2].get(nodeData['id'])
    followers_arcs = list_dict_successors_predecessors[3].get(nodeData['id'])
    following_nodes = list_dict_successors_predecessors[0].get(nodeData['id'])
    following_arcs = list_dict_successors_predecessors[1].get(nodeData['id'])

    if expansion_mode == 'predecessors':

        if followers_nodes:
            for node in followers_nodes:
                node['classes'] = 'followerNode'
            elements.extend(followers_nodes)

        if followers_arcs:
            for follower_edge in followers_arcs:
                follower_edge['classes'] = 'followerEdge'
            elements.extend(followers_arcs)

    elif expansion_mode == 'successors':

        if following_nodes:
            for node in following_nodes:
                    node['classes'] = 'followingNode'
                    elements.append(node)

        if following_arcs:
            for following_edge in following_arcs:
                following_edge['classes'] = 'followingEdge'
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

        if followers_arcs:
            for follower_edge in followers_arcs:
                follower_edge['classes'] = 'followerEdge'
                for i in range(0, len(elements)):
                    if(elements[i].get('data').get("id") == follower_edge['data']['id']):
                        elements[i]=follower_edge
                        print(elements[i])
                        if(elements[i].get('selectable')==True):
                            a.append(construct_allnodes.set_list_relations([],elements[i].get('data').get("id")))
                        break

        if following_arcs:
            for following_edge in following_arcs:
                following_edge['classes'] = 'followingEdge'
                for i in range(0, len(elements)):
                    if(elements[i].get('data').get("id") == following_edge['data']['id']):
                        elements[i]=following_edge
                        print(elements[i])
                        if (elements[i].get('selectable') == True):
                            b.append(construct_allnodes.set_list_relations([],elements[i].get('data').get("id")))
                        break


        for element in elements:
            if (element.get('classes') != 'ffNodes'):
                element['classes'] ='notSelect'
                element['selectable']=False
            else:
                element['selectable']=True

    def new_stylesheet(stylesheet):
        stylesheet.append(
            {
            'selector': '.notSelect',
                'style': {
                    'background-color': '#95a5a6',
                     "background-opacity": 0.5,
                    "text-opacity" : "0.5",
                    "font-opacity" : "0.5",
                    "label-opacity": "0.5",
                }
            }
        )
        stylesheet.append(
            {
                'selector': '.followerEdge',
                 "style": {
                        "mid-target-arrow-color": "blue",
                        "mid-target-arrow-shape": "vee",
                        "line-color": "#0074D9"
                 }
            }
        )
        return stylesheet

    a.extend(b)
    stylesheet=new_stylesheet(default_stylesheet)
    return elements, stylesheet, json.dumps(a)



if __name__ == '__main__':
    # metadata = ConstDF.readbd()
    # elements_graph = NodesRelations.elements(metadata)
    app.run_server(debug=True)


