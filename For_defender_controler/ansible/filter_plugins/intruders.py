
def if_contain_intruders(output,router_ids):
    output=[line.split()[0] for line in output.split('\n')[2:-1]]
    if not set(router_ids).issuperset(set(output)):
        return True #contain a non-valid router_ID
    else:
        return False

def get_intruders_list(output,router_ids):
    output=[line.split()[0] for line in output.split('\n')[2:-1]]
    return list(set(router_ids)-set(output))
class FilterModule(object):
    def filters(self):
        return {
            'if_contain_intruders': if_contain_intruders
        }