import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_reusable_components as drc
import plotly.express as px
from dash.dependencies import Input, Output, State
import json

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
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "height" : "100%"
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

SECTION1_STYLE = {
    "height": "95vh"
}


WIDTH100 = {
    "width" : "100%"
}



# navbar = dbc.NavbarSimple(
#
#     [
#
# dbc.Row(
#     [
#         dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px"),width="auto"),
#         dbc.Col(dbc.NavbarBrand(APP_NAME, className="ml-2")),
#         dbc.Col(dbc.NavLink("Page 1", href="#")),
#     ],
#     align="center",
#     no_gutters=True,
# ),
#
#     ],
#     color="primary",
#     dark=True,
# )

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
    dark=True,
    ),width=12

    )

    ],align="center",
     no_gutters=True,
)

# sidebar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.Hr(),
#         html.P(
#             "A simple sidebar layout with navigation links", className="lead"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Page 1", href="/page-1", id="page-1-link"),
#                 dbc.NavLink("Page 2", href="/page-2", id="page-2-link"),
#                 dbc.NavLink("Page 3", href="/page-3", id="page-3-link"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )


section1 = dbc.Row(
    [
        dbc.Col(
            html.Div(
    [
        html.H2("StagBI25", className="display-5"),
        html.Hr(),
        html.P("Select a graph : ", className="lead"),
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
                # drc.NamedRadioItems(
                #                     name="",
                #                     className="lead, custom-control-label::before, custom-control-input",
                #                     id='radio-expand',
                #                     options=drc.DropdownOptionsList(
                #                               'predecessors',
                #                               'successors'
                #                           ),
                #                           value='predecessors'
                #                       )

dbc.FormGroup(
    [
        dbc.Col(
            dbc.RadioItems(
                id="example-radios-row",
                options=[
                    {"label": "Childs", "value": 1},
                    {"label": "Parents", "value": 2},
                    {"label": "All relations","value": 3},
                ],value=3
            ),width=12,
        ),
    ],row=True,
)


    ]
)

    ],style=SIDEBAR_STYLE,
)
        ,width=2, className="bg-light"),
        dbc.Col(
            html.Div(id="page-content", style=CONTENT_STYLE),
                width=10, className="bg-light")
    ],align="left",
     no_gutters=True,
     style=SECTION1_STYLE
)





# content = html.Div(id="page-content", style=CONTENT_STYLE)

# section1 = dbc.Row(
#     [
#         dbc.Col(
#             ""
#         ,width=4, className="bg-primary"),
#         dbc.Col(
#             ""
#         ,width=8,  className="bg-dark")
#
#     ])
#





# link fontawesome to get the chevron icons
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
external_stylesheets = [dbc.themes.FLATLY, FA]
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)
app.layout = html.Div([dcc.Location(id="url"),navbar2,section1
])

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
        return html.P("Graph view 1")
    elif pathname == "/page-2":
        return html.P("Graph view 2")
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


if __name__ == '__main__':
    # metadata = ConstDF.readbd()
    # elements_graph = NodesRelations.elements(metadata)
    app.run_server(debug=True)


