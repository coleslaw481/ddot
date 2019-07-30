from flask_restful import reqparse, fields, Resource

from ddot import Ontology

class Controller(Resource):

    def post(self):
        
        file_name = 'edge_list.txt'
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('algorithm')
            parser.add_argument('type')
            parser.add_argument('edge_list')
            args = parser.parse_args()
            print(args)
            algorithm = args['algorithm']
            graph_type = False
            if args['type'] == "directed":
                graph_type = True
            edge_list = args['edge_list']
            
            with open(file_name, 'w+') as f:
                f.write(edge_list)
            
            if algorithm == "louvain":
                Ontology.run_louvain(graph = file_name, directed = graph_type)
            elif algorithm == "infomap":
                Ontology.run_infomap(algdir = "../ddot/Infomap/Infomap", graph = file_name, directed = graph_type)
            
            content = ''
            with open('tree.txt', 'r') as f:
                for line in f:
                    temp = line.replace('\t', ',')
                    content += temp.replace('\n', ';')
            return content, 201
        except Exception as e:
            return {'error': str(e)}
        