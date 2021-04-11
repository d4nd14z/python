import hashlib

def encryptPassword(password):    
    return hashlib.sha256(password.encode()).hexdigest()

def validateUser(Usuario):
    isValid = False
    if Usuario.getLogin() == "d4nd14z":
        if Usuario.getPassword() == "509dcefdc21ef402bd9159e8c9eef9f7cb530f800658256f397584d1cab26cff":
            isValid = True
    return isValid

def mostrarUsuario(Usuario):
    print(Usuario.getNombres() + "\t" + Usuario.getApellidos() + "\t" + Usuario.getEmail() + "\t\t" + Usuario.getPassword())