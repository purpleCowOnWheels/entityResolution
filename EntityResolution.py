from LibEntityResolution import *
from ClassEntityResolution import *

data = {
    'A': { 'CMSID': [ 'a1', 'b1', 'c1', 'd1', 'e1' ],
           'ciqid': [ 'a2', 'b2', 'c2', 'd2', 'e2' ],
           'gvkey': [ 'a3', 'b3', 'c3', 'd3', 'e3' ],
           'valA1': [ 'a4', 'b4', 'c4', 'd4', 'e4' ],
           'valA2': [ 'a5', 'b5', 'c5', 'd5', 'e5' ],         
         },
    'B': { 'capiqid': [ 'a2', 'b2', 'c2', 'd2', 'e2' ],
           'gvkey':  [ 'a3', 'b3', 'c3*', 'd3', 'e3' ],
           'GenId2':  [ 'a6', 'b6', 'c6', 'd6', 'e6' ],
           'valB1':   [ 'a7', 'b7', 'c7', 'd7', 'e7' ],         
         },
    'C': { 'ciqid':  [ 'a2', 'b2', 'c2', 'd2', 'e2' ],
           'GSLE':   [ 'a8', 'b8', 'c8', 'd8', 'e8' ],
           'valC1':  [ 'a9', 'b9', 'c9', 'd9', 'e9' ],         
         },
    'D': { 'ciqid':  [ 'a2', 'b2', 'c2', 'd2', 'e2' ],
           'LEID':  [ 'a8', 'b8', 'c8', 'd8', 'e8' ],
           'GenId2': [ 'a6', 'b6', 'c6', 'd6', 'e6' ],
           'GenId':  [ 'a10', 'b10', 'c10', 'd10', 'e10' ],
           'InId':  [ 'a12', 'b12', 'c12', 'd12', 'e12' ],
           'valD1':  [ 'a11', 'b11', 'c11', 'd11', 'e11' ],         
         },
    'E': { 'GenId': [ 'a10', 'b10', 'c10', 'd10', 'e10' ],
           'valE1':  [ 'a13', 'b13', 'c13', 'd13', 'e13' ],         
         },
}

mt1 = mapTable( "A", [ ], data['A'] )
mt2 = mapTable( "B", [ ], data['B'] )
mt3 = mapTable( "C", [ ], data['C'] )
mt4 = mapTable( "D", [ ], data['D'] )
mt5 = mapTable( "E", [ ], data['E'] )

#mt1.addDiscId( discCompanyId( "CMSEntityId", "CMSID" ) )
mt1.addId( companyId( "capIqCompanyId", "ciqid", mt2, "capiqid" ) )
mt2.addId( companyId( "capIqCompanyId", "capiqid", mt3, "ciqid" ) )
mt1.addId( companyId( "GVKey", "gvkey", mt2, "gvkey" ) )
mt1.addId( companyId( "capIqCompanyId", "ciqid", mt3, "ciqid" ) )
mt3.addId( companyId( "LEID", "GSLE", mt4, "LEID" ) )
mt5.addId( companyId( "IDGeneric", "GenId", mt4, "GenId" ) )
mt2.addId( companyId( "IDGeneric2", "GenId2", mt4, "GenId2" ) )
#mt4.addDiscId( discCompanyId( "InId", "InId" ) )

#print( globalMapTables )
#meta = {'table1': set(['pk1', 'pk2', 'pk3' ]),
#         'table2': set(['pk2', 'pk3']),
#         'table3': set(['pk3', 'pk4']),
#         'table4': set(['pk1', 'pk5']),
#         'table5': set(['pk5', 'pk4']),
#        }

#print( mt3 )
mapTables = { 'A' : mt1,
              'B' : mt2,
              'C' : mt3,
              'D' : mt4,
              'E' : mt5
            }

graph = getGraph( mapTables )
paths = getAllPaths( graph, mt1, mt5 )
#print( graph )

#print( retrieveValue( mt1, mt2, "GVKey", "GVKey", 'c3' ))
#print( paths[0])
#print( traversePath( paths[0], 'c2', mapTables ) )

candidates = traversePaths( paths, 'c2', mapTables )
print( pickWinningMap( candidates ) )