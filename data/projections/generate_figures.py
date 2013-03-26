# IPython log file

import dgw
import dgw.dtw.visualisation
from dgw.dtw.transformations import dtw_projection
import matplotlib.pyplot as plt


regions = dgw.read_bed('interesting_tss_regions.bed')
data = dgw.read_bam(['/Users/saulius/dev/coursework/proj/data/interesting/broad/K562/wgEncodeBroadHistoneK562H3k4me3StdAlnRep1.bam'], regions, resolution=50, extend_to=200)

a_ix = data.items[0]
b_ix = data.items[1]

a = data.ix[a_ix]
b = data.ix[b_ix]

def visualise_dtw_projection(index_a, index_b, *args, **kwargs):
    dtw_func = dgw.dtw.parametrised_dtw_wrapper(*args, **kwargs)

    projection = dtw_projection(a,b, dtw_function=dtw_func)
    plt.plot(projection)

def save_and_close_figure(title, filename):
    plt.title(title)
    plt.savefig(filename)
    plt.close('all')


plt.plot(a);  save_and_close_figure(a_ix, 'sequence.pdf')
plt.plot(b);  save_and_close_figure(b_ix, 'basis.pdf')
visualise_dtw_projection(a,b, try_reverse=False);  save_and_close_figure('Projection', 'projection.pdf')
