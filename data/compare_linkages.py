import numpy as np
import dgw
import random
import fastcluster
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hcluster

random.seed(42)
np.random.seed(42)

regions = dgw.data.parsers.read_bed('encode_regions_around_tss.bed')
random_regions = regions.ix[random.sample(regions.index, 1000)]

data = dgw.read_bam('/Users/saulius/dev/coursework/proj/data/interesting/broad/K562/wgEncodeBroadHistoneK562H3k4me3StdAlnRep1.bam', random_regions)
data = data.to_log_scale()

dm = dgw.dtw.parallel.parallel_pdist(data)

single = fastcluster.single(dm)
complete = fastcluster.complete(dm)
average = fastcluster.average(dm)

hcluster.dendrogram(single, no_labels=True, color_threshold=0)
plt.title('Single linkage')
# plt.savefig('single.pdf')
# plt.close('all')
#
# hcluster.dendrogram(complete, no_labels=True, color_threshold=0)
# plt.title('Complete linkage')
# plt.savefig('complete.pdf')
# plt.close('all')
#
# hcluster.dendrogram(average, no_labels=True, color_threshold=0)
# plt.title('Average linkage')
# plt.savefig('average.pdf')
# plt.close('all')


