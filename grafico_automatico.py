import matplotlib.pyplot as plt 
 
input_values = range(-1001, 1001)
squares = [x**2 for x in input_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

 
    # configura a curva dps configura os pontos 
#ax.plot(input_values, squares, linewidth=3, c=(0, 0.05, 0, 0.052))
#ax.scatter(input_values[::50], squares[::50], , c='red', s=10)
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, s=10) 


    # seta o titulo do grafico e titulo do eixos 
ax.set_title("naturais ao quadrado", fontsize=18, fontweight='bold', fontstyle='oblique')
ax.set_xlabel("valor de x", fontsize=14)
ax.set_ylabel("valor de x ao quadrado", fontsize=14)

    # seta a espessura da curva  
ax.tick_params(axis='both', labelsize=10)


    # define o maximo e minumo no eixo X 
        # e dps
    # o maximo e o minimo no eixo Y
ax.axis([-1100, 1100, -0, 1100000])

    # marca coordenadas (x, y) e neste caso com outra cor diferente (verde)
    # dos de mais pontos azuis 
ax.scatter(0, 0)

plt.show()