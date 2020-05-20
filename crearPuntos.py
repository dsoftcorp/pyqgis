import random

def CreaCapaPuntos(n):
    layer = QgsVectorLayer("Point?crs=EPSG:4326","capa3","memory")
    layer.dataProvider().addAttributes([QgsField("id", QVariant.Int)] )
    layer.updateFields()
    indice = len(list(layer.getFeatures()))    
    for pt in range(indice + 1,indice + n + 1):
            feature = QgsFeature()
            feature.setFields(layer.fields())
            feature.setAttribute("id",pt)
            
            x = random.randint(1,50)
            y = random.randint(1,50)
            
            punto = QgsPointXY(x,y)
            geom = QgsGeometry.fromPointXY(punto)
            
            feature.setGeometry(geom)
            layer.dataProvider().addFeatures([feature])
    print("Se agregaron " + str(n) + " puntos correctamente")
    return layer

puntos = CreaCapaPuntos(50)
QgsProject.instance().addMapLayer(puntos)
