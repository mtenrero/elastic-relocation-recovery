
import elasticREST
import logging
import json

def resolveAllocation(endpoint: str):
    """Fix Allocation problems"""
    logging.basicConfig(level=logging.INFO)

    allocation_status = elasticREST.allocationExplain(endpoint)
    allocated_indexes = 0

    while 'error' not in allocation_status:
        index = allocation_status['index']
        shard = allocation_status['shard']

        node_id_found = allocation_status['node_allocation_decisions'][0]['node_id']

        for val in allocation_status['node_allocation_decisions']:
            if ('store' in val) and ('allocation_id' in val['store']):
                node_id_found = val['node_id']
                break

        allocation_result = elasticREST.forceAllocation(endpoint, allocation_status, node_id_found)

        if 'acknowledged' in allocation_result:
            logging.info("Index: {}, shard: {} allocation FORCED SUCCESFULLY".format(index, shard))
        else:
            logging.warning("Index {}, shard: {} forced allocation failed!!".format(index, shard), allocation_result)

        allocation_status = elasticREST.allocationExplain(endpoint)
        allocated_indexes += 1


    logging.info('Forced allocation over {} indexes'.format(allocated_indexes))
    return allocated_indexes
        