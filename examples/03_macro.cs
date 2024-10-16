using System;

// Create a macro for changing each row:
// Old: GetData<T>(args);
// New: args.T;
class MacrosAreAwesome 
{
    public static void Main (string[] args)
    {
        var result = new Result();

        result.Identifier = GetData<Ident>(args);
        result.DataTypes = GetData<DataTypes>(args);
        result.Variables = GetData<Var>(args);
        result.Literals = GetData<Lit>(args);
        result.Operators = GetData<Ops>(args);
        result.Keywords = GetData<KeyWords>(args);
        result.Class = GetData<Clazz>(args);
        result.Object = GetData<Obj>(args);
        result.Inheritance = GetData<Inherit>(args);
        result.Encapsulation = GetData<Encaps>(args);
        result.Abstraction = GetData<Abstract>(args);
        result.Methods = GetData<Methods>(args);
        result.Overloading = GetData<Overload>(args);
        result.Overriding = GetData<Override>(args);
        result.OptionalParameter = GetData<OptPara>(args);
        result.NullOrEmpty = GetData<NullEmpty>(args);
        result.Arrays = GetData<Arr>(args);
        result.Strings = GetData<Str>(args);
    }
}