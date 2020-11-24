from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


import sys
import heapq

from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
class Node():
    def __init__(self, name, G,coordinate):
        self.name = name
        self.previous = None
        self.distance = sys.maxsize
        self.adjacency_list = []
        self.visited = False
        G.attr('Node', shape='box',fontsize='60',color='#E5E4E2',font='Helvetica')
        G.node(self.name,pos=coordinate)


    def __lt__(self, other):
        return self.distance < other.distance


class Edge():
    def __init__(self, node1, node2, distance, G):
        self.start_vertex = node1
        self.end_vertex = node2
        self.weight = distance
        self.start_vertex.adjacency_list.append(self)
        #self.end_vertex.adjacency_list.append(self)
        G.attr('Edge', fontsize='30')
        G.edge(str(node1.name), str(node2.name), label=node1.name[0:1]+'>'+node2.name[0:1]+'\n'+str(distance),arrowsize='3.0')
        #G.add_edge(node2.name, node1.name, weight=distance)


class Djkstra_Algorithm():

    def calculateShortestDistance(self, start_vertex,G):
        q = []
        start_vertex.distance = 0
        heapq.heappush(q, start_vertex)
        G.node(start_vertex.name,color='green')
        while q:
            current_vertex = heapq.heappop(q)
            for edge in current_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.end_vertex
                new_distance = u.distance + edge.weight

                if new_distance < v.distance:
                    v.previous = u
                    v.distance = new_distance
                    heapq.heappush(q, v)

    def getShortestPath(self, target_vertex, G):
        #print("shortest path distance from source:", target_vertex.distance)
        #print("shortest route from source:")
        G.node(target_vertex.name,color='red')
        vertex = target_vertex
        while vertex is not None:
            #print(vertex.name)
            if vertex.previous is not None:
                G.edge(str(vertex.previous.name), str(vertex.name), color='red',style='bold')
            vertex = vertex.previous

def convertToString(x,y):
    temp=str(x)+','+str(y)+'!'
    #print(temp)
    return temp

def run(var):

    G = Digraph( format='jpg',strict=True,engine="neato",node_attr={'color': 'lightblue2', 'style': 'filled'})
    G.attr(bgcolor='#BCC6CC')

    #node1 = Node('A', G)
    node1 = Node('Palashi', G,convertToString(0,0))

    #node2 = Node('B', G)
    node2 = Node('Azimpur', G,convertToString(0,3.5))

    #node3 = Node('C', G)
    node3 = Node('Dhaka Medical', G,convertToString(0,-12))

    #node4 = Node('D', G)
    node4 = Node('Lalbagh', G,convertToString(-13,0))

    #node5 = Node('E', G)
    node5 = Node('Nilkhet', G,convertToString(1,2.5))
    node6 = Node('Folab Road', G,convertToString(3,-3))
    node7 = Node('Shahid Minar', G,convertToString(3.5,-15))
    node8 = Node('Press Club', G,convertToString(-3,-22))
    node9 = Node('Shahbagh', G,convertToString(7,-17))
    node10 = Node('New Market', G,convertToString(5.5,3.5))


    #node6 = Node('F', G)

    #node7 = Node('G', G)

    #node8 = Node('H', G)

    #edge1 = Edge(node1, node2, 5, G)
    #edge11 = Edge(node2, node1, 6, G)
    #edge2 = Edge(node1, node8, 8, G)
    #edge22 = Edge(node8, node1, 9, G)
    #edge3 = Edge(node1, node5, 9, G)
    #edge33 = Edge(node5, node1, 10, G)
    #edge4 = Edge(node2, node4, 15, G)
    #edge44 = Edge(node4, node2, 16, G)
    #edge5 = Edge(node2, node3, 12, G)
    #edge55 = Edge(node3, node2, 13, G)
    #edge6 = Edge(node2, node8, 4, G)
    #edge66 = Edge(node8, node2, 5, G)
    #edge7 = Edge(node8, node3, 7, G)
    #edge77 = Edge(node3, node8, 8, G)
    #edge8 = Edge(node8, node6, 6, G)
    #edge88 = Edge(node6, node8, 7, G)
    edge1 = Edge(node1, node2, 3.5, G)
    edge2 = Edge(node2, node1, 4.5, G)
    edge3 = Edge(node1, node3, 12, G)
    edge4 = Edge(node3, node1, 13, G)
    edge5 = Edge(node1, node4, 13, G)
    edge6 = Edge(node4, node1, 14, G)
    edge7 = Edge(node1, node5, 7, G)
    edge8 = Edge(node5, node1, 8, G)
    edge9 = Edge(node1, node6, 4, G)
    edge10 = Edge(node6, node1, 5, G)
    edge11 = Edge(node2, node4, 10, G)
    edge12 = Edge(node4, node2, 11, G)
    edge13 = Edge(node2, node10, 5.5, G)
    edge14 = Edge(node10, node2, 6.5, G)
    edge15 = Edge(node3, node4, 22, G)
    edge16 = Edge(node4, node3, 23, G)
    edge17 = Edge(node3, node7, 3.5, G)
    edge18 = Edge(node7, node3, 4.5, G)
    edge19 = Edge(node3, node8, 12, G)
    edge20 = Edge(node8, node3, 13, G)
    edge21 = Edge(node5, node6, 5, G)
    edge22 = Edge(node6, node5, 6, G)
    edge23 = Edge(node5, node10, 2.1, G)
    edge24 = Edge(node10, node5, 3.1, G)
    #edge25 = Edge(node6, node7, 7.5, G)
    #edge26 = Edge(node7, node6, 8.5, G)
    edge25 = Edge(node6, node7, 17.5, G)
    edge26 = Edge(node7, node6, 18.5, G)
    edge27 = Edge(node6, node9, 18, G)
    edge28 = Edge(node9, node6, 19, G)
    edge29 = Edge(node7, node9, 17, G)
    edge30 = Edge(node9, node7, 18, G)
    edge31 = Edge(node8, node9, 19, G)
    edge32 = Edge(node9, node8, 20, G)









    vertex_list = (node1, node2, node3, node4, node5, node6, node7, node8,node9,node10)

    algorithm = Djkstra_Algorithm()


    if(len(var)==2):
        for i in vertex_list:
            if i.name == var[0]:
                src = i
            elif i.name == var[1]:
                dest = i
        algorithm.calculateShortestDistance(src, G)

        algorithm.getShortestPath(dest, G)
    #algorithm.calculateShortestDistance(node10,G)

    #algorithm.getShortestPath(node8, G)

    #print(G.source)
    G.render('./map/static/map/images/newout')

    #G.render('test-output/newout', view=True)

    #algorithm.getShortestPath(node4)


def home(request):

    run()
    return render(request,'map/home.html')
def about(request):
    return render(request,'map/about.html',{'title':'about'})


from django.shortcuts import render

from .form import PathForm
varList=[]

def get_path(request):

    if (request.method=='POST'):
        path_form = PathForm(request.POST)
        if path_form.is_valid():
            varList.append(path_form.cleaned_data['source'])
            varList.append(path_form.cleaned_data['destination'])


        print(varList )

    path_form = PathForm()
    # if this is a POST request we need to process the form data
    run(varList)
    return render(request,'map/form.html',{'form':path_form})

def map(request):
    return render(request,'map/mapdesign.html')