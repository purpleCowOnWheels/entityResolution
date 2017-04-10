#A script to generate a graph-based entity resolution
from LibEntityResolution import *
import ClassEntityResolution

meta = {'table1': set(['pk1', 'pk2']),
         'table2': set(['pk2', 'pk3']),
         'table3': set(['pk3', 'pk4']),
         'table4': set(['pk1', 'pk5']),
         'table5': set(['pk5', 'pk4']),
        }

tables = {
    'table1': { 'pk1': [ 'a1', 'b1', 'c1', 'd1', 'e1' ],
                'pk2': [ 'a2', 'b2', 'c2', 'd2', 'e2' ],
            },
    'table2': { 'pk2': [ 'a2', 'b2', 'c2', 'd2', 'e2' ],
                'pk3': [ 'a3', 'b3', 'c3', 'd3', 'e3'],
            },
    'table3':{  'pk3': [ 'a3', 'b3', 'c3', 'd3', 'e3'],
                'pk4': [ 'a4', 'b4', 'c4', 'd4', 'e4' ],
            },
    'table4':{  'pk1': [ 'a1', 'b1', 'c1', 'd1', 'e1' ],
                'pk5': [ 'a5', 'b5', 'c5', 'd5', 'e5' ],
            },
    'table5':{  'pk4': [ 'a4', 'b4', 'c4', 'd4', 'e4' ],
                'pk5': [ 'a5', 'b5', 'c5', 'd5', 'e5' ],
            }
}

paths = list(dfs_paths(getGraph(meta), 'pk1', 'pk4' ) )

candidates = traversePaths( paths, 'c1', tables )
print( pickWinningMap( candidates ) )

