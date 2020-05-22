x = "arden"
l = list(x)
print(l)
print(" ".join(x))
a = ("xD".join(x))
print(a.split("xD"))
r = x.replace("de", "e")
print(r)

format = "{}, jermen, arden, garbis, {}".format("santik", "garen")
print(format)

formatRound = "{:,.2f}".format(29999564.24546)
print(formatRound)

print(dir(x))
print(help(x.replace))
print(help(str))