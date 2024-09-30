class User:
    _id_counter = 1

    def _init_(self, nome, sobrenome, email):
        self.id_user = User._id_counter
        User._id_counter += 1
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email

    def _str_(self):
        return f"ID: {self.id_user}, Nome: {self.nome} {self.sobrenome}, Email: {self.email}"


class Sala:
    def _init_(self, nome_sala):
        self.nome_sala = nome_sala

    def _str_(self):
        return f"Sala: {self.nome_sala}"


class Equipment:
    def _init_(self, nome_equip, serial):
        self.nome_equip = nome_equip
        self.serial = serial

    def _str_(self):
        return f"Equipment: {self.nome_equip}, Serial: {self.serial}"


class UserController:
    def _init_(self, is_student=True):
        self.is_student = is_student
        self.usuarios = []

    def listar_usuarios(self):
        return self.usuarios

    def adicionar_usuario(self, user):
        self.usuarios.append(user)

    def deletar_usuario(self, user_id):
        self.usuarios = [user for user in self.usuarios if user.id_user != user_id]

    def atualizar_usuario(self, user_id, novo_email):
        for user in self.usuarios:
            if user.id_user == user_id:
                user.email = novo_email


class SalaController:
    def _init_(self):
        self.salas = []

    def adicionar_sala(self, sala):
        self.salas.append(sala)


class EqpController:
    def _init_(self):
        self.equipamentos = []

    def adicionar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)


def main():
    controllerA = UserController(is_student=True)
    controllerP = UserController(is_student=False)
    controllerSala = SalaController()
    controllerEqp = EqpController()

    user_aluno = User("Joao", "Lucas", "joao@gmail.com")
    user_professor = User("Thiago", "Reis", "thiagoreis@gmail.com")

    controllerA.adicionar_usuario(user_aluno)
    controllerP.adicionar_usuario(user_professor)

    classroom = Sala("5ESPG")
    equipment = Equipment("Alicate", "12345")

    controllerSala.adicionar_sala(classroom)
    controllerEqp.adicionar_equipamento(equipment)

    alunos = controllerA.listar_usuarios()
    if alunos:
        print("Lista de Alunos:")
        for aluno in alunos:
            print(aluno)
    else:
        print("Nenhum aluno encontrado.")

    professores = controllerP.listar_usuarios()
    if professores:
        print("Lista de Professores:")
        for professor in professores:
            print(professor)
    else:
        print("Nenhum professor encontrado.")

    # Exemplo de atualização e exclusão de usuário:
    # controllerP.deletar_usuario(4)
    # controllerP.atualizar_usuario(9, "teste@gmail.com")


