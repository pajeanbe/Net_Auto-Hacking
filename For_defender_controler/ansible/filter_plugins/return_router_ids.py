
router_ids=["1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4"]
def return_router_ids(output):
    output=[line.split()[0] for line in output.split('\n')[2:-1]]
    if not set(router_ids).issuperset(set(output)):
        return ["OSPF list contain non valid router ID",output]
    else:
        return list(set(output))

        # get all the router ID
        #return list(set([line.split()[0] for line in output.split('\n')[2:-1]]))


class FilterModule(object):
    def filters(self):
        return {
            'return_router_ids': return_router_ids
        }