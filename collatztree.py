import graphviz
from math import log

def pick_color(value : str) -> str:
    # mark the cycle 1-2-4
    if value in ("1","2","4"):
        return "#ff2211"

    # color other nodes based on the number of digits, including an arbitrary
    # exponential term on the number of digits to make the gradient "scale" faster
    colors_by_size = ["#ff8811","#f4c271", "#f4f1e9", "#b1d182", "#688f4e", "#2b463c"]
    return colors_by_size[min(len(str(int(int(value) ** 1.33))), len(colors_by_size)) - 1]



def generate_graph(upper_bound : int):
    # set tree attributes
    tree = graphviz.Digraph("collatz-tree-" + str(upper_bound), format = "svg", engine = "neato")
    tree.attr("node", shape="circle")
    tree.attr("node", style="filled")
    tree.attr("node", fillcolor = "#694b37")
    tree.attr("node", fontcolor = "#111111")
    tree.attr(bgcolor = "#111111 : #222222")
    tree.attr(gradientangle = "90")
    # root = graphviz.Digraph("test")
    # root.attr(rank = "max")
    # root.node("1", style = "filled", fillcolor = "#ff6633")
    # tree.subgraph(root)

    # array for keeping edges
    edges = []
    already_tried = []

    # generate edges
    for i in range(1,upper_bound):
        while(True):
            last_i = i

            color = 0 if i % 2 == 0 else 1
            i = i//2 if i % 2 == 0 else 3 * i + 1

            if (last_i,i) in already_tried:
                break

            edges += [(last_i, i, color)]
            already_tried += [(last_i, i)]   
            
    # generate graph from edges
    for edge in [[str(n) for n in e] for e in edges]:
        colorstr = "#66dd88" if edge[2] == "1" else "#dd6644"
        tree.node(edge[0], shape = "circle", style = "filled", fillcolor = pick_color(edge[0]))
        tree.edge(edge[0], edge[1], color = colorstr)
    print("Done! Starting Rendering...")
    tree.render(directory = "output")
    print("Rendering Complete!")

if __name__ == "__main__":
    generate_graph(500)

