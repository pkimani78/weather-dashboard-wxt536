import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly_graphs import plotly_graphs


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.GRID])
server = app.server

app.title = 'Nairobi Weather Dashboard'
app.layout = html.Div(children=[
    dbc.Row(id='topheader', children=[
        dbc.Col([
            html.Header(className='header', children=[
                html.Nav(className='navbar', children=[
                    html.Ul([
                        html.Li(html.A(className='navlinks',
                                href='#', children='Home')),
                        html.Li(html.A(className='navlinks',
                            href='https://www.linkedin.com/in/peter-kimani-85898342/', target='_blank', children='Contacts')),
                    ]),
                    dcc.Dropdown(id='dropdown', options=[{'label': 'today', 'value': 0}, {'label': 'last 7 days', 'value': 7}, {
                        'label': 'last 30 days', 'value': 30}, {'label': 'last  1 year', 'value': 365}], value=0),
                ]),
                html.H1(className='logo', children=html.A(
                    href='#', children='Statta logo')),
                html.H1(
                    'Nairobi Weather Dashboard', style={'text-align': 'center', 'position': 'relative', 'top': '-150px'})
            ]),
        ], width=12, style={'background-color': 'black', 'height': '400px'}),
    ], no_gutters=True,),
    html.Div(id='weathertrends', children=[],)
])


@app.callback(
    Output(component_id='weathertrends', component_property='children'),
    Input(component_id='dropdown', component_property='value')
)
def update_Graphs(days):
    fig1, fig2, fig3, fig4, fig5, fig6 = plotly_graphs(days)
    return dbc.Row([
        dbc.Col(dcc.Graph(figure=fig1), width=6),
        dbc.Col(dcc.Graph(figure=fig2), width=6),
    ], no_gutters=True,), dbc.Row([
        dbc.Col(dcc.Graph(figure=fig3), width=6),
        dbc.Col(dcc.Graph(figure=fig4), width=6),
    ], no_gutters=True,), dbc.Row([
        dbc.Col(dcc.Graph(figure=fig5), width=6),
        dbc.Col(dcc.Graph(figure=fig6), width=6),
    ], no_gutters=True,),


if __name__ == '__main__':
    app.run_server(debug=True)
