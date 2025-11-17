def find_first_crashed_process(crashed_processes, children_map):
    """
    Find the first crashed process that doesn't have a crashed parent.
    Returns the first such process in the order of crashed_processes.
    
    Time: O(n + m) where n = len(crashed_processes), m = total children
    Space: O(n + m)
    """
    # Build child -> parent mapping in one pass
    parent_of = {
        child: parent
        for parent, children in children_map.items()
        for child in children
    }
    
    # Convert to set for O(1) lookup
    crashed = set(crashed_processes)
    
    # Find first crashed process whose parent is NOT crashed
    # This is the root of the crash chain
    for process in crashed_processes:
        if parent_of.get(process) not in crashed:
            return process
    
    return -1

