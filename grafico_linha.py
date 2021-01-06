import matplotlib.pyplot as plt 
 
input_values = [1, 2, 3, 4 , 5] 
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
    # seta o titulo do grafico e titulo do eixos 
ax.set_title("naturais ao quadrado", fontsize=18, fontweight='bold', fontstyle='oblique')
ax.set_xlabel("valor de x", fontsize=14)
ax.set_ylabel("valor de x ao quadrado", fontsize=14)

    # seta a espessura da curva  
ax.tick_params(axis='both', labelsize=10)

    # marca coordenadas (x, y)
ax.scatter(2, 4)

plt.show()