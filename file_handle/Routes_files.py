from Routes.Routes import Routes, json_repr_routes
from networkx.readwrite.json_graph import node_link_graph
from file_handle.file_handle import write_data, read_data


def write_Route(route: Routes):
    write_data(json_repr_routes(route), base_path="data/Routes_files")


def read_Route(uniq_id):
    data = read_data(uniq_id, base_path="data/Routes_files")
    routes = Routes(
        data['id'], node_link_graph(data['graph'], edges="edges"), False
    )
    return routes
