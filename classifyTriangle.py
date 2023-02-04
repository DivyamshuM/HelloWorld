
def classifyTriangle(a,b,c):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return "Input must be numerical."

    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    
    #if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        #return "Right"
    if (a <= 0 or b<=0 or c<=0) or ((a > b + c) or (b > a + c) or (c > a + b)):
        return "NotATriangle"
    elif a == b == c:
        return "Equilateral" 
    elif a == b or b == c or c == a:
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            return "Right"
        else:

            return "Isosceles"
    #elif (a!=b) and (b!=c) and (a!=c):
    else:
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            return "Right"
        else:
            return "Scalene"
    #else:
        #return "NotATriangle"

#print(classifyTriangle(1,1,1.5))

