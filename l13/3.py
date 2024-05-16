import vk_api
import numpy as np

def get_network(user_ids, access_token, as_edgelist=False):
    vk_session = vk_api.VkApi(token=access_token)
    vk = vk_session.get_api()

    adjacency_matrix = np.zeros((len(user_ids), len(user_ids)), dtype=int)
    edge_list = []

    for idx, user_id in enumerate(user_ids):
        try:
            friends_response = vk.friends.get(user_id=user_id)
            friends_ids = friends_response['items']

            for friend_id in friends_ids:
                if friend_id in user_ids:
                    friend_idx = user_ids.index(friend_id)
                    adjacency_matrix[idx][friend_idx] = 1

                    if as_edgelist:
                        edge_list.append((idx, friend_idx))

        except vk_api.ApiError as e:
            print(f"Error for user_id {user_id}: {e}")

    if as_edgelist:
        return edge_list
    else:
        return adjacency_matrix


user_ids = [345006376, 115321885, 735566239]
access_token = "vk1.a.XRMasYCpbhtaPv3Hjs86tCVLnzsx1UsLqt7ttBk512XtuDv2ohuwRaltCOVgwV1TMhccx5Rqh0NG9inFtzkx9ONU99h1uSC0fRXq-UjUjOnzI--TXWdJTpIuMc8gEnBnfhx7ksIOwDfDPSdWnSaty8H0q9DLMaAiHIgmBQ7E4T81-8VLlQ-WWUV0aB9q_KA0YegtTudJmLH6MxH6RiFgvg"

edge_list = get_network(user_ids, access_token, as_edgelist=True)
print("Список ребер:")
print(edge_list)

adjacency_matrix = get_network(user_ids, access_token, as_edgelist=False)
print("\nМатрица смежности:")
print(adjacency_matrix)