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
            graph_type = args['type']
            edge_list = args['edge_list']
            
            with open(file_name, 'w+') as f:
                f.write('#' + graph_type + '\n')
                f.write(edge_list)
                
            Ontology.run_community_alg(graph = file_name, method = algorithm, overlap = True, configuration_model = 'RB')
            
            content = ''
            with open('tree.txt', 'r') as f:
                content = f.read()
            return content, 201
        except Exception as e:
            return {'error': str(e)}
        