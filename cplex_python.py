# coding:utf-8
import cplex

c = cplex.Cplex()  # 创建cplex对象
c.objective.set_sense(c.objective.sense.minimize)  # 目标为最小化
names = ['x1', 'x2', 'x3']  # 变量名称
c.variables.add(obj=[1, 1, 1], names=names)  # 添加目标函数
rows = [[[0, 1], [1, 1]],  # 约束条件的list表示
        [[1, 2], [1, 2]],
        [[0, 2], [1, 3]]]
c.linear_constraints.add(lin_expr=rows,  # 添加约束条件
                         rhs=[20, 30, 25],
                         senses='GGG',
                         names=['c1', 'c2', 'c3'])
c.solve()  # 求解
result = c.solution.get_values()  # 得到解的值
print result
for i in range(3):
    print names[i],result[i]
c.write('easy.lp')
