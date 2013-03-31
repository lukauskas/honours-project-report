import scipy.cluster.hierarchy as hcluster
import numpy as np
import matplotlib.pyplot as plt

chained_linkage = np.array([[1, 2, 1], [9, 3, 2], [10, 4, 3], [11, 5, 4], [12, 6, 5], [13, 7, 6], [14, 8, 7]])
chained_linkage = hcluster.from_mlab_linkage(chained_linkage)
perfect_linkage = hcluster.from_mlab_linkage(np.array([[1,2,1], [3,4,1], [5,6,1], [7,8,1], [9,10,2], [11,12,2], [13,14,3]]))

hcluster.dendrogram(perfect_linkage, color_threshold=0)
plt.savefig('perfect_linkage.pdf')
plt.close('all')
hcluster.dendrogram(chained_linkage, color_threshold=0)
plt.savefig('worst_case_linkage.pdf')
plt.close('all')

