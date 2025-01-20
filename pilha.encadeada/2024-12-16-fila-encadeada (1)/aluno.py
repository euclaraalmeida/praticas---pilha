class Aluno:
    def __init__(self, nome:str, matricula:int):
        self.__nome = nome
        self.__matricula = matricula
    
    def __str__(self):
        return f'{self.__nome} - {self.__matricula}'
    
    def __eq__(self, outro):
        return self.__matricula == outro.__matricula