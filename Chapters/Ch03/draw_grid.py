def do_twice(f):
    f()
    f()
    
def do_four(f):
    do_twice(f)
    do_twice(f)

def line_two_by_two():
    print('+ - - - -', end=' ')
    print('+ - - - -', end=' ')
    print('+', end=' ')
    print()
    
def line_with_space():
    print('|        ', end=' ')
    print('|        ', end=' ')
    print('|', end=' ')
    print()
    
def line_four_by_four():
    print('+ - - - -', end=' ')
    print('+ - - - -', end=' ')  
    print('+ - - - -', end=' ')
    print('+ - - - -', end=' ')
    print('+', end=' ')
    print()
    
def line_with_space_four():
    print('|        ', end=' ')
    print('|        ', end=' ')
    print('|        ', end=' ')
    print('|        ', end=' ')
    print('|', end=' ')
    print()
    
def grid_two_by_two():
    line_two_by_two()
    do_four(line_with_space)
    line_two_by_two()
    do_four(line_with_space)
    line_two_by_two()
    #print()
    
def grid_four_by_four():
    line_four_by_four()
    do_four(line_with_space_four)
    line_four_by_four()
    do_four(line_with_space_four)
    line_four_by_four()
    do_four(line_with_space_four)
    line_four_by_four()
    do_four(line_with_space_four)
    line_four_by_four()
    
    
grid_four_by_four()