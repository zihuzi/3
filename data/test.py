# 开发时间：2021/7/13 7:51
def print_models(unprinted_designs,completed_designs):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print('Printing model:'+current_design)
        completed_designs.append(current_design)
def show_models(unprinted_designs,completed_designs):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        completed_designs.append(current_design)
    print('The following models have been printed:')
    for completed_design in completed_designs:
        print(completed_design)