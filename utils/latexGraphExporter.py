from graph.graph import Graph

class LatexGraphExporter:
    def __init__(self):
        pass

    def to_latex(self, graph: Graph):
        latex_string = r"""\documentclass{article}
            \usepackage{graphicx} % Required for inserting images
            \usepackage{tikz}
            \usetikzlibrary{positioning, quotes, shapes.multipart}
            
            \begin{document}
            """
        latex_string += self.to_latex_raw(graph)

        latex_string += "\end{document}"
        
        return latex_string


    def to_latex_raw(self, graph: Graph):
        latex_string = r"""\begin{tikzpicture}[scale = 3, font = \Large, node distance = 15mm and 15mm,
                                            V/.style= {circle, draw, fill = gray!30},
                                            every edge quotes/.style= {auto, font =\footnotesize, sloped}
                                            ]""" + "\n"
                                            
        latex_string += r"\begin{scope}[nodes=V]" + "\n"
        for node_id, node in graph.nodes.items():
            node_id = str(node_id)
            if node.label:
                latex_string += f"\\node[circle split,draw]  ({node_id}) at ({node.x}, {node.y}) {{{node_id} \\nodepart{{lower}} {node.label}}};\n"
            else:
                latex_string += f"\\node ({node_id}) at ({node.x}, {node.y}) {{{node_id}}};\n"
        latex_string += r"\end{scope}" + "\n"

        latex_string += r"\begin{scope}[->]" + "\n"
        for edge in graph.edges:
            if edge.label:
                latex_string += f"\\draw ({edge.from_node}) edge[\"{edge.label}\"] ({edge.to_node});\n"
            else:
                latex_string += f"\\draw ({edge.from_node}) ({edge.to_node});\n"
        latex_string += r"\end{scope}" + "\n"

        latex_string += r"\end{tikzpicture}" + "\n"

        return latex_string