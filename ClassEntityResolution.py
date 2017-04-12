globalMapTables = [ ]

class mapTable:
    'A heirarchical company with parents, children and securities'
    tableCount = 0

    def __init__(
        self,
        name,
        ids,            #array of companyIds at the same level of heirarchy
        dataDict,       #dictionary of colnames and data
        ):
        
        self.name           = name
        self.ids            = ids       #array of companyIds at the same level of heirarchy
#        self.parentIds      = [ ]      #array of companyIds up one level of heirarchy
#        self.childIds       = [ ]      #array of companyIds down one level of heirarchy
#        self.securityKeys   = [ ]      #array of securityIds held at this level of heirarchy
        self.dataDict       = dataDict
        mapTable.tableCount += 1
        globalMapTables.append( name )
        
    def printCount(self):
        print( "Total Companies %d" % Company.companyCount )

    def getIdNames(self):
        idNames = [ ]
        for id in self.ids:
            idNames.append( id.name )
        return( idNames )
        
    def addId( self, this_companyId ):
        self.ids.append( this_companyId )
        
        #if the other table doesn't have the converse mapping, add it
        if this_companyId.name_otherTable is not None and this_companyId.name_otherTable not in this_companyId.otherTable.getIdNames():
            that_companyId = companyId( this_companyId.name, this_companyId.name_otherTable, self, this_companyId.name_table )
            this_companyId.otherTable.ids.append( that_companyId )
            
    def getMappings( self ):
        mappings = {}
        for id in self.ids:
            mappings[ self.name + "_" + id.name ] = set()
            
            #get all the things within the same table it connects with
            for id2 in self.ids:
#                print( id2 )
                if id == id2:
                    mappings[ self.name + "_" + id.name ].add( id2.otherTable.name + "_" + id2.name )
                else:
                    mappings[ self.name + "_" + id.name ].add( self.name + "_" + id2.name )                                
        return( mappings )
                

    
    def __str__( self ):
        output = "\n############################\nTable Name: " + self.name + "\n\nConnected Ids:"
        for id in self.ids:
            output = output + "\n" + id.__str__()
        output = output + "\n############################"
        return( output )
            
        
class companyId:
    'a single instance of an identifier, telling what its called, where it maps to, and its name in the mapped table'
    def __init__(self, name, name_table, otherTable, name_otherTable ):
        self.name               = name                  #the global name of this identifier
        self.name_table         = name_table            #what the field is called in the table
        self.otherTable         = otherTable            #a different map table containing this Id
        self.name_otherTable    = name_otherTable       #what the field is called in the other table

        if otherTable != None and otherTable.name not in globalMapTables:
            raise Exception( 'Links to non-existant table '+ name_otherTable )
            
    def  __str__(self):
        output = ""
        output = output + "Global Name: " + self.name + "\n"
        output = output + "Name in Table: " + self.name_table + "\n"
        output = output + "Other Table: " + self.otherTable.name + "\n"
        output = output + "Name in Other Table: " + self.name_otherTable + "\n"
        return( output )
        
    def getClass(self):
        return( self.__class__.__name__)

