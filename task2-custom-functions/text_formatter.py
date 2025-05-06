def format_text(text:str,prefix:str,suffix:str, capitalize:bool=False, max_length:int=None)->str:
    """
    formats the text tha t you input  by applying prefix,suffix,capitalize,and max_length.
    Parameters:
    text(str):The main input string which is being to be formatted.
    prefix(str,optional): this the string to add at the beginning of the input text. Default is an empty string.
    suffix(str,optional): this the string to add to end of a text. Default is an empty.
    Captalize(bool,optional): if value is true , capitalize the text. Default is False
    max_length(int or None,optional): if provided truncates  the final results to this maximum length.

    Returns:
    The functions formatted returns str according to the given parameters.
    Raises:
    the formatted text raise type error input types are incorrect and value error if max_length is negative.

    """
    try:
        if not isinstance(text,str):
           raise TypeError("'text'must be a string")
        if not isinstance(prefix,str):
          raise TypeError("'prefix' must be a string")
        if not isinstance(suffix,str):
          raise TypeError("'suffix' must be a string")
        if not isinstance(capitalize,bool):
           raise TypeError("'capitalize' must be a boolian")
        if max_length is not None and  not isinstance(max_length,int):
         raise TypeError("'max_length' must be None or integer")
        if max_length < 0:
           raise ValueError("'max_length'can not be negative.")
    
    # capitalise if needed
        if capitalize:
          text= text.capitalize()
        # apply prefix anf=d suffix
        Formatted_text= f"{prefix}{text}{suffix}"
        if max_length is not None:
         Formatted_text= Formatted_text[:max_length]
         return Formatted_text
    except(TypeError,ValueError) as e:
       return f"'Error :{e}"
text2= format_text("emmanuel" , prefix="hey",suffix="!" , capitalize= True , max_length=30)
print(text2)

