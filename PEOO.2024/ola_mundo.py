class Treinos:
    treinos = []

    def Inserir(self, treino):
        self.treinos.append(treino)

    def Listar(self):
        return self.treinos

    def Listar_Id(self, id):
        for treino in self.treinos:
            if treino.id == id:
                return treino
        return None

    def MaisRapido(self):
        treinos_ordenados = sorted(self.treinos, key=lambda treino: treino.distancia / treino.tempo, reverse=True)
        return treinos_ordenados

    def Atualizar(self, id, novo_treino):
        for i, treino in enumerate(self.treinos):
            if treino.id == id:
                self.treinos[i] = novo_treino
                return

    def Excluir(self, id):
        for i, treino in enumerate(self.treinos):
            if treino.id == id:
                del self.treinos[i]
                return

    def Abrir(self, arquivo):
        with open(arquivo, 'r') as f:
            dados = json.load(f)
            self.treinos = [Treino(**treino) for treino in dados]

    def Salvar(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([treino.__dict__ for treino in self.treinos], f, indent=4)
