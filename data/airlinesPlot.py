import plotly.plotly as py
py.sign_in('kradnangel', 'l4t5rjasng')
import plotly.graph_objs as go

trace1 = go.Scatter(
    x = range(1988,2007),
    y = [753983,783320,824062,874791,916593,898896,874526,884019,888306,921850,915095,914130,908029,835236,728758,660617,687638,658302,506086],
    name='DL',
)
trace2 = go.Scatter(
    x = range(1988,2008),
    y = [694757,723252,712060,725191,782371,786696,722277,688471,655539,663954,653919,692653,742265,716985,852439,752241,698548,673569,643597,633857],
    name='AA',
)
trace3 = go.Scatter(
    x = range(1988,2005) + range(2007,2008),
    y = [587144,574674,606713,630093,639349,649086,638750,724807,735266,743847,748459,774370,776559,704977,587887,543957,555812,490002],
    name='UA',
)
trace4 = go.Scatter(
    x = range(1988,2002),
    y = [494383,712342,1002485,907184,886305,833131,857906,778835,728534,718751,696030,714430,748624,688748],
    name='US',
)
trace5 = go.Scatter(
    x = range(1988,1989),
    y = [470957],
    name='PI',
)
trace6 = go.Scatter(
    x = range(1989,1993) + range(2002, 2005),
    y = [451752,461745,460230,474931,513331,499160,507286],
    name='NW',
)
trace7 = go.Scatter(
    x = range(1993,2008),
    y = [488332,565426,693101,757419,794849,815069,853683,911699,957145,956745,958566,990404,1036034,1099321,1168871],
    name='WN',
)
trace8 = go.Scatter(
    x = range(2005,2008),
    y = [532032,550088,540494],
    name='MQ',
)
trace9 = go.Scatter(
    x = range(2005,2008),
    y = [517454,548109,597882],
    name='OO',
)

data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9]

layout = go.Layout(
    title='Top 5 Airlines',
    xaxis=dict(
        title='Years'
    ),
    yaxis=dict(
        title='Number of flights'
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='proj1')