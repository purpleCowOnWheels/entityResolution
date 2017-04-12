from statistics import mode

def getGraph( mapTables ):
    mappings = {}
    for mapTable in mapTables:
        these_mappings = mapTables[mapTable].getMappings()
        for this_mapping in these_mappings:
            if this_mapping in mappings.keys():
                mappings[this_mapping].union( these_mappings[ this_mapping ])
            else:
                mappings[this_mapping] = these_mappings[ this_mapping ]
    return( mappings )

def unique( myList ):
    result = [ ]
    for x in myList:
        if x not in result:
            result.append( x )
    return( result )

def getAllPaths( graph, startTable, goalTable ):
    allPaths = list()
    for startId in startTable.ids:
        for endId in goalTable.ids:
            start = startTable.name + "_" + startId.name
            end   = goalTable.name + "_" + endId.name
            thesePaths = list( getSomePaths(graph, start,end ) )
        for path in thesePaths:
            allPaths.append( path )
    return( unique( allPaths ) )
    
def getSomePaths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def retrieveValue( mtFrom, mtTo, fromCol, toCol, valFrom ):
    #get the id we're coming from so we can get the local column name
    for id in mtFrom.ids:
        if id.name == fromCol:
            idFrom = id

    for id2 in mtTo.ids:
        if id2.name == toCol:
            idTo = id2

    try:
        #since we're running all paths btw two tables, if your path is starting on a column that isn't relevant it wont have your starting value. Null these out. Should eventually filter these earlier
        index = mtFrom.dataDict[ idFrom.name_table ].index( valFrom )
    except:
        return( None )
    valTo = mtTo.dataDict[ idTo.name_table ][index]
    return( valTo )

def traversePath( thisPath, valFrom, tables ):
    mapping = {
                "thisPath": thisPath,
                "values": [ valFrom ]
                }
    for index, node in enumerate( thisPath ):
        if index == (len(thisPath)-1):
            return( mapping )
        else:
            nextNode = thisPath[ index+1 ]
#        print( valFrom )
        node        = node.split("_")
        nextNode    = nextNode.split("_")
        valTo = retrieveValue( tables[ node[0] ], tables[ nextNode[0] ], node[1], nextNode[1], valFrom )
        mapping["values"].append( valTo )
        valFrom = valTo
    return( mapping )

def traversePaths( paths, valFrom, tables ):
    allMappings = []
    for index, thisPath in enumerate(paths):
#        print( thisPath )
        allMappings.append( traversePath( thisPath, valFrom, tables ) )
    return( allMappings )

def pickWinningMap( candidateMaps ):
    candidateVals = []
    for candidate in candidateMaps:
        candidateVals.append(candidate["values"][-1])
    candidateVals = filter( None, candidateVals )
    return( mode(candidateVals) )
