class SLLNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
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
        
        
def main():
    node1 = SLLNode('apple')
    node2 = SLLNode(3)

    node1.set_next(node2)
    print(node1.get_next())

if __name__ == "__main__":
    main()