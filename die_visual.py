from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()
die_2 = Die()
results = []

# gera o resultado
for roll_num in range(1000):
	result = die.roll() +die_2.roll()
	results.append(result)

# analisa o reusltado 
frequencies = []
max_result = die.num_sides +die_2.num_sides

for value in range(1, max_result +1):
	frequency = results.count(value)
	frequencies.append(frequency)

# visiualizando os resultados
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequencia'}

my_layout = Layout(title='Resultado de 1000 giros em dois d6', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')