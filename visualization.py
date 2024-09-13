import dash
from dash import dcc
from dash import html
app = dash.Dash()

app.layout = html.Div([
    html.H1('Hello!'),
    html.Div('this is built using dash'),
    html.P('I dont want annything to do with python ')
])
print(help(app.callback))
if __name__ == '__main__':
    app.run_server(port=4050)
