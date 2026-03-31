
router_ids=["1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4"]
def if_contain_intruders(output):
    output=[line.split()[0] for line in output.split('\n')[2:-1]]
    if not set(router_ids).issuperset(set(output)):
        return True #contain a non-valid router_ID
    else:
        return False

def list_of_intruder(output):
    output=[line.split()[0] for line in output.split('\n')[2:-1]]
    return list(set(router_ids)-set(output))
class FilterModule(object):
    def filters(self):
        return {
            'if_contain_intruders': if_contain_intruders
        }