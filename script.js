// --- SISTEMA DE ESTRELAS DE FUNDO ---
function generateUniverse() {
    // Número de estrelas
    const starCount = 80;

    for (let i = 0; i < starCount; i++) {
        const star = document.createElement('div');
        star.className = 'star';

        // Tamanho aleatório (pequenas e grandes)
        const size = Math.random() * 3 + 1; // Entre 1px e 4px
        star.style.width = size + 'px';
        star.style.height = size + 'px';

        // Posição horizontal aleatória
        star.style.left = Math.random() * 100 + 'vw';

        // Posição vertical inicial aleatória
        star.style.top = Math.random() * 100 + 'vh';

        // Duração da animação aleatória (Parallax)
        // Estrelas maiores parecem cair mais rápido
        const duration = (Math.random() * 3 + 3) * (5 / size); 
        star.style.animationDuration = duration + 's';

        // Brilho aleatório
        star.style.opacity = Math.random() * 0.5 + 0.2;

        container.appendChild(star);
    }
}

// Inicia o universo quando o jogo começa
generateUniverse();
