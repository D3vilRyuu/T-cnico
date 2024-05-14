# 7 - Crie um programa que imprima uma lista de tarefas, e que em seguida imprima na tela a mensagem 
# ("Tarefa x concluída") e remova da lista. O programa deve repetir esse procedimento até todas as tarefas 
# serem concluídas, e então exibir "lista de tarefas finalizada!"

tarefas = ["Varrer a casa", "Limpar o banheiro", "Ir para a escola", "Almoçar"]
print(f"Lista de tarefas: {tarefas}")
elementos = len(tarefas)

for tarefa in range(elementos):
    tarefa = tarefas[0]
    print(f"Tarefa: {tarefa} foi concluída")
    tarefas.remove(tarefa)
    
print(tarefas)
print("Lista de tarefas finalizada!")
 

    
    