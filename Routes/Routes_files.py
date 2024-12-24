import json
from Routes.Routes import Routes
from datetime import datetime
from networkx.readwrite.json_graph import node_link_graph

def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


def deserialize_datetime(obj):
    for key, value in obj.items():
        if isinstance(value, str):
            try:
                obj[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return obj



def write_Route(route: Routes):
    data = route.json_repr()
    s1 = json.dumps(data, default=serialize_datetime, indent=4)
    uniq_id = str(route.routes_id)
    file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Routes_files/" + f"{uniq_id}.json" # relative path add
    with open(file_path, 'w') as file_handle:
        file_handle.write(s1)


def read_Route(uniq_id):
    file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Routes_files/" + f"{uniq_id}.json" # relative path add
    with open(file_path, 'r') as file_handle:
        file_data = file_handle.read()

    data = json.loads(file_data, object_hook=deserialize_datetime)
    routes = Routes(data['id'], node_link_graph(data['graph'], edges="links"), False)
    return routes