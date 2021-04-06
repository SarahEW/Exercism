class Garden:
    def __init__(self, diagram, students = []):
        self.diagram = diagram
        self.students = sorted(students) if len(students)>0 else \
        ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        
    def parse_rows(self):
        rows = self.diagram.split('\n')
        diagram_array = [[rows[0][i:i+2] for i in range(0, len(rows[0]), 2)],
                        [rows[1][i:i+2] for i in range(0, len(rows[1]), 2)]]
        return diagram_array
        
    def students_plants(self):
        plant_index = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}
        rows_split = Garden.parse_rows(self)
        students_plants = {}
        for i in range(len(rows_split[0])):
            plants = list(rows_split[0][i]+rows_split[1][i])
            plant_names = []
            for plant in plants:
                plant_names.append(plant_index[plant])
            students_plants[self.students[i]] = plant_names
        return students_plants
        
    def plants(self, student):
        plants = Garden.students_plants(self)[student]
        return plants

garden = Garden("VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"])
print(garden.plants("Xander"))