def occupy_memory():
    import sys
    var1="Python"
    var2=100
    var3=True
    print(sys.getsizeof(var1)) 
    print(sys.getsizeof(var2)) 
    print(sys.getsizeof(var3)) 

def anogram(str1, str2):
    from collections import Counter
    def anagrams(str1, str2):
        return Counter(str1) == Counter(str2)
    anagrams("str1", "str2") 
