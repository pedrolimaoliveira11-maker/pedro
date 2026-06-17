// ================================================
// script.js - Lógica da Calculadora de IMC
// ================================================
// Este arquivo contém toda a lógica JavaScript da calculadora.
// Ele deve ser linkado no index.html usando: <script src="script.js"></script>
//
// COMENTADO LINHA POR LINHA para facilitar o aprendizado.
// ================================================


// ================================================
// FUNÇÃO: calcularIMC()
// É chamada quando o usuário clica no botão "CALCULAR MEU IMC"
// ================================================
function calcularIMC() {
    // Linha 1: Pegamos os elementos dos inputs de peso e altura
    const pesoInput = document.getElementById('peso');
    const alturaInput = document.getElementById('altura');

    // Linha 2: Convertemos os valores digitados (texto) para números decimais
    const peso = parseFloat(pesoInput.value);
    const altura = parseFloat(alturaInput.value);

    // ================================================
    // VALIDAÇÃO DOS DADOS
    // ================================================

    // Linha 3: Verifica se os campos estão vazios ou com valor inválido
    if (!peso || !altura || peso <= 0 || altura <= 0) {
        alert("⚠️ Por favor, preencha os campos de peso e altura com valores válidos e maiores que zero.");
        
        // Linha 4: Foca no campo que está errado
        if (!peso || peso <= 0) {
            pesoInput.focus();
        } else {
            alturaInput.focus();
        }
        return; // Para a execução da função
    }

    // Linha 5: Validação de altura realista
    if (altura < 0.5 || altura > 2.5) {
        alert("⚠️ Altura fora do intervalo realista. Verifique o valor digitado.");
        alturaInput.focus();
        return;
    }

    // Linha 6: Validação de peso realista
    if (peso < 1 || peso > 300) {
        alert("⚠️ Peso fora do intervalo realista. Verifique o valor digitado.");
        pesoInput.focus();
        return;
    }

    // ================================================
    // CÁLCULO DO IMC
    // ================================================

    // Linha 7: Aplica a fórmula do IMC → IMC = peso / (altura × altura)
    const imc = peso / (altura * altura);

    // Linha 8: Arredonda para 2 casas decimais
    const imcArredondado = imc.toFixed(2);

    // ================================================
    // CLASSIFICAÇÃO DO IMC (segundo a OMS)
    // ================================================

    let classificacao = "";
    let emoji = "";
    let corClasse = "";
    let mensagem = "";

    // Linha 9: Estrutura de decisão para definir a classificação
    if (imc < 18.5) {
        classificacao = "Abaixo do peso";
        emoji = "🔴";
        corClasse = "bg-red-100 text-red-700 border border-red-200";
        mensagem = "Você está abaixo do peso ideal. Recomenda-se consultar um nutricionista.";
    } 
    else if (imc < 25) {
        classificacao = "Peso normal";
        emoji = "🟢";
        corClasse = "bg-emerald-100 text-emerald-700 border border-emerald-200";
        mensagem = "Parabéns! Seu peso está dentro da faixa considerada saudável pela OMS.";
    } 
    else if (imc < 30) {
        classificacao = "Sobrepeso";
        emoji = "🟡";
        corClasse = "bg-amber-100 text-amber-700 border border-amber-200";
        mensagem = "Você está com sobrepeso. Pequenas mudanças na alimentação e exercícios podem ajudar.";
    } 
    else if (imc < 35) {
        classificacao = "Obesidade grau I";
        emoji = "🟠";
        corClasse = "bg-orange-100 text-orange-700 border border-orange-200";
        mensagem = "Você está na faixa de obesidade grau I. Busque orientação médica e nutricional.";
    } 
    else if (imc < 40) {
        classificacao = "Obesidade grau II";
        emoji = "🔴";
        corClasse = "bg-red-100 text-red-700 border border-red-200";
        mensagem = "Obesidade grau II. Recomenda-se fortemente acompanhamento médico.";
    } 
    else {
        classificacao = "Obesidade grau III";
        emoji = "🔴";
        corClasse = "bg-red-200 text-red-800 border border-red-300";
        mensagem = "Obesidade grau III (mórbida). Procure atendimento médico especializado.";
    }

    // ================================================
    // ATUALIZAÇÃO DA PÁGINA (DOM)
    // ================================================

    // Linha 10: Pegamos os elementos onde vamos mostrar o resultado
    const resultadoDiv = document.getElementById('resultado');
    const valorImcEl = document.getElementById('valor-imc');
    const emojiEl = document.getElementById('emoji-resultado');
    const classificacaoEl = document.getElementById('classificacao');
    const mensagemEl = document.getElementById('mensagem');

    // Linha 11: Preenchemos os valores na tela
    valorImcEl.innerHTML = imcArredondado;
    emojiEl.innerHTML = emoji;
    classificacaoEl.innerHTML = classificacao;
    classificacaoEl.className = `px-4 py-1.5 rounded-full text-sm font-bold ${corClasse}`;
    mensagemEl.innerHTML = mensagem;

    // Linha 12: Mostramos a área de resultado com animação
    resultadoDiv.classList.remove('hidden');
    resultadoDiv.classList.add('resultado-animado');

    // Linha 13: Rolamos a tela até o resultado
    resultadoDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });

    // Linha 14: Mostramos no console (para desenvolvedores)
    console.log(`[IMC] Peso: ${peso}kg | Altura: ${altura}m | IMC: ${imcArredondado} | Classificação: ${classificacao}`);
}


// ================================================
// FUNÇÃO: limparCampos()
// Limpa os campos e esconde o resultado
// ================================================
function limparCampos() {
    // Linha 15: Limpa os inputs
    document.getElementById('peso').value = '';
    document.getElementById('altura').value = '';

    // Linha 16: Esconde a área de resultado
    const resultadoDiv = document.getElementById('resultado');
    resultadoDiv.classList.add('hidden');
    resultadoDiv.classList.remove('resultado-animado');

    // Linha 17: Foca no campo de peso novamente
    document.getElementById('peso').focus();
}


// ================================================
// FUNÇÃO: reiniciarCalculadora()
// Usada pelo botão "Calcular novamente"
// ================================================
function reiniciarCalculadora() {
    // Linha 18: Esconde o resultado
    const resultadoDiv = document.getElementById('resultado');
    resultadoDiv.classList.add('hidden');
    resultadoDiv.classList.remove('resultado-animado');

    // Linha 19: Limpa os campos
    document.getElementById('peso').value = '';
    document.getElementById('altura').value = '';

    // Linha 20: Rola até o formulário
    document.getElementById('form-imc').scrollIntoView({ behavior: 'smooth' });

    // Linha 21: Foca no campo de peso após meio segundo
    setTimeout(() => {
        document.getElementById('peso').focus();
    }, 500);
}


// ================================================
// EVENTOS DA PÁGINA
// ================================================

// Linha 22: Quando a página terminar de carregar
window.onload = function() {
    
    // Linha 23: Permite calcular apertando Enter nos inputs
    const inputs = document.querySelectorAll('#peso, #altura');

    inputs.forEach(input => {
        input.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                calcularIMC();
            }
        });
    });

    // Linha 24: Foca automaticamente no campo de peso ao abrir a página
    document.getElementById('peso').focus();

    // Linha 25: Mensagem no console (visível apertando F12)
    console.log('%c[IMC] Calculadora de IMC carregada com sucesso! (script.js)', 'color: #64748b');
};
