# IPython log file

import dgw
import dgw.dtw.visualisation
import matplotlib.pyplot as plt


regions = dgw.read_bed('interesting_tss_regions.bed')
data = dgw.read_bam('/Users/saulius/dev/coursework/proj/data/interesting/broad/K562/wgEncodeBroadHistoneK562H3k4me3StdAlnRep1.bam', regions, resolution=25, extend_to=200)

def visualise_dtw_mappings(index_a, index_b, *args, **kwargs):
    a = data.ix[index_a]
    b = data.ix[index_b]

    dtw_func = dgw.dtw.parametrised_dtw_wrapper(*args, **kwargs)
    return dgw.dtw.visualisation.visualise_dtw_mappings(a,b, sequence_x_label=index_a, sequence_y_label=index_b, dtw_function=dtw_func)

def visualise_dtw_cost_function(index_a, index_b, *args, **kwargs):
    a = data.ix[index_a]
    b = data.ix[index_b]

    dtw_func = dgw.dtw.parametrised_dtw_wrapper(*args, **kwargs)
    return dgw.dtw.visualisation.visualise_dtw(a,b,dtw_function=dtw_func)

def to_figure(index_a, index_b, suffix="",  extension='pdf', *args, **kwargs):
    f = visualise_dtw_mappings(index_a, index_b, *args, **kwargs)
    f.savefig("{0}-{1}-mappings-{2}.{3}".format(index_a, index_b, suffix, extension))
    plt.close(f)

    f = visualise_dtw_cost_function(index_a, index_b, *args, **kwargs)
    f.savefig("{0}-{1}-cost-{2}.{3}".format(index_a, index_b, suffix, extension))
    plt.close(f)

