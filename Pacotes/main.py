from model.usuario import Usuario

usuario = Usuario('José Silva', 'jose@empresa.com.br')
print(usuario)
print(usuario.email.dominio)
print(usuario.email.usuario)