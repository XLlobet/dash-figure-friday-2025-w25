import  pandas                  as pd
import  plotly.express          as px
import  dash_ag_grid            as dag
from    plotly.graph_objects    import Figure

def create_grid(
        df:             pd.DataFrame)->dag.AgGrid:
    '''
    Create an AgGrid component
    '''

    grid = dag.AgGrid(
                id              = {"type": "grid", "index": "main_grid"},
                rowData         = df.to_dict("records"),
                columnDefs      = [{"field": i, 'filter': True, 'sortable': True} for i in df.columns],
                dashGridOptions = {"pagination": True})

    return grid
