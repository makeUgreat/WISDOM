def KFC():
    st1 = input()
    
    lower_count = 0
    upper_count = 0
    
    for st in st1:
    
        if st.islower():
            lower_count += 1
        if st.isupper():
            upper_count += 1
        
    return lower_count, upper_count   
    

low, up = KFC()

print(f'대문자{up}개')
print(f'소문자{low}개')