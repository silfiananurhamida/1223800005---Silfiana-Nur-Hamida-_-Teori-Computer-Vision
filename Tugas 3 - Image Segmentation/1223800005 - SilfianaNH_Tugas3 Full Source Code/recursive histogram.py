import cv2
import numpy as np
image = cv2.imread('favorit.jpg')
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
l_channel, a_channel, b_channel = cv2.split(lab_image)
hist_l = cv2.calcHist([l_channel], [0], None, [256], [0, 256])
hist_a = cv2.calcHist([a_channel], [0], None, [256], [0, 256])
hist_b = cv2.calcHist([b_channel], [0], None, [256], [0, 256])
def histogram_distance(hist1, hist2):
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
histograms_and_masks = [(hist_l, l_channel), (hist_a, a_channel), (hist_b, b_channel)]
def recursive_clustering(hist_and_mask_list, cluster_list):
    if len(hist_and_mask_list) == 0:
        return
    max_distance = -1
    cluster_index = -1
    for i in range(len(hist_and_mask_list)):
        for j in range(i + 1, len(hist_and_mask_list)):
            distance = histogram_distance(hist_and_mask_list[i][0], hist_and_mask_list[j][0])
            if distance > max_distance:
                max_distance = distance
                cluster_index = (i, j)

    if cluster_index != -1:
        i, j = cluster_index
        new_histogram = hist_and_mask_list[i][0] + hist_and_mask_list[j][0]
        new_mask = np.maximum(hist_and_mask_list[i][1], hist_and_mask_list[j][1])
        del hist_and_mask_list[j]
        del hist_and_mask_list[i]
        hist_and_mask_list.append((new_histogram, new_mask))
        cluster_list.append(new_mask)
        recursive_clustering(hist_and_mask_list, cluster_list)
clusters = []
recursive_clustering(histograms_and_masks, clusters)

for i, cluster in enumerate(clusters):
    result_image = cv2.bitwise_and(image, image, mask=cluster)
    cv2.imwrite(f'cluster_{i}.jpg', result_image)
