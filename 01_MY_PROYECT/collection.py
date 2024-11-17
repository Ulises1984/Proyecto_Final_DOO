from document import Document
import csv

class Collection:
    def __init__(self, name):
        self.name = name
        self.documents = {}
        self.next_id = 1
    
    def add_document(self, document):
        self.documents[document.id] = document
    
    def delete_document(self, doc_id):
        self.documents.pop(doc_id, None)
    
    def search_document(self, doc_id):
        return self.documents.get(doc_id, None)
    
    def list_documents(self):
        return [str(doc) for doc in self.documents.values()]
    
    def import_csv(self, ruta_csv):
        try:
            with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
                index = 0
                while index < len(rows):
                    row = rows[index]
                    doc = Document(str(self.next_id), row)
                    self.add_document(doc)
                    self.next_id += 1
                    index += 1
        except FileNotFoundError:
            print(f"Archivo '{ruta_csv}' no encontrado.")
            
"""
# uso
if __name__ == "__main__":
    ruta_csv = r"C:\Users\ulise\Desktop\Ulises\IFTS11\ANALISIS_DE_SISTEMA_PLAN_NUEVO_2024\2DO_CUATRIMESTRE\03-DESARROLLO_ORIENTADO_A_OBJETOS\MY_PROYECT"
    coleccion = Collection("Ejemplo")
    coleccion.import_csv(ruta_csv)
    print(coleccion.list_documents())
"""