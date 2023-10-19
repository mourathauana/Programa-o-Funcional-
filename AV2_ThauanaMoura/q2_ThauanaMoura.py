register = lambda file : open(file, "a+"). writelines(f"{input ('Digite o usuario')} {input('Digite a senha')}\n")

login = lambda file : print ("SUCESSO") if (input("Digite usuario"), input("Digite a senha")) in [tuple (line.strip().split(" ")) for line in open (file, "r")] else print("FRACASSO")


file = "Aplicação.txt"
login (file)
