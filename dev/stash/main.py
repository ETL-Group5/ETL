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

# ------Création de l'environnement

cyto.load_extra_layouts()
external_stylesheets = [dbc.themes.SIMPLEX]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

metadata=ConstDF.readbd()
default_elements=NodesRelations.elements(metadata)
list_dict_successors_predecessors=Listsuccessorpredecesseurs.successors_predecesseurs(metadata['table_columns_relations'])
joined_list = [*list_dict_successors_predecessors[4], *list_dict_successors_predecessors[5]]
default_elements=joined_list
default_elements=construct_allnodes.set_all_nodes_arcs(default_elements)


app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

# Define the app
# app.layout = dbc.Container(
#     dbc.Alert("Hello Bootstrap!", color="success"),
#     className="p-5",
# )

items = [
    dbc.DropdownMenuItem("Item 1"),
    dbc.DropdownMenuItem("Item 2"),
    dbc.DropdownMenuItem("Item 3"),
]

menu_style = {
    "background-color":"primary",
    "color":"secondary"
}

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

navbar = dbc.Navbar(
    brand="Demo",
    brand_href="#",
    sticky="top",
    color="primary",
    dark="True",
    children=[
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
        dbc.NavItem(dbc.NavLink("Link", href="#")),
    ],
)

app.layout = html.Div([navbar
])

if __name__ == '__main__':
    # metadata = ConstDF.readbd()
    # elements_graph = NodesRelations.elements(metadata)
    app.run_server(debug=True)


