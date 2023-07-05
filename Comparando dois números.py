pri = float(input("\33[34mColoque o primeiro número: \33[m"))
seg = float(input("\33[34mColoque o segundo número: \33[m"))
if pri > seg:
    print("\33[1;32mO primeiro valor {} é maior que o segundo {}\33[m".format(pri , seg))
elif seg > pri:
    print("\33[1;32mO segundo valor {} é maior que o primeiro {}\33[m".format(seg , pri))
else:
    print("\33[1;32mO primeiro valor {} e o segundo valor {} são iguais.\33[m".format(seg , pri))