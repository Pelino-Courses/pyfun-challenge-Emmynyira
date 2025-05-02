def calculate(*args,**kwargs):
    """ 
    performs the callculations (add,subtract,multiply,divide) on given numbers.
    
    positional  Arguments:
    *args: tuple
    the number to be processed.
    Keywords arguments:
    **kwargs- operations to perform(add=true,subtract=true,muliply=true,divide=true).

    Returns:
    dict:operation result.
    
    Rasises:
    TypeError: if any inputs is not number.
    ValueError: if fewer than two numbers are provided.

    """
    if not args:
        raise ValueError("At least one number is required.")
    
    for arg in args:
        if not isinstance(arg,(int,float)):
            raise TypeError(f"{arg} is invalid input: {arg} is not number.")
        
    
    if len(args) <2:
        raise ValueError("At least two numbers are required for meaningful ")
    result={}
    num1=list(map(float,args))

    if kwargs.get("add",False):
        result["add"]=sum(num1) 

    if kwargs.get("subtract",False):
        sub_result= num1[0]
        for n in num1[1:]:
            sub_result -= n
        result["subtract"]= sub_result
    if kwargs.get("multiply",False):
        mul_result = 1
        for n in num1:
            mul_result *= n
        result["multiply"] = mul_result
    if kwargs.get("divide",False):
        div_result = num1[0]
        try:
            for n in num1[1:]:
                div_result/= n
            result["divide"]= div_result
        except ZeroDivisionError:
            raise ZeroDivisionError("can not divide by zero.")
        if not result:
            raise ValueError("No valid operationprovided.")
        return result
    
solution= calculate(10,5, add=True, subtract=True,multiply=True,divide=True)
print(solution)