import matplotlib.pyplot as plt
import dgw


dgw.genes.read_encode_known_genes('../knownGenes_pilot')
known_genes = dgw.genes.read_encode_known_genes('../knownGenes_pilot')

tss_regions = known_genes.regions_around_transcription_start_sites(2000)
data = dgw.read_bam('/Users/saulius/dev/coursework/proj/data/interesting/broad/K562/wgEncodeBroadHistoneK562H3k4me3StdAlnRep1.bam', tss_regions,
                    extend_to=200, resolution=50)
known_genes = known_genes.ix[data.items]

plt.plot(data.ix[known_genes[known_genes.strand=='-'].index].mean().values)
plt.xlabel('Offset from TSS (base pairs)')
plt.ylabel('Average number of reads')
xticklabels = [ '{0}'.format(int((x-40)*50)) for x in plt.xticks()[0] ]
plt.gca().set_xticklabels(xticklabels)
plt.savefig('reverse_strand.pdf')

plt.clf()
plt.plot(data.ix[known_genes[known_genes.strand=='+'].index].mean().values)
plt.xlabel('Offset from TSS (base pairs)')
plt.ylabel('Average number of reads')
xticklabels = [ '{0}'.format(int((x-40)*50)) for x in plt.xticks()[0] ]
plt.gca().set_xticklabels(xticklabels)
plt.savefig('forward_strand.pdf')

plt.close('all')


