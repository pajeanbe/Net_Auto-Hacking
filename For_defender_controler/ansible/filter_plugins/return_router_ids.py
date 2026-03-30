def return_router_ids(output):
        # get all the router ID
        return [line.split()[0] for line in output.split('\n')[2:-1]]


class FilterModule(object):
    def filters(self):
        return {
            'return_router_ids': return_router_ids
        }