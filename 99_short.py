result = [(x, y) for x in range(2,10) for y in range(2,10)]
print(' '.join (f"{x}{y}={x*y}" + ('\n' if y == 9 else '') for x, y in result))
