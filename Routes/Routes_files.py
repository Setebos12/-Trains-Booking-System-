from Routes.Routes import Routes
from networkx.readwrite.json_graph import node_link_graph
from file_handle import write_data, read_data


def write_Route(route: Routes):
    # data = route.json_repr()
    # s1 = json.dumps(data, default=serialize_datetime, indent=4)
    # uniq_id = str(route.id)
    # file_path = (
    #     "/home/krzysztof-rutkowski/pipr1/project1/data/Routes_files/"
    #     f"{uniq_id}.json"
    # )
    # with open(file_path, 'w') as file_handle:
    #     file_handle.write(s1)
    write_data(route, base_path="data/Routes_files")


def read_Route(uniq_id):
    # file_path = (
    #     "/home/krzysztof-rutkowski/pipr1/project1/data/Routes_files/"
    #     f"{uniq_id}.json"
    # )
    # with open(file_path, 'r') as file_handle:
    #     file_data = file_handle.read()

    data = read_data(uniq_id, base_path="data/Routes_files")
    routes = Routes(
        data['id'], node_link_graph(data['graph'], edges="edges"), False
    )
    return routes
