class Funcionario:
    prefixo = 'Instrutor'

    @classmethod # (cls) -> abreviação de class talvez
    def info(cls):
        return f'Esse é um {cls.prefixo}'

