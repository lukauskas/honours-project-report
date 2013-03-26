
import matplotlib.pyplot as plt
import dgw
from dgw.dtw.transformations import sdtw_averaging, uniform_scaling_to_length, dtw_path_averaging
regions = dgw.read_bed('interesting_regions.bed')
data = dgw.read_bam('/Users/saulius/dev/coursework/proj/data/interesting/broad/K562/wgEncodeBroadHistoneK562H3k4me3StdAlnRep1.bam', regions, resolution=25, extend_to=200)

a_ix = data.items[0]
b_ix = data.items[1]

a = data.ix[a_ix]
b = data.ix[b_ix]

def plot(item, title, filename):
    plt.plot(item);
    plt.title(title);
    plt.savefig(filename);
    plt.close('all')

plot(a, a_ix, "{0}.pdf".format(a_ix.replace('.', '_')))
plot(b, b_ix, "{0}.pdf".format(b_ix.replace('.', '_')))

max_len = max(len(a), len(b))
WEIGHT_A = 10
WEIGHT_B = 50

print 'Weight of {0} is {1}'.format(a_ix, WEIGHT_A)
print 'Weight of {0} is {1}'.format(b_ix, WEIGHT_B)

dtw_function = dgw.dtw.distance.parametrised_dtw_wrapper(try_reverse=False, constraint='sakoe_chiba', k=12)
psa_avg = uniform_scaling_to_length(sdtw_averaging(a,b,WEIGHT_A, WEIGHT_B, dtw_function=dtw_function), max_len)
std_avg = uniform_scaling_to_length(dtw_path_averaging(a,b,WEIGHT_A, WEIGHT_B, dtw_function=dtw_function), max_len)
unweighted_avg = uniform_scaling_to_length(dtw_path_averaging(a,b,1, 1, dtw_function=dtw_function), max_len)

plot(psa_avg, '', 'psa.pdf')
plot(std_avg, '', 'std.pdf')
plot(unweighted_avg, '', 'unweighted.pdf')
