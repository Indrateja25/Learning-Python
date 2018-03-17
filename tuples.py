def performance(grades):
    first , *middle , last = grades
    avg = sum(middle)/len(middle)
    print('highest : ',max(grades),'lowest : ',min(grades),'middle avg : ',avg)

class10 = performance([56,78,91,35,66])
class9 = performance([29,98,67,88])