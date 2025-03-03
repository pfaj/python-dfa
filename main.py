class Node:
    def __init__(self, name:str, adjacency: list[str], transition: list[list[str]], is_acceptor: bool):
        #INFO: Name is just used as an identifier
        self.name = name 
        #INFO: Used to keep track whether this is an acceptor state
        self.is_acceptor = is_acceptor
        self.create_edge(adjacency, transition)

    def create_edge(self, adjacency, transition):
        edge_list = []
        #INFO: Each node contains a list of its edges
        for i in range(len(adjacency)):
            edge_list.append(Edge(adjacency[i],transition[i]))

        self.edge = edge_list

    def __str__(self):
        print("State", self.name, "| Acceptor", self.is_acceptor)
        for edge in self.edge:
            print(f'    {self.name} --> {edge}')
        return ""

class Edge:
    def __init__(self, destination: list[str], transition: list[list[str]]):
        #INFO: The destination is the node that we point to
        self.destination = destination 
        self.transition = transition

    def __str__(self):
        return f'Destination: {self.destination}, Transition: {self.transition}'

class Graph:
    def __init__(self, valid_char: list[str]):
        self.nodes = [] 
        #INFO: Valid Char is used to delcare what 
        # characters are valid in the language
        self.valid_char = valid_char

    def add(self, node):
        self.nodes.append(node)

    def get_node(self, input_node: str) -> Node:
        for node in self.nodes:
            if input_node == node.name:
                return node 
        return None

    def __str__(self):
        for node in self.nodes:
            print(node)
        return ''
    
    def validate(self, string: str) -> bool:
        #INFO: The first item in the node list of the graph is the entry point of the DFA
        state = self.nodes[0]

        #INFO: Iterate through each character
        for char in string:
            valid_transition = False
            if char in self.valid_char: 
                #INFO: Iterates through each edge that the node has
                for edge in state.edge:
                    #INFO: Checking for transitions
                    if char in edge.transition:
                        valid_transition = True
                        state = self.get_node(edge.destination)
                        break

                if not valid_transition:
                    print('Trap State')
                    return False
            else:
                print(f'"{char}" is not a valid character.')
                return False

            print(f'Changed State: {state.name}')

        if state.is_acceptor:
            print('Valid')
            return state.is_acceptor 
        else:
            print('Trap State')
            return state.is_acceptor 


'''
    Aidan Jimenez
    3/2/25

    DFA INITIALIZATION:
    In this main function I declare a DFA that has the language 
    that contains chars (a,b) and has to start and end with b
'''

if __name__ == "__main__":
    #INFO: Setting up DFA/Graph
    #Graph input validates the valid chars for the language
    dfa = Graph(["a", "b"])

    # q0 State
    q0 = Node('q0',['q1'], [['b']], False)
    dfa.add(q0)

    # q1 State
    q1 = Node('q1',['q1', 'q2'], [['b'],['a']], True)
    dfa.add(q1)

    # q2 State
    q2 = Node('q2',['q2', 'q1'], [['a'],['b']], False)
    dfa.add(q2)

    string = str(input("Input the string to validate: "))

    # Check if Valid/Traverse DFA with input string.
    dfa.validate(string)
