// Variável para controlar o intervalo do tiro automático
let autoFireInterval;

// Função para iniciar o tiro automático
function startAutoFire() {
    autoFireInterval = setInterval(() => {
        if (active) { // Só atira se o jogo não for Game Over
            fire();
        }
    }, 200); // 200ms significa 5 tiros por segundo. Diminua para atirar mais rápido!
}

// Chame a função no final do script para começar assim que o jogo abrir
startAutoFire();

// AJUSTE NO CONTROLE: Remova o 'fire()' do evento de teclado
document.addEventListener('keydown', (e) => {
    if (!active) return;
    if (e.key === 'ArrowLeft' || e.key === 'a') playerX -= 25;
    if (e.key === 'ArrowRight' || e.key === 'd') playerX += 25;
    
    // O if (e.key === ' ') foi removido daqui para não atirar manualmente
    
    playerX = Math.max(25, Math.min(window.innerWidth - 25, playerX));
    player.style.left = playerX + 'px';
});
