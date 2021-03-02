from graphviz import Digraph

casa = 'pared'
perro = 'sala'

g = Digraph('unix', filename='Reporte.png',
            node_attr={'color': 'lightblue2', 'style': 'filled'})

g.edge(casa, perro)

g.view()