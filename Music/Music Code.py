    # Function to convert the image to HSV color space
hsv = cv2.cvtColor(ori_img, cv2.COLOR_BGR2HSV)

    # Bilding the image
fig, axs = plt.subplots(1, 3, figsize = (15,15))
names = ['BGR','RGB','HSV']
imgs  = [ori_img, img, hsv]
i = 0
for elem in imgs:
    axs[i].title.set_text(names[i])
    axs[i].imshow(elem)
    axs[i].grid(False)
    i += 1
plt.show()

    # Initialization 
hues = []
for i in range(height):
    for j in range(width):
        hue = hsv[i][j][0] # Meaning coordination (i,j)
        hues.append(hue)