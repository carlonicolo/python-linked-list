class DLLNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        
    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)
    
    def get_data(self):
        """Return the self.data attribute."""
        return self.data
    
    def set_data(self, new_data):
        """Replace the existing value of self.data attribute with new_data 
        parameter"""
        self.data = new_data
    
    def get_next(self):
        """Return the self.next attribute"""
        return self.next
    
    def set_next(self, new_next):
        """Replace the existing value of self.next attribute with new_next parameter."""
        self.next = new_next
    
    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous
    
    def set_next(self, new_previous):
        """Replace the existing value of self.previous attribute with new_previous parameter."""
        self.previous = new_previous
        
        
def main():
    node1 = DLLNode('apple')
    node2 = DLLNode(3)

    node1.set_next(node2)
    print(node1.get_next())

if __name__ == "__main__":
    main()