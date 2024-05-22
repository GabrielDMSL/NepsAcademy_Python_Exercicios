class Project:
    def __init__(self, programming_requirement, design_requirement):
        self.programming_requirement = programming_requirement
        self.design_requirement = design_requirement

class Programmer:
    def __init__(self, value_per_project: int, programming_skill: int):
        self.value_per_project = value_per_project
        self.programming_skill = programming_skill
        self.received_value = 0  # Inicialize received_value para 0

    def able(self, project: Project) -> bool:
        # Verifique se a habilidade do programador é maior ou igual ao requisito do projeto
        return self.programming_skill >= project.programming_requirement

class Designer:
    def __init__(self, value_per_project: int, design_skill: int):
        self.value_per_project = value_per_project
        self.design_skill = design_skill
        self.received_value = 0  # Inicialize received_value para 0

    def able(self, project: Project) -> bool:
        # Verifique se a habilidade do designer é maior ou igual ao requisito do projeto
        return self.design_skill >= project.design_requirement

if __name__ == "__main__":
    value, skill = map(int, input().split())
    programmer = Programmer(value, skill)

    value, skill = map(int, input().split())
    designer = Designer(value, skill)

    n = int(input())
    for _ in range(n):
        requirement_programming, requirement_design = map(int, input().split())
        project = Project(requirement_programming, requirement_design)

        # Verifique se tanto o programador quanto o designer podem completar o projeto
        if programmer.able(project) and designer.able(project):
            # Se eles puderem, adicione o valor do projeto ao received_value deles
            programmer.received_value += programmer.value_per_project
            designer.received_value += designer.value_per_project

    print(f"Programador: R$ {programmer.received_value}")
    print(f"Designer: R$ {designer.received_value}")
