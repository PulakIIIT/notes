
# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_12 = Integer(12); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_25 = Integer(25)
p = MixedIntegerLinearProgram(maximization=False)
v = p.new_variable(binary=True, nonnegative=True)
x1, x2, x3, x4 = v["x1"], v["x2"], v["x3"], v["x4"]
p.set_objective(-_sage_const_17  * x1 + -_sage_const_25  * x2 + -_sage_const_12  * x3 + -_sage_const_10  * x4)
p.add_constraint(_sage_const_3  * x1 + _sage_const_6  * x2 + _sage_const_5  * x3 + _sage_const_5  * x4 <= _sage_const_12 )
p.add_constraint(_sage_const_4  * x2 + _sage_const_9  * x2 - _sage_const_2  * x3 + x4 <= _sage_const_25 )
p.solve()
x1opt, x2opt, x3opt, x4opt = tuple(p.get_values([x1, x2, x3, x4]))

print(x1opt, x2opt, x3opt, x4opt)

bs = [_sage_const_0 , _sage_const_1 ]
def objective(x1, x2, x3, x4): return _sage_const_17  * x1 + _sage_const_25  * x2 + _sage_const_12  * x3 + _sage_const_10  * x4

assign = None
obj = _sage_const_0 
for x1 in bs:
    for x2 in bs:
        for x3 in bs:
            for x4 in bs:
                curobj = objective(x1, x2, x3, x4)
                s = str((x1, x2, x3, x4))
                if not (_sage_const_3  * x1 + _sage_const_6  * x2 + _sage_const_5  * x3 + _sage_const_5  * x4 <= _sage_const_12 ): 
                    s += "| first infeasible"
                    print(s)
                    continue
                if not (_sage_const_4  * x2 + _sage_const_9  * x2 - _sage_const_2  * x3 + x4 <= _sage_const_25 ): 
                    s += "| second infeasible"
                    print(s)
                    continue
                if curobj > obj: obj = curobj; assign = (x1, x2, x3, x4)
print (assign, obj)

