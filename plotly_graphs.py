from postgres_dataframe import return_query_Timestamps, query_Database
import plotly.express as px


def plotly_graphs(days):
    '''
    Return plotly graphs for temp, RH, wind Dir, Wind Speed, Air Pressure and Rainfall
    '''
    first_day, last_day = return_query_Timestamps(days)
    df = query_Database(first_day, last_day)
    # ------------FORMATING OPTIONS------------------------------------------
    colors = {'background': '#111111', 'text': '#7FDBFF'}
    title_format = {'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'}
    # --------------------TEMPERATURE--------------------------------------------------------
    fig1 = px.line(df, x='timestamp', y='air_temp', title='Temperature', labels={
                   'timestamp': 'Datetime', 'air_temp': 'Temperature: Celcius'})
    fig1.update_layout(plot_bgcolor=colors['background'],
                       paper_bgcolor=colors['background'],
                       font_color=colors['text'],
                       title=title_format)
    fig1.update_xaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    fig1.update_yaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    # -----------------------RELATIVE-HUMIDITY------------------------------------------------
    fig2 = px.line(df, x='timestamp', y='rel_humidity', title='Relative Humidity', labels={
                   'timestamp': 'Datetime', 'rel_humidity': '% Relative Humidity'})
    fig2.update_layout(plot_bgcolor=colors['background'],
                       paper_bgcolor=colors['background'],
                       font_color=colors['text'],
                       title=title_format)
    fig2.update_xaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    fig2.update_yaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    # -----------------------WIND-DIRECTION--------------------------------------------------
    fig3 = px.line(df, x='timestamp', y='wind_dir', title='Azimuth Wind Direction',
                   labels={'timestamp': 'Datetime', 'wind_dir': 'Wind Direction'})
    fig3.update_layout(plot_bgcolor=colors['background'],
                       paper_bgcolor=colors['background'],
                       font_color=colors['text'],
                       title=title_format)
    fig3.update_xaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    fig3.update_yaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    # -----------------------WIND-SPEED--------------------------------------------------
    fig4 = px.line(df, x='timestamp', y='wind_speed', title='Wind Speed', labels={
                   'timestamp': 'Datetime', 'wind_speed': 'Wind Speed (m/s)'})
    fig4.update_layout(plot_bgcolor=colors['background'],
                       paper_bgcolor=colors['background'],
                       font_color=colors['text'],
                       title=title_format)
    fig4.update_xaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    fig4.update_yaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    # -----------------------AIR-PRESSURE--------------------------------------------------
    fig5 = px.line(df, x='timestamp', y='air_pressure', title='Air Pressure', labels={
                   'timestamp': 'Datetime', 'air_pressure': 'Air Pressure (mmHg)'})
    fig5.update_layout(plot_bgcolor=colors['background'],
                       paper_bgcolor=colors['background'],
                       font_color=colors['text'],
                       title=title_format)
    fig5.update_xaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    fig5.update_yaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    # -----------------------RAINFALL--------------------------------------------------
    fig6 = px.line(df, x='timestamp', y='rain_acc', title='RainFall', labels={
        'timestamp': 'Datetime', 'rain_acc': 'Rainfall (mm)'})
    fig6.update_layout(plot_bgcolor=colors['background'],
                       paper_bgcolor=colors['background'],
                       font_color=colors['text'],
                       title=title_format)
    fig6.update_xaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')
    fig6.update_yaxes(showgrid=False, zeroline=False,
                      showline=True, linewidth=2, linecolor='white')

    return fig1, fig2, fig3, fig4, fig5, fig6


if __name__ == '__main__':
    plotly_graphs(7)
