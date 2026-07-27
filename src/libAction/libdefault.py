import re
from datetime import datetime

# Verifica se nomes estao vazios, possuem numeros ou caracteres invalidos


def nameValidation(name):
    # TESTE SE NOME DO PRODUTO ESTA VAZIO
    if not name:
        return None
    # TESTA SE NOME POSSUI CARACTERE NÃO PERMITIDO
    proibidos = ('@', '#', '$', '¨', '&', '*')
    for c in name:
        if c in proibidos:
            return False

    else:
        return name


def validateDoc(dados, tipo):
    # VERIFICA CPF
    if tipo == 'Fisica':
        # verifica se campo cpf esta vazio
        if not dados:
            return False, 'O camppo CPF não pode estar vazio!'

        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, dados))

        # Verifica se o CPF tem menos de 11 dígitos ou é uma sequência repetida
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False, 'O CPF digitado está incorreto'

        # Função para calcular o dígito verificador
        else:
            def calcular_digito_cpf(cpf, peso_inicial):
                soma = sum(int(cpf[i]) * (peso_inicial - i)
                           for i in range(peso_inicial - 1))
                resto = (soma * 10) % 11
                return resto if resto < 10 else 0

            # Calcula os dois dígitos verificadores
            digito1 = calcular_digito_cpf(cpf, 10)
            digito2 = calcular_digito_cpf(cpf, 11)

            # Verifica se os dígitos calculados correspondem aos do CPF
            if cpf[-2:] == f"{digito1}{digito2}":
                return True, cpf
            else:
                # menssage('O numero de CPF é inválido!', 'Erro no Cadastro')
                return False, 'Cpf invalido'

    # VERIFCA CNPJ
    if tipo == 'Juridico':
        if not dados:
            return False, 'Campo CNPJ não pode estar vazio'

    # Remove caracteres não numéricos
        cnpj = re.sub(r'\D', '', dados)

    # CNPJ deve ter 14 dígitos
        if len(cnpj) != 14:
            return False, 'CNPJ digitado está Incorreto'

        # Elimina CNPJs com todos os dígitos iguais (ex: 00000000000000)
        if cnpj == cnpj[0] * 14:
            return False, 'CNPJ digitado está Incorreto'

        # Função auxiliar para calcular dígito verificador
        def calcular_digito_cnpj(cnpj_parcial: str) -> str:
            pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            soma = sum(int(d) * pesos[i + (len(pesos) - len(cnpj_parcial))]
                       for i, d in enumerate(cnpj_parcial))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        # Calcula os dois dígitos verificadores
        primeiro_digito = calcular_digito_cnpj(cnpj[:12])
        segundo_digito = calcular_digito_cnpj(cnpj[:12] + primeiro_digito)

        if cnpj[-2:] == primeiro_digito + segundo_digito:
            return True, cnpj
        else:
            return False, 'CNPJ invalido'


def dataValidator(dados):
    data = str(dados)
    data_obj = datetime.strptime(data, "%d/%m/%Y")
    data_str = data_obj.strftime("%Y-%m-%d")
    return data_str
