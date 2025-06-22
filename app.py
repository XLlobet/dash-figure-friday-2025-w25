from    dash                        import Dash, Input, Output, dcc, html
from    plotly.graph_objects        import Figure
from    figures                     import plots
import  dash_bootstrap_components   as dbc
import  dash_customizable_app_style as dcas
import  plotly.express              as px
import  pandas                      as pd
from datetime import datetime


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

cat_dict:       dict            = {'estprojectcost': 'Project Cost', 'fee': 'Fee'}


colors: list = [
    "#440154", "#471164", "#482576", "#453781", "#3F4889",
    "#39558C", "#31688E", "#2A788E", "#23888E", "#1F988B",
    "#22A884", "#3FBC73", "#5CC863", "#7AD151", "#9DD93A",
    "#BFD53E", "#D4E36B", "#EAE51A", "#FDE725", "#FCE225",
    "#FAD221", "#F8C318", "#F5B016", "#F29E17", "#EF861A",
    "#EB7120", "#E95C26", "#E6482E", "#E23338", "#DE1F40",
    "#D60C4A", "#CC0952", "#C1065A", "#B8045F", "#AD0365",
    "#A2026A", "#97036E", "#8B046F", "#7E056F", "#71066F",
    "#63086C", "#540B68", "#450E62", "#37115A", "#2B1451",
    "#201746", "#161A3C", "#0E1E31", "#0A2026", "#081F1C"
]

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

# for col in list(df.columns):

#     print(col)
#     print(df[col].dtype)
#     print("\n\n")

print('OBJECT')
print("\n")
print('workclass')
print(set(list(df['workclass'])))
print("\n\n")
print('permitclassmapped')
print(set(list(df['permitclassmapped'])))
print("\n\n")
print('constcompletedofficial')
print(set(list(df['constcompletedofficial'])))
print("\n\n")
print('censuslanduse')
print(set(list(df['censuslanduse'])))
print("\n\n")
print('contractorcompanyname')
print(set(list(df['contractorcompanyname'])))
print("\n\n")
print('contractorcity')
print(set(list(df['contractorcity'])))
print("\n\n")
print('countylocation')
print(set(list(df['countylocation'])))
print("\n\n")
print('jurisdiction_inout_ral')
print(set(list(df['jurisdiction_inout_ral'])))
print("\n\n")
print('statuscurrent')
print(set(list(df['statuscurrent'])))
print("\n\n")
print('statuscurrentmapped')
print(set(list(df['statuscurrentmapped'])))
print("\n\n")
print('workclassmapped')
print(set(list(df['workclassmapped'])))
print("\n\n")

print('NUMBERS')
print("\n")
print('permitclass')
print('estprojectcost')
print('censuslandusecode')
print('fee')
print('housingunitstotal')
print('latitude_perm')
print('longitude_perm')
print('originalzip')
print('permitnum')

print('DESCRIPTIONS')
print("\n")
print('proposedworkdescription')
print('description')
print('proposeduse')

print('DATES')
print("\n")
print('applieddate')
print('issueddate')
print('expiresdate')
print('issueddate_mth')
print('issueddate_yr')
print('recordupdatedate')
print('CreationDate')
print('EditDate')



grid                            = plots.create_grid(df)

app = Dash ("Figure Friday 2025 week 25", external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div(
    id       = "main_container",
    style    = {"minHeight": "100vh"},
    children = [
        dcas.customize_app_selectors(),
        html.H1("Raleigh NC - Building Permits Issued Past 180 Days", className="p-4 mb-0"),
        # grid,
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
                            className = "ms-4 me-4 mt-4 text-dark   ",
                            id = 'variable',
                            options = ['estprojectcost', 'fee'],
                            value = 'estprojectcost',
                        ),
                        dcc.Loading(
                            children = [
                                dcc.Store(id={"type": "figure-store", "index": "map_fig"}),
                                dcc.Graph(
                                    id = {"type": "graph", "index": "map_fig"},
                        )], type='default'),
                        html.Div(
                            className= "col-6 m-0 p-0",
                            children = [
                                dcc.Loading(
                                    children = [
                                        dcc.Store(id={"type": "figure-store", "index": "line_week"}),
                                        dcc.Graph(
                                            id = {"type": "graph", "index": "line_week"},
                                        )], type='default'),
                            ]
                        ),
                        html.Div(
                            className= "col-6 m-0 p-0",
                            children = [
                                dcc.Loading(
                                    children = [
                                        dcc.Store(id={"type": "figure-store", "index": "line_month"}),
                                        dcc.Graph(
                                            id = {"type": "graph", "index": "line_month"},
                                        )], type='default'),
                            ]
                        )
                    ])
                    
            ]),
    ])

@app.callback(
    Output({"type": "figure-store", "index": "line_week"}, 'data'),
    Output({"type": "figure-store", "index": "line_month"}, 'data'),
    Output({"type": "figure-store", "index": "map_fig"}, 'data'),
    Input('variable', 'value')
)
def update_figure(variable):
    
    figure_day      = px.histogram( df, 
                                    x='Week Day',
                                    y=variable,
                                    title=f'{cat_dict[variable]} per Week Day',
                                    template='plotly_white',
                                    color='Week Day',
                                    category_orders=orders).update_layout(yaxis_title=f'{cat_dict[variable]}')
    figure_month    = px.histogram( df, 
                                    x='Month',
                                    y=variable,
                                    title=f'{cat_dict[variable]} per Month and Week Day',
                                    template='plotly_white',
                                    color='Week Day',
                                    category_orders=orders).update_layout(yaxis_title=f'{cat_dict[variable]}')
    
    fig_map = px.scatter_map(df, lat="latitude_perm", lon="longitude_perm", size=variable, color=variable,
                        map_style='carto-darkmatter',zoom=9.5, height=550, color_continuous_scale=px.colors.sequential.Plasma_r).update_layout(coloraxis_colorbar=dict(title=dict(text=f'{cat_dict[variable]}')))
    
    return figure_day.to_dict(), figure_month.to_dict(), fig_map.to_dict()


if __name__ == "__main__":
    app.run(debug=False)