f = open('../data/SubjectNetwork.tsv')
lines = [line.strip() for line in f]
f.close()

subjects = []
subject_trees = []
subject_graphs = []

#Read the file into an array called subjects
for line in lines:
	subject = [x.split(' -- ') for x in line.split(';')]
	subjects.append(subject)

#Create edges between each adjacent subject in a subject group to form a tree
# [a,b,c] => a;b and b;c
for subject in subjects:
	for s in subject:
		l = len(s)
		if l > 1:
			for i in range(0,l-1):
				subject_trees.append([s[i],s[i+1]])

#Create edges between each of the top subject headings for a book
# [a,b,c],[d,e,f],[g,h] ==> a;d and a;g and d;g
for subject in subjects:
	l = len(subject)
	if l > 1:
		for i in range(0,l-1):
			for j in range(1,l):
				if i != j and subject[i][0] != subject[j][0]:
					subject_graphs.append([subject[i][0],subject[j][0]])

#write to file
import sys
sys.stdout = open('../data/top_subject_edge_table.csv','w')
print 'Source;Target;Type'
for sg in subject_graphs:
	print sg[0] + ";" + sg[1] + ";Undirected"
# for st in subject_trees:
# 	print st[0] + ";" + st[1] + ";Directed"


if __name__ == '__main__':
	pass