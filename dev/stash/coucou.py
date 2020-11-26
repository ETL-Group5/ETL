from dash import Dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

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

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Heading"),
                        html.P(
                            "Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui."
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            id="dash-docs-graph",
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]},
                        ),
                    ]
                ),
            ]
        )
    ],
    className="docs-content",
)
external_stylesheets = [dbc.themes.SIMPLEX]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

app.layout = html.Div([navbar, body])

if __name__ == "__main__":
    app.run_server(debug=True)