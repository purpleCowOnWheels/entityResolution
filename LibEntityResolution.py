from statistics import mode

def getGraph(meta):
    pks = {}
    for table in meta:
        for pk in meta[table]:
            if pk in pks.keys():
                pks[pk] = set().union(pks[pk],meta[table])
            else:
                pks[pk] = meta[table]
    return(pks)

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def retrieveValue( pkFrom, pkTo, pkFromValue, tables ):
    if pkFrom is None or pkTo is None or pkFromValue is None:
        return None
    for table in tables:
        table = tables[table]
        if pkFrom in table.keys() and pkTo in table.keys():
            index = table[pkFrom].index( pkFromValue )
            pkToValue = table[pkTo][index]
            if pkToValue is not None:
                return( pkToValue )

def traversePath( thisPath, pkFromValue, tables ):
    mapping = {
                "thisPath": thisPath,
                "mappings": [ pkFromValue ]
                }
    for index, thisPk in enumerate( thisPath ):
        if index == (len(thisPath)-1):
            return( mapping )
        else:
            nextPk = thisPath[index+1]
        mapping["mappings"].append( retrieveValue( thisPk, nextPk, mapping["mappings"][-1], tables ) )

def traversePaths( paths, pkFromValue, tables ):
    allMappings = {}
    for index, thisPath in enumerate(paths):
        try:
            allMappings["path"+str(index)] = traversePath( thisPath, pkFromValue, tables )
        except:
            continue
    return( allMappings)


def pickWinningMap( candidateMaps ):
    candidateVals = []
    for candidate in candidateMaps:
        candidateVals.append(candidateMaps[candidate]["mappings"][-1])
    return( mode(candidateVals))
