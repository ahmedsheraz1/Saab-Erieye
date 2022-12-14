Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a = [-1, 1, 66.25, 360, 360, 1234.5]
del a[0]
[1, 66.25, 360, 360, 1234.5]
[1, 66.25, 360, 360, 1234.5]
del a[2:4]
a
[1, 66.25, 1234.5]
del a[:]
a
[]
