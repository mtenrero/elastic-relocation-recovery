import network

def allocationExplain(endpoint: str):
    """Get allocation status"""
    response = network.rGetJSON(endpoint + '/_cluster/allocation/explain?pretty')

    return response

def forceAllocation(endpoint: str, allocation: object, node: str):
    """Force shard allocation to the first node with its data"""
    index = allocation['index']
    shard = allocation['shard']
    
    body = {
        "commands" : [ {
            "allocate_stale_primary" :
                {
                "index" : index,
                "shard" : shard,
                "node" : node,
                "accept_data_loss" : "true"
                }
            }
        ]
    }

    response = network.rPostJSON(endpoint + '/_cluster/reroute?pretty', body)
    return response