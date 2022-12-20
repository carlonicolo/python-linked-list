import pytest
import singleLinkedListsNode

def test_data_node():
    node1 = singleLinkedListsNode.SLLNode('apple')
    assert node1.get_data() == 'apple'
    
def test_set_data_node():
    node1 = singleLinkedListsNode.SLLNode('apple')
    node1.set_data('pippo')
    assert node1.get_data() == 'pippo'
    
