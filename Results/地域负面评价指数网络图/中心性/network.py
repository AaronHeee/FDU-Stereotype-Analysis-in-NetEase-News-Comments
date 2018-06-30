import networkx as nx
#G= nx.Graph()
DG = nx.DiGraph()
f=open('province_data.txt','r')
data=f.readlines()
edgelist=[]
for i in range(34):
    row=data[i].split(' ')
    for j in range(34):
        edgelist.append((i+1,j+1,float(row[j])))
f.close()

DG.add_weighted_edges_from(edgelist)
score = nx.betweenness_centrality(DG,weight='weight')
f= open('betweenness_centrality.txt','w')
f.write(str(score))
f.close()


score = nx.eigenvector_centrality(DG,weight='weight')
f= open('eigenvector_centrality.txt','w')
f.write(str(score))
f.close()