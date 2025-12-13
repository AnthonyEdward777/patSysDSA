def sort_by_severity(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return
    
    swapped = True

    while swapped:
        swapped = False
        current = linked_list.head


        while current.next is not None:
            if current.data.getSeverity() > current.next.data.getSeverity():

                current.data, current.next.data = current.next.data, current.data
                swapped = True
           
            current = current.next

def sort_by_severity_desc(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return
    
    
    swapped = True

    while swapped:
        swapped = False
        current = linked_list.head

        while current.next is not None:

            if current.data.getSeverity() < current.next.data.getSeverity():
                current.data, current.next.data = current.next.data, current.data
                swapped = True
           
            current = current.next
