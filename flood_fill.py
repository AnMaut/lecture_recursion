import matplotlib.pyplot as plt


def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    # img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()



import matplotlib.pyplot as plt
from fontTools.misc.cython import returns


# def flood_file(array, x_param, y_param):



def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    # img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()



img = plt.imread("files/img0.png")[:, :, 0]

print(img.shape)

x_param = 0
y_param = 0

position = [x_param, y_param]

if position[0] < 0 or position[0] > len(img[0]) - 1:
    img[position] = 0

if position[1] < 0 or position[1] > len(img[1]) - 1:
    img[position] = 0


