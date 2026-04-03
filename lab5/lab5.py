def factorial(x):
    if x<0:
        return "Invalid"
    if x==0 or x==1:
        return 1
    return x*factorial(x-1)


abs_term=lambda t: t if t>=0 else -t
def exp_x(x, n):
    total=0
    for i in range(n):
        term=abs_term((x**(2*i))/factorial(2*i))
        if i%2==0:
            total+=term
        else:
            total-=term
    return total


g_total=0
def geometric_recursive(n, r):
    """
This function calculates 1+r+r^2+...+r^n using recursion.
If n < 0, the function stops.If it is not n<0, it adds r^nto a global variable
and calls itself with n-1.
 If r is negative, python handles.
    """
    global g_total
    if n<0:
        return
    g_total+=r**n
    geometric_recursive(n-1, r)

x=float(input("Enter x: "))
n1=int(input("Enter n: "))

print("Factorial of", n1, "=", factorial(n1))
print("Summation result =", round(exp_x(x, n1), 4))
n2 = int(input("Enter n: "))
r = float(input("Enter r: "))

g_total=0
geometric_recursive(n2, r)
print("Geometric series result =", g_total)