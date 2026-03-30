
router_ids=["1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4"]
def return_router_ids(output):
    output=[line.split()[0] for line in output.split('\n')]
    if not set(router_ids).issuperset(set(output)):
        return ["OSPF list contain non valid router ID",output]
    else:
        return output


class FilterModule(object):
    def filters(self):
        return {
            'return_router_ids': return_router_ids
        }