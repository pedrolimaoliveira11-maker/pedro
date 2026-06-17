# ================================================
# app.py - Calculadora de IMC (Índice de Massa Corporal)
# ================================================
# Este arquivo contém um programa Python completo e independente
# para calcular o IMC diretamente no terminal (VSCode Terminal).
#
# ⚠️ IMPORTANTE: Este app.py NÃO está integrado com o index.html
# São dois projetos SEPARADOS e independentes para o mesmo objetivo.
# O app.py é para uso em linha de comando (Python).
# O index.html é para uso no navegador (HTML + JavaScript).
#
# COMO USAR NO VSCODE:
# 1. Abra a pasta do projeto no VSCode
# 2. No terminal integrado (Ctrl + J), digite: python app.py
# 3. Siga as instruções que aparecem na tela
#
# O CÓDIGO ESTÁ TOTALMENTE COMENTADO LINHA POR LINHA
# para facilitar o entendimento e aprendizado de iniciantes.
# ================================================

# ================================================
# SEÇÃO 1: DEFINIÇÃO DA FUNÇÃO PRINCIPAL
# ================================================

# Linha 1: Definimos uma função chamada 'calcular_imc'
# Funções servem para organizar o código e permitir reutilização
def calcular_imc():
    # Linha 2: Imprime uma linha em branco para dar espaço visual
    print()
    
    # Linha 3: Imprime uma linha decorativa superior
    print("╔════════════════════════════════════════════════════════════╗")
    
    # Linha 4: Imprime o título centralizado do programa
    print("║           🧮 CALCULADORA DE IMC - ÍNDICE DE MASSA CORPORAL           ║")
    
    # Linha 5: Imprime a linha decorativa inferior
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    
    # Linha 6: Pede o nome do usuário para personalizar a experiência
    # A função input() sempre retorna uma string (texto)
    nome = input("👤 Digite seu nome completo: ")
    
    # Linha 7: Imprime uma saudação amigável usando f-string (formatação moderna)
    print(f"\nOlá, {nome}! 👋 Vamos calcular seu IMC de forma rápida e precisa.")
    print()
    
    # ================================================
    # SEÇÃO 2: LOOP DE VALIDAÇÃO DE ENTRADA DE DADOS
    # ================================================
    
    # Linha 8: Iniciamos um loop 'while True' para repetir até o usuário digitar dados válidos
    # Isso evita que o programa quebre se o usuário errar a digitação
    while True:
        try:
            # Linha 9: Pedimos o peso em quilogramas
            # Usamos input() para ler do teclado
            peso_input = input("⚖️  Digite seu peso em quilogramas (exemplo: 72.5): ")
            
            # Linha 10: Convertemos o texto digitado para número decimal (float)
            # Isso é necessário porque input() retorna sempre string
            peso = float(peso_input)
            
            # Linha 11: Validamos se o peso é maior que zero
            # IMC não faz sentido com peso zero ou negativo
            if peso <= 0:
                # Linha 12: Mostramos mensagem de erro amigável
                print("❌ Erro: O peso deve ser um número maior que zero. Tente novamente.\n")
                # Linha 13: 'continue' faz o loop voltar para o início (pedir peso novamente)
                continue
            
            # Linha 14: Pedimos a altura em metros
            altura_input = input("📏 Digite sua altura em metros (exemplo: 1.78): ")
            
            # Linha 15: Convertemos a altura para float
            altura = float(altura_input)
            
            # Linha 16: Validamos se a altura é maior que zero
            if altura <= 0:
                print("❌ Erro: A altura deve ser um número maior que zero. Tente novamente.\n")
                continue
            
            # Linha 17: Se chegamos até aqui, significa que os dados são válidos
            # Então usamos 'break' para sair do loop while
            break
            
        except ValueError:
            # Linha 18: Este bloco 'except' captura erros de conversão
            # Acontece quando o usuário digita letras ou símbolos inválidos
            print("❌ Erro: Por favor, digite apenas números. Use ponto (.) para separar decimais.")
            print("   Exemplo correto: 70.5   |   Exemplo incorreto: 70,5 ou setenta\n")

    # ================================================
    # SEÇÃO 3: CÁLCULO DO IMC
    # ================================================
    
    # Linha 19: Calculamos o IMC usando a fórmula oficial da OMS
    # Fórmula: IMC = peso ÷ (altura × altura)   ou   peso / (altura ** 2)
    imc = peso / (altura ** 2)
    
    # Linha 20: Arredondamos o resultado para apenas 2 casas decimais
    # round() é uma função nativa do Python
    imc_arredondado = round(imc, 2)
    
    # ================================================
    # SEÇÃO 4: CLASSIFICAÇÃO DO IMC (segundo OMS)
    # ================================================
    
    # Linha 21: Usamos estrutura if-elif-else para classificar o IMC
    # Cada faixa tem uma classificação e uma mensagem educativa
    if imc < 18.5:
        # Linha 22: Abaixo do peso
        classificacao = "Abaixo do peso"
        emoji = "🔴"
        mensagem = "Você está abaixo do peso ideal. Recomenda-se consultar um nutricionista."
        cor_terminal = "\033[91m"  # Vermelho no terminal (código ANSI)
    elif imc < 25.0:
        # Linha 23: Peso normal (faixa saudável)
        classificacao = "Peso normal"
        emoji = "🟢"
        mensagem = "Excelente! Seu peso está dentro da faixa considerada saudável."
        cor_terminal = "\033[92m"  # Verde
    elif imc < 30.0:
        # Linha 24: Sobrepeso
        classificacao = "Sobrepeso"
        emoji = "🟡"
        mensagem = "Você está com sobrepeso. Pequenas mudanças na alimentação e exercícios podem ajudar."
        cor_terminal = "\033[93m"  # Amarelo
    else:
        # Linha 25: Obesidade
        classificacao = "Obesidade"
        emoji = "🔴"
        mensagem = "Você está na faixa de obesidade. É importante procurar orientação médica e nutricional."
        cor_terminal = "\033[91m"  # Vermelho
    
    # ================================================
    # SEÇÃO 5: EXIBIÇÃO DOS RESULTADOS
    # ================================================
    
    # Linha 26: Imprimimos uma linha decorativa
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║                        📊 RESULTADO                          ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    # Linha 27: Mostramos o nome do usuário em maiúsculo
    print(f"Usuário: {nome.upper()}")
    
    # Linha 28: Mostramos o IMC calculado com 2 casas decimais
    print(f"Seu IMC calculado: {imc_arredondado} kg/m²")
    
    # Linha 29: Mostramos a classificação com emoji e cor (se o terminal suportar)
    print(f"Classificação: {emoji} {cor_terminal}{classificacao}\033[0m")
    
    # Linha 30: Mostramos a mensagem educativa
    print(f"\n💡 {mensagem}")
    
    # ================================================
    # SEÇÃO 6: TABELA DE REFERÊNCIA
    # ================================================
    
    # Linha 31: Exibimos a tabela oficial de classificação do IMC
    print("\n📋 TABELA DE CLASSIFICAÇÃO DO IMC (Organização Mundial da Saúde - OMS):")
    print("─────────────────────────────────────────────────────────────────")
    print("│ IMC                  │ Classificação      │ Risco à saúde      │")
    print("─────────────────────────────────────────────────────────────────")
    print("│ Menor que 18,5       │ Abaixo do peso     │ Baixo              │")
    print("│ 18,5 a 24,9          │ Peso normal        │ Normal             │")
    print("│ 25,0 a 29,9          │ Sobrepeso          │ Aumentado          │")
    print("│ 30,0 a 34,9          │ Obesidade grau I   │ Moderado           │")
    print("│ 35,0 a 39,9          │ Obesidade grau II  │ Alto               │")
    print("│ Maior ou igual a 40  │ Obesidade grau III │ Muito alto         │")
    print("─────────────────────────────────────────────────────────────────")
    
    # ================================================
    # SEÇÃO 7: MENSAGEM FINAL E REPETIÇÃO
    # ================================================
    
    # Linha 32: Mensagem importante sobre o IMC
    print("\n⚠️  IMPORTANTE: O IMC é apenas uma ferramenta de triagem populacional.")
    print("   Ele não substitui uma avaliação médica ou nutricional completa.")
    print("   Fatores como massa muscular, idade, sexo e composição corporal também importam.")
    
    # Linha 33: Dica de saúde
    print("\n✅ Dica de saúde: Mantenha uma alimentação equilibrada e pratique")
    print("   atividades físicas regularmente. Cuide do seu corpo! 💪")
    
    # Linha 34: Perguntamos se o usuário quer fazer novo cálculo
    print("\n" + "─" * 60)
    resposta = input("🔄 Deseja calcular o IMC de outra pessoa? (s/n): ").strip().lower()
    
    # Linha 35: Verificamos a resposta do usuário
    if resposta == "s" or resposta == "sim" or resposta == "y" or resposta == "yes":
        # Linha 36: Se sim, chamamos a função novamente (recursão)
        # Isso permite calcular várias vezes sem reiniciar o programa
        calcular_imc()
    else:
        # Linha 37: Mensagem de despedida
        print("\n🙏 Obrigado por usar a Calculadora de IMC!")
        print("   Cuide bem da sua saúde. Até a próxima! 🌟")
        print("\n" + "═" * 60)

# ================================================
# SEÇÃO 8: PONTO DE ENTRADA DO PROGRAMA
# ================================================

# Linha 38: Este é o ponto de entrada padrão em Python
# Quando executamos "python app.py", o Python procura por __name__ == "__main__"
if __name__ == "__main__":
    # Linha 39: Chamamos a função principal para iniciar o programa
    calcular_imc()

# ================================================
# FIM DO ARQUIVO app.py
# ================================================
# Este programa foi criado com comentários detalhados linha por linha
# para ajudar no aprendizado de Python e conceitos de IMC.
#
# Dica para GitHub: 
# git add app.py
# git commit -m "Adiciona calculadora de IMC em Python com comentários"
# git push
# ================================================
