course = 'Python for Beginners'
print(course.find('P')) # 0
print(course.find('o')) # 4
print(course.find('O')) # -1
print(course.find('Beginners')) # 11
print(course.replace('Beginners',
                     'Absolute Beginners'))
                    # Python for Absolute Beginners
print(course.replace('beginners',
                     'Absolute Beginners'))
                    # Python for Beginners
print('Beginners' in course) # True
print('beginners' in course) # False
