import math



# ------------------ Number-theoretic and representation functions ---------------------



x = 4.25
y = 4.82
ceiling_value = math.ceil(x) # `math.ceil()` function in Python is used to find the smallest integer greater than or equal to given number(x). It returns the ceiling value of a floating-point or decimal number.
#print("Ceiling value of",x, "is",ceiling_value) # x = 5



'''`n`: Total Number of balls available.  
`k`: Number of balls you want to choose.
The `math.comb()` function helps you figure out how many different ways you can pick `k` balls from the total of `n` balls, without considering the order you picked them in.'''
n = 8  #total number of balls
k = 3  #Number of balls you want to choose
numberof_combinations = math.comb(n,k) #Calculate the number of combinations using math.comb()
#print(f"You can choose {k} balls out of {n} in {numberof_combinations} different ways.")
 


'''`math.copysign()` function in Python returns a floating-point number whose magnitude(absolute value) is that of `x`, but whose sign is taken from `y`. This function helps to copy the sign from one number to another.'''
x = 5.7 #The number whose magnitude will be used.
y = -8.9 #The number whose sign will be used.
result = math.copysign(x,y)
# print(result)



x = -7.25 # `x`: The number for which you want to find the absolute value.
result = math.fabs(x)
# print(result)



n = 5 # `n`: The non-negative integer  for which you want to compute the factorial
result = math.factorial(n) # 5! = 1 * 2 * 3 * 4 * 5
print(result) 


# `math.floor(x)` is a function from the `math` module that returns the largest integer less than or equal to `x`. It rounds down the given number to the nearest integer
x = 3.7 
result = math.floor(x) # answer will be 3



#if `x` (the numerator) is positive, the result of `math.fmod(x,y)` will also be positive.
#if `x` is negative, the result of `math.fmod(x,y)` will also be negative.
x = -10
y = 3
result = math.fmod(x,y)
print(result) #output will be -1.0



# `math.fsum(iterable)` function return the accurate floating-point sum of all the values in the iterable(such as a list, tuple or any iterable object) while minimizing the rounding errors that can occur simple addition.
numbers =[0.1,0.2,0.3,0.4,0.5]
result = math.fsum(numbers) #return the precise sum of the number in the list 
print(result) # output will be 1.0



# `math.isclose()` function in python is used to determine whether two floating-point number are "close" to each other in value. It takes two mandatory arguments, a and b representing the two numbers to compare. It accepts two optional keyword argument, rel_tol and abs_tol, whic specify the relative and absolute tolerances, respectively.
print(math.isclose(1.0,1.0)) #check if two numbers are equal with default tolerances (output True)
print(math.isclose(1.0001,1.0, rel_tol = 0.01)) #check if two numbers are close with relative tolerance (output True)
print(math.isclose(0.99,1.0, abs_tol=0.01)) #check if two numbers are close with absulate tolerance (output True)



#Calculate the GCD of 12 and 16 (Greatest Common Divisor) gosago
gcd_value = math.gcd(12,16)
print(gcd_value)
#Calculate the GCD of multiple integers
gcd_value = math.gcd(12,16,20,24)
print(gcd_value)

# `math.isfinite()` function in python is used to check whether a number is finit or not. A finit number is a real number that is neither positive nor negative infinity, nor is it "not a number"(NaN).
print(math.isfinite(10)) # output true
print(math.isfinite(-1.5)) # output true
print(math.isfinite(float('nan'))) # output False



# `math.isinf()` function in Python is used to determine whether a number is positive or negative infinity. It takes a single argument (x) representing the number to be checked.

print(math.isinf(float('inf'))) # output : True
print(math.isinf(float('-inf'))) # output : True
print(math.isinf(10)) # output : False
print(math.isinf(-1.4)) # output : False


#Define a variable with a NaN value
nan_value = float('NaN')
#check if the value is NaN using math.isnan()
result = math.isnan(nan_value)
print(f"the value NaN?{result}") 



# Calculate the integer square root using math.isqrt()
squart_root = math.isqrt(25) # output 5



# Calculate the LCM(gossago) of 12 and 16
lcm_value = math.lcm(12,16)
print(lcm_value) #output 48



#Define a singnificand and an exponent
significand = 0.75 #significand is set to `0.75`
exponent = 3 #exponent is set to `3`
# `math.ldexp(significand,exponent)` calculate 0.75 * 2 to the power expnent(3)
result = math.ldexp(significand,exponent) # 0.75 * (2*2*2)
print(result) # output 6.0



number  = -8.49
#Split the number into its fraction and integer parts using math.modf()
fractional_part, integer_part = math.modf(number)
print(fractional_part) # output : -0.4900
print(integer_part) # output : -8.0



print (math.nextafter(1.0,2.0,steps=2)) # 1.0 = The starting floating point number , 2.0 = The target floating point number   (steps = 2) = An optional integer specifying the number of steps to move towards y. The default value is 1.



# Calculate the number of permutation of 5 items taken 3 at a time
permutation = math.perm(5,3) # ((5!) / ((5-3)!))
permutation2 = math.perm(4) # 4!   
print(permutation,permutation2) # output : 120  and output : 24



# Define a list of number
numbers = [2,3,5,7]
#Calculate the product of all number in the list using math.prod()
result = math.prod(numbers,start=10) # (2*3*5*7) = 210  and start is a optional 210*10 = 2100
print(result) # ouput : 2100



x = -10
y = 3
print(x%y) # output : 2
z=math.remainder(x,y)
print(z) # output : -1.0
# `%` operator gives a remainder of `2` for `-10%3`
# and the other hand `math.remainder()` return `-1.0`, which is a value with the same sign as `-10`(the `x` argument), and the absolute value of the result (`1.0`) is less than absolute value of `y`(`3`)



p = [1,2,3]
q = [4,5,6]
dot_product = math.sumprod(p,q) # (1*4) + (2*5) + (3*6)
print(dot_product) # output : 32



float_number = 3.75
truncated_value = math.trunc(float_number)  # remove the decimal part
print(truncated_value)  # output : 3



float_number = 1.0
ulp_value = math.ulp(float_number) # smallest possible change for given number
print(ulp_value)  # output : 2.2203306250312e-16



# -------------------------- Power and logarithmatic function ------------------------


number = 27
cube_root = math.cbrt(number) # calculate the cube root using math.cbrt()
print(cube_root)



exponent = 2
# Calculate the exponential value using math.exp()
exp_value = math.exp(exponent) # e^2 = (2.71 * 2.71)) = 7.38
print(exp_value) # output : 7.38



result = math.exp2(4) # This will return 2^4 which is 16
print(result)  # output : 16



result = math.expm1(2) # This will return e^2 - 1
print(result) # output: 6.38\


result = math.log(10) # Natural logarithm of 10 (base e)
print(result) # output : 2.30
result2 = math.log(100,10) # Logarithm of 100 to the base 10
print(result2) # output : 2




result = math.log1p(1) # This will be return natural Logarithm 1 + 1 (loge 2)
print(result) # output : 0.69



result = math.log2(8) # This will return the base - 2 logarithm of 8 (log2 8)
print(result) # outptut : 3



result = math.log10(100) # This will return the base - 10 logarithm of 100
print(result)  # output : 2.0



result = math.pow(2,3) #  2*2*2
print(result ) # output : 8



result = math.sqrt(25)  # root of 25
print(result)



# ---------------------------- Trigonometric funciton ---------------------------



x = 0.5 # `x` should be in the range [-1,1]
result = math.acos(0.5) # acos means cos^-1 and This will calculate the arc cosine of 0.5
print(result) # output : 1.04



x = 0.5 # `x` should be in the range [-1,1]
result = math.asin(0.5) # acos means cos^-1 and This will calculate the arc sine of 0.5
print(result) # output : 0.52



x = 0.5
result =math.atan(1) # This will calculate the arc tangent of 1
print(result) # output : 0.78



result = math.atan2(1,1) # This will calculate the arc tangant of (x->1/y->1)
print(result) # output : 0.78




result = math.cos(math.pi/5) # This will calculate the cosine of pi/3 radians
print(result) # output 0.80


p = (2,3)
q = (4,5)
distance = math.dist(p,q) #sqrt((x2 - x1)^2 + (y2 - y1)^2)
print(distance)  # output : 2.82



x = 3
y = 4
distance = math.hypot(x,y)  # distance = sqrt(x^2)+(y^2)
print(distance)



result = math.sin(math.pi/6) # This will calculate the sine of pi/6 radians
print(result) # output will be  0.5



result = math.tan(math.pi/4) # This will calculate the tangent of pi/4 radius
print(result) # output will be 1.0



# -------------------------  Angular conversion -------------------------------



radian_angle = math.pi/2  # an angle in radian (90 degrees)
degree_angle = math.degrees(radian_angle)  # Convert readians to degrees
print(radian_angle)  # output will be 90



degree_angle = 180 # An angle in degree
radian_angle = math.radians(degree_angle) # converts degrees to radians
print(radian_angle)  # output : 3.14159


# ------------------------------------ Hyperbolic Function ---------------------------



x= 2
result = math.acosh(x) # formula = In(x + (sqrt (x^2) - 1)) and x>=1
print(result)  # output 1.31



x = 2.5
result = math.asinh(x) # formula = In(x + (sqrt (x^2) + 1)) and x>=1
print(result) # output 1.64



x = 0.5
result = math.atanh(x)  #formula atanh(x) = (1/2) In((1+x)/(1-x)) and -1<x<1
print(result)  # output 0.54


x = 2
result = math.cosh(x) # formula cosh(x) = ((e^x + (e^-x))/2)
print(result) # output : 3.76


x = 1.5
result = math.sinh(x) # formula sing(x) = ((e^x - (e^-x))/2)
print(result) # output : 2.12



x  = 0.8
result = math.tanh(x) # formula tanh(x) = (sinh(x) / consh(x))
print(result) # output : 0.66



x = 1.5
result = math.erf(x) # formula erf(x) = 2/(sqrt3.1416)|(up=x and down=0)e^-t^2 dt
print(result) # output : 0.96



pi_value = math.pi
print(pi_value) # output 3.14


e_value = math.e
print(e_value) # output  2.71



radius = 5
circumstance = math.tau * radius # math.tau = 2pi
print(circumstance) #output = 31.41
positive_infinity = math.inf
print(positive_infinity)   # output will be inf
x = 1000
if x > positive_infinity:
    print("x is greater than positive infinity.")
else:
    print("x is not greater than positive infinity.")




not_a_number = math.nan
print(not_a_number) # output will be none

#comparing involving NaN
print(not_a_number = not_a_number) # False(NaN does not equal itself)
print(math.isnan(not_a_number)) # output : True(checking if a value is NaN using math.isnan())
