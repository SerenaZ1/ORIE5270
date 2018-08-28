import heapq

def get_edges(name_txt_file):
    edges = []
    f = open(name_txt_file)
    num = 1
    for line in f:
        if num % 2 != 0:
            node_start = int(line[:-1])
        else:
            line = line[:-1]
            if line != '':
                values = line.split(',')
                id = 1
                for i in range(len(values)):
                    if id % 2 != 0:
                        node_end = int(values[i][1:])
                    else:
                        weight = int(values[i][:-1])
                        edges.append((node_start,node_end,weight))
                    id += 1
        num += 1
    f.close()
    n = (num - 1) / 2
    return edges, n


def get_path(idx, start, end):
    path = [end]
    last = idx[end]
    while last != start:
        path.append(last)
        last = idx[last]
    if start != end:
        path.append(start)
    print (list(reversed(path)))
    return list(reversed(path))

def find_negative_cycles(name_txt_file):
    edges, n = get_edges(name_txt_file)
    dis = [float('inf')] * (n + 1)
    idx = [0] * (n + 1)
    dis[1] = 0
    for i in range(n - 1):
        for edge in edges:
            if dis[edge[1]] > dis[edge[0]] + edge[2]:
                idx[edge[1]] = edge[0]
                dis[edge[1]] = dis[edge[0]] + edge[2]

    has_negative_loop = False
    for edge in edges:
        if dis[edge[1]] > dis[edge[0]] + edge[2]:
            has_negative_loop = True
            break
    if has_negative_loop == True:
        get_path(idx, edge[1],edge[1])
    else:
        print ("")


def find_shortest_path(name_txt_file, source, destination):
    edges, n = get_edges(name_txt_file)
    graph = [[float('inf')] * (n+1) for i in range(n+1)]
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    #print graph
    F = [source]
    S = []
    dis = [float('inf')] * (n + 1)
    dis[source] = 0
    idx = [0] * (n + 1)
    isvisted = [False] * (n + 1)
    isvisted[source] = True

    dis_list = [(dis[node], node) for node in F]
    heapq.heapify(dis_list)
    while F:
        cur = heapq.heappop(dis_list)[1]
        S.append(cur)
        F.remove(cur)
        for j in range(1,n):
            if graph[cur][j] == float('inf'):
                continue
            if isvisted[j] == False:
                dis[j] = dis[cur] + graph[cur][j]
                idx[j] = cur
                F.append(j)
                isvisted[j] = True
            else:
                if dis[j] > dis[cur] + graph[cur][j]:
                    dis[j] = dis[cur] + graph[cur][j]
                    idx[j] = cur
        dis_list = [(dis[node],node) for node in F]
        heapq.heapify(dis_list)
    get_path(idx,source,destination)
