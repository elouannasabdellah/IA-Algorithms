
graphe={
    "S": ["B","D","A"],
    "A": ["C"],
    "B": ["D"],
    "C":["G","D"],
    "D": ["G"],
    "G":[]
}
def bfs(graphe,start,goal):
    visited=[]
    queue=[[start]]
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes= graphe.get(node,[])
            for node2 in adjacent_nodes:
                new_path=path.copy()
                new_path.append(node2)
                queue.append(new_path)

solution = bfs(graphe, "S","G")
print("solustion BFS : ",solution)

def dfs(graphe, start,goal):
    visited=[]
    stack=[[start]]
    while stack:
        path=stack.pop()
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node ==goal:
            return path
        else:
             adjacent_nodes= graphe.get(node,[])
             for node2 in adjacent_nodes:
                 new_path=path.copy()
                 new_path.append(node2)
                 stack.append(new_path)
solutionDfs=dfs(graphe,"S","G")
print("Solution de DFS: ", solutionDfs)

graph={

    "S":[ ("A",2),("B",3),("D",5) ],
    "A": [ ("C",4) ],
    "B":[("D",4)],
    "C":[("D",1),("G",2)],
    "D":[("G",5)],
    "G":[]
}        

# 2. Fonction pour calculer le coût total d'un chemin
def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]

# 3. L'algorithme UCS
def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=lambda path: path_cost(path)[0])
        
        path = queue.pop(0)
        node = path[-1][0] # On récupère le nom du dernier noeud
        
        if node in visited:
            continue   
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)

solution2 = ucs(graph, 'S', 'G')

print('Solution is', solution2)
print('Cost of Solution is', path_cost(solution2)[0])
    


heuristique = {"S": 7, "A": 5, "B": 6, "C": 2, "D": 4, "G": 0}

def greedy_search(graph, start, goal, heuristique):
    visited = []
    queue = [[start]] # On stocke juste les noms des nœuds ici
    
    while queue:
        # TRI GLOUTON : On trie selon la valeur h(n) du dernier nœud du chemin
        queue.sort(key=lambda path: heuristique[path[-1]])
        
        path = queue.pop(0)
        node = path[-1]
        
        if node in visited:
            continue
            
        visited.append(node)
        if node == goal:
            return path
        
        # On ajoute les voisins (en ignorant le coût des arêtes cette fois)
        for (voisin, cout_arete) in graph.get(node, []):
            new_path = list(path)
            new_path.append(voisin)
            queue.append(new_path)

# --- Test ---
solution = greedy_search(graph, "S", "G", heuristique)
print("Solution Greedy Search :", solution)

# --------------      ---  pour A* -----------------------------
def get_g_cost(path):
    """Calcule le coût réel parcouru g(n)"""
    return sum(cost for node, cost in path[1:])

def a_star(graph, start, goal, heuristique):
    # La queue stocke des chemins avec leurs coûts : [[(noeud, cout_depuis_parent)]]
    queue = [[(start, 0)]]
    visited = set()

    while queue:
        # TRI PAR f(n) = g(n) + h(n)
        queue.sort(key=lambda path: get_g_cost(path) + heuristique[path[-1][0]])
        path = queue.pop(0)
        node = path[-1][0]
        
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for (voisin, cost) in graph.get(node, []):
                new_path = list(path)
                new_path.append((voisin, cost))
                queue.append(new_path)

# --- Exécution ---
solution = a_star(graph, "S", "G", heuristique)
print("Solution A* :", [node for node, cost in solution])
print("Coût total :", sum(cost for node, cost in solution))


