# %matplotlib inline
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt

people = fetch_lfw_people(min_faces_per_person=20, resize=0.7)
print ('dir(people):')
print (dir(people))









print (people.images.shape)
print (dir(people.images))
# image_shape = people.images[0].shape
# kw = {'xticks':(), 'yticks':()} # () = empty tuple
# kw = {'xticks':[], 'yticks':[]} # () = empty tuple
kw = {'xticks':(0, 10), 'yticks':[]} # () = empty tuple
fix, axis = plt.subplots(2, 5, figsize=(15, 8), subplot_kw=kw)
# fix, axis = plt.subplots(8, 8, figsize=(15, 8))
zipped = zip(people.target, people.images, axis.ravel())
# print(tpl.__repr__)
for target, image, ax in zipped:
    ax.imshow(image)
    ax.set_title(people.target_names[target])
plt.show()
