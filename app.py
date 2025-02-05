import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server
# App layout
app.layout = html.Div(
    children=[
        # Header section with a title
        html.H1("A Special Message Just For You", style={
            'text-align': 'center', 'color': 'red', 'font-size': '4vw', 'font-family': 'Cursive'
        }),
        
        # Love letter container (styled as paper)
        html.Div(id="love-letter", children=[
            html.P("I've been wanting to tell you something...", style={
                'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'
            })
        ], style={
            'width': '80%', 'max-width': '600px', 'margin': '30px auto', 'padding': '20px', 'border': '2px solid #000', 
            'background-color': 'white', 'box-shadow': '5px 5px 10px rgba(0, 0, 0, 0.1)', 'border-radius': '10px'
        }),
        
        # Read More button (smaller width)
        dbc.Button("Read More", id="read-more-button", color="danger", size="md", style={
            'font-size': '1.5em', 'display': 'block', 'margin': '30px auto', 'padding': '5px 15px', 'width': '200px'
        }),
        
        # Yes button (initially hidden, smaller width)
        dbc.Button("Yes", id="yes-button", color="success", size="md", style={
            'font-size': '1.5em', 'display': 'none', 'margin': '30px auto', 'padding': '5px 15px', 'width': '200px'
        }),
        
        # Image container (initially hidden)
        html.Div(id="image-container", children=[], style={'text-align': 'center', 'margin-top': '30px'}),
    ],
    style={'background-color': '#ffcccb', 'height': '100vh', 'overflow-y': 'auto', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center'}
)

# Callback to reveal the love letter parts on button click and handle image display
@app.callback(
    [Output("love-letter", "children"),
     Output("read-more-button", "style"),
     Output("yes-button", "style"),
     Output("image-container", "children")],
    [Input("read-more-button", "n_clicks"),
     Input("yes-button", "n_clicks")]
)
def reveal_love_letter_and_handle_image(read_more_clicks, yes_clicks):
    # The text parts of the love letter
    text_parts = [
        "I've been wanting to tell you something!",
        "You're so special to me.",
        "I enjoy spending time with you.",
        "You're so far away but...",
        "Will you be my Valentine? ❤️"
    ]
    
    # Determine the content of the love letter based on how many times "Read More" has been clicked
    if read_more_clicks is None:
        letter_content = [html.P(text_parts[0], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'})]
    elif read_more_clicks == 1:
        letter_content = [
            html.P(text_parts[0], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[1], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'})
        ]
    elif read_more_clicks == 2:
        letter_content = [
            html.P(text_parts[0], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[1], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[2], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'})
        ]
    elif read_more_clicks == 3:
        letter_content = [
            html.P(text_parts[0], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[1], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[2], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[3], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'})
        ]
    else:
        letter_content = [
            html.P(text_parts[0], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[1], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[2], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[3], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'}),
            html.P(text_parts[4], style={'text-align': 'left', 'font-size': '2em', 'font-family': 'Cursive'})
        ]
    
    # If all the text is revealed, show the "Yes" button and hide the "Read More" button
    if read_more_clicks and read_more_clicks >= 4:
        read_more_style = {'display': 'none'}
        yes_button_style = {'display': 'block'}
    else:
        read_more_style = {'display': 'block'}
        yes_button_style = {'display': 'none'}
    
    # If the "Yes" button is clicked, display the image
    if yes_clicks:
        image_content = html.Img(src="https://t4.ftcdn.net/jpg/00/48/65/85/360_F_48658571_57S9CsaWk2spdRGLdaCiVZFOw2A2OvTJ.jpg", id="love-image", style={
            'max-width': '100%', 'height': 'auto', 'margin': '0 auto', 'display': 'block'
        })
    else:
        image_content = html.Div()  # Empty div if no image is to be shown

    return letter_content, read_more_style, yes_button_style, image_content

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8053)