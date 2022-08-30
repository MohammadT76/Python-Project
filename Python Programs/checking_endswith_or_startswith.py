
# for more information see these links ; 
# https://careerkarma.com/blog/python-startswith-and-endswith/#:~:text=The%20startswith()%20string%20method,otherwise%2C%20the%20function%20returns%20False.
# or https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters

test = 'ali'
test2 = 'Ali'
print(test2.startswith(('a','A')))

potential_extensions = ('.mp3', '.mp4')
file_name = 'music.mp3'
print(file_name.endswith(potential_extensions))