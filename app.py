from    dash                        import Dash, Input, Output, dcc, html
from    figures                     import plots
import  dash_bootstrap_components   as dbc
import  dash_customizable_app_style as dcas
import  plotly.express              as px
import  pandas                      as pd
from    datetime                    import datetime


df:     pd.DataFrame    = pd.read_csv("https://raw.githubusercontent.com/plotly/Figure-Friday/refs/heads/main/2025/week-25/Building_Permits_Issued_Past_180_Days.csv")
df = df.dropna(subset=['fee'])

dates:          list            = [''.join(list(date)[:10]) for date in df['CreationDate']]
months:         list            = [datetime.strptime(date, "%Y/%m/%d").strftime("%B") for date in dates]
days_of_week:   list            = [datetime.strptime(date, "%Y/%m/%d").strftime("%A") for date in dates]

df['Month']                     = months
df['Week Day']                  = days_of_week

orders:         dict            = {'Week Day':  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                                   "Month":     ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"],
                                   }


# Permits df
rows       = []

for value in orders['Month']:
    current_df          = df[df['Month'] == value]
    residential_df      = current_df[current_df['permitclassmapped'] == 'Residential']
    nonresidential_df   = current_df[current_df['permitclassmapped'] == 'Non-Residential']
    inside_city_df      = current_df[current_df['jurisdiction_inout_ral'] == 'Inside City Limits']
    outside_city_df     = current_df[current_df['jurisdiction_inout_ral'] == 'Outside City Limits']
    new_df              = current_df[current_df['workclassmapped'] == 'New']
    existing_df         = current_df[current_df['workclassmapped'] == 'Existing']

    rows.append({'Month':           value, 
                 'Permits Amount':  len(current_df), 
                 'Residential':     len(residential_df),
                 'Non-Residential': len(nonresidential_df),
                 'Inside City':     len(inside_city_df),
                 'Outside City':    len(outside_city_df),
                 'New':             len(new_df),
                 'Existing':        len(existing_df),
                 })

permits_df:     pd.DataFrame    = pd.DataFrame(rows)

cat_dict:       dict            = {'estprojectcost':    'Project Cost', 
                                   'fee':               'Fee', 
                                   'permitclassmapped': 'Permit Class',
                                   'Week Day':          'Week Day'}

cool_colors = [
    "#003f5c",  # deep navy blue
    "#006d5b",  # deep forest green
    "#5e548e",  # dark muted purple
    "#0077b6",  # vivid ocean blue
    "#00a86b",  # emerald green
    "#9d4edd",  # bright violet

    "#66cdaa",  # medium aquamarine
    "#b185db",  # pastel purple
    "#014f86",  # rich ocean blue
    "#5cb85c",  # leafy green
    "#a078b0",  # muted lilac
    "#90e0ef",  # icy blue
    "#8fd694",  # light moss green
]

grid                            = plots.create_grid(df)

app = Dash ("Figure Friday 2025 week 25", external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div(
    id       = "main_container",
    style    = {"minHeight": "100vh"},
    children = [
        dcas.customize_app_selectors(),
        html.H1("Raleigh NC - Building Permits Issued Past 180 Days", className="p-4 mb-0"),
        grid,
        html.Div(
            id          = "main_div",
            className   = "row m-0 p-0 pt-4 text-center",
            children    = [

                html.Div(
                    className   = "col-2 m-0 p-0 text-center",
                    children    = [
                        html.P("Residential Permits",
                               className="m-0 p-0 fw-bold fst-italic fs-5",
                               style= {'color': '#4cb5c6'}),

                        html.P(f"{len(df[df['permitclassmapped'] == 'Residential'])}",
                               className="m-0 p-0 fw-bold fs-1 fst-italic",
                               style= {'color': ' 	#b0e6d5'}),
                    ]),

                html.Div(
                    className   = "col-2 m-0 p-0 text-center",
                    children    = [
                        html.P("Non-Residential Permits",
                               className="m-0 p-0 fw-bold fst-italic fs-5",
                               style= {'color': '#4cb5c6'}),

                        html.P(f"{len(df[df['permitclassmapped'] == 'Non-Residential'])}",
                               className="m-0 p-0 fw-bold fs-1 fst-italic",
                               style= {'color': ' 	#b0e6d5'}),
                    ]),

                html.Div(
                    className   = "col-2 m-0 p-0 text-center",
                    children    = [
                        html.P("Status - Complete",
                               className="m-0 p-0 fw-bold fst-italic fs-5",
                               style= {'color': '#4cb5c6'}),

                        html.P(f"{len(df[df['statuscurrent'] == 'Complete'])}",
                               className="m-0 p-0 fw-bold fs-1 fst-italic",
                               style= {'color': ' 	#b0e6d5'}),
                    ]),

                html.Div(
                    className   = "col-2 m-0 p-0 text-center",
                    children    = [
                        html.P("Status - Issued",
                               className="m-0 p-0 fw-bold fst-italic fs-5",
                               style= {'color': '#4cb5c6'}),

                        html.P(f"{len(df[df['statuscurrent'] == 'Issued'])}",
                               className="m-0 p-0 fw-bold fs-1 fst-italic",
                               style= {'color': ' 	#b0e6d5'}),
                    ]),

                html.Div(
                    className   = "col-2 m-0 p-0 text-center",
                    children    = [
                        html.P("Average Cost",
                               className="m-0 p-0 fw-bold fst-italic fs-5",
                               style= {'color': '#4cb5c6'}),

                        html.P(round(df['estprojectcost'].mean(), 1),
                               className="m-0 p-0 fw-bold fs-1 fst-italic",
                               style= {'color': ' 	#b0e6d5'}),
                    ]),

                html.Div(
                    className   = "col-2 m-0 p-0 text-center",
                    children    = [
                        html.P("Average Fee",
                               className="m-0 p-0 fw-bold fst-italic fs-5",
                               style= {'color': '#4cb5c6'}),

                        html.P(round(df['fee'].mean(), 1),
                               className="m-0 p-0 fw-bold fs-1 fst-italic",
                               style= {'color': ' 	#b0e6d5'}),
                    ]),

                html.Div(
                    className   = "row m-0 p-0 text-center",
                    children    = [
                        
                        dcc.Dropdown(
                            className = "ms-4 me-4 mt-4 text-dark",
                            id = 'variable',
                            options = ['estprojectcost', 'fee'],
                            value = 'estprojectcost',
                        ),

                        html.Div(
                            className= "col-12 m-0 p-0",
                            children = [
                                dcc.Loading(
                                    children = [
                                        dcc.Store(id={"type": "figure-store", "index": "map_fig"}),
                                        dcc.Graph(
                                            id = {"type": "graph", "index": "map_fig"},
                                )], type='default'),
                            ]
                        ),

                        html.Div(
                            className= "col-12 m-0 p-0",
                            children = [
                                dcc.Loading(
                                    children = [
                                        dcc.Store(id={"type": "figure-store", "index": "summary"}),
                                        dcc.Graph(
                                            id = {"type": "graph", "index": "summary"},
                                            figure= px.histogram(permits_df, 
                                                                 x='Month', 
                                                                 y=['Permits Amount', 'Residential', 'Non-Residential', 'Inside City', 'Outside City', 'New', 'Existing'],
                                                                 barmode='group'),
                                )], type='default'),
                            ]
                        ),

                        

                        dcc.Dropdown(
                            className = "ms-4 me-4 mt-4 text-dark",
                            id = 'color',
                            options = ['Week Day', 'permitclassmapped'],
                            value = 'Week Day',
                        ),

                        html.Div(
                            className= "col-6 m-0 p-0",
                            children = [
                                dcc.Loading(
                                    children = [
                                        dcc.Store(id={"type": "figure-store", "index": "bar_week"}),
                                        dcc.Graph(
                                            id = {"type": "graph", "index": "bar_week"},
                                        )], type='default'),
                            ]
                        ),
                        
                        html.Div(
                            className= "col-6 m-0 p-0",
                            children = [
                                dcc.Loading(
                                    children = [
                                        dcc.Store(id={"type": "figure-store", "index": "bar_month"}),
                                        dcc.Graph(
                                            id = {"type": "graph", "index": "bar_month"},
                                        )], type='default'),
                            ]
                        ),

                    ])
                    
            ]),
    ])

@app.callback(
    Output({"type": "figure-store", "index": "summary"}, 'data'),
    Input('variable', 'value')
)
def update_figure(variable):
        
    fig     = px.bar( permits_df, 
                            x='Month', 
                            y=['Permits Amount', 'Residential', 'Non-Residential', 'Inside City', 'Outside City', 'New', 'Existing'],
                            barmode='group')
    
    return fig.to_dict()

@app.callback(
    Output({"type": "figure-store", "index": "map_fig"}, 'data'),
    Input('variable', 'value')
)
def update_figure(variable):
        
    fig_map         = px.scatter_map(df, 
                                     lat="latitude_perm", 
                                     lon="longitude_perm", 
                                     size=variable, 
                                     color=variable,
                                     map_style='carto-darkmatter',
                                     zoom=9.5, 
                                     height=550, 
                                     color_continuous_scale=px.colors.sequential.Plasma_r).update_layout(coloraxis_colorbar=dict(title=dict(text=f'{cat_dict[variable]}')), font=dict(size=10))
    
    return fig_map.to_dict()


@app.callback(
    Output({"type": "figure-store", "index": "bar_week"}, 'data'),
    Output({"type": "figure-store", "index": "bar_month"}, 'data'),
    Input('variable', 'value'),
    Input('color', 'value')
)
def update_bars(variable, color):

    if color == 'Week Day':

        color_seq = None

    else:

        color_seq = [cool_colors[0], cool_colors[12]]
    
    figure_day      = px.histogram( df, 
                                    x='Week Day',
                                    y=variable,
                                    title=f'{cat_dict[variable]} per {cat_dict[color]}',
                                    template='plotly_white',
                                    color=color,
                                    category_orders=orders,
                                    color_discrete_sequence=color_seq).update_layout(yaxis_title=f'{cat_dict[variable]}', font=dict(size=10))
    figure_month    = px.histogram( df, 
                                    x='Month',
                                    y=variable,
                                    title=f'{cat_dict[variable]} per Month and {cat_dict[color]}',
                                    template='plotly_white',
                                    color=color,
                                    category_orders=orders,
                                    color_discrete_sequence=color_seq).update_layout(yaxis_title=f'{cat_dict[variable]}', font=dict(size=10))

    return figure_day.to_dict(), figure_month.to_dict()


if __name__ == "__main__":
    app.run(debug=True)