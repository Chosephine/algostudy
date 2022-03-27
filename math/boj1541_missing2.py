# 55-50+40
formula = '09-09'
# formula = input()

# 55-50+40-
# formula = formula + '-'
minus_idx = []
for i in range(len(formula)):
    if formula[i] == '-':
        open_idx.append(i)

# 2, 8
min_formula = 1e+12
if not open_idx:
    min_formula = eval(formula[:len(formula)])
else:
    for j in range(len(open_idx)-1):
        if eval(formula[:open_idx[j]]) - eval(formula[open_idx[j]+1:open_idx[j+1]]) <= min_formula:
            min_formula = eval(formula[:open_idx[j]]) - eval(formula[open_idx[j]+1:open_idx[j+1]])

print(eval(formula))
# print(min_formula)