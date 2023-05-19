def switch(val,*conditions):
    conditions = list(conditions)

    for i in range(0,len(conditions)):
        if (val == conditions[i]):
            return i