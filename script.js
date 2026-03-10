const container = document.getElementById('game-container');
const player = document.getElementById('player');
const scoreEl = document.getElementById('score');
const lifeEl = document.getElementById('lives');

let playerX = window.innerWidth / 2;
let score = 0;
let lives = 3;
let active = true;
let level = 1; // Começa no nível 1

// 1. DISPARO AUTOMÁTICO COM LÓGICA DE NÍVEL
setInterval(() => {
    if (active) {
        if (level === 1) {
            // Tiro Simples (Centro)
            createBullet(0); 
        } else {
            // Tiro Dobrado (Saindo das Asas)
            createBullet(-15); // Tiro da esquerda
            createBullet(15);  // Tiro da direita
        }
    }
}, 250); // Velocidade do tiro (ms)

function createBullet(offset) {
    const b = document.createElement('div');
    b.className = 'bullet';
    // Posiciona o tiro com base no centro do foguete + o deslocamento (offset)
    b.style.left = (playerX + offset - 2) + 'px';
    b.style.bottom = '90px';
    container.appendChild(b);

    let pos = 90;
    const move = setInterval(() => {
        pos += 15;
        b.style.bottom = pos + 'px';

        // Colisão com Aliens
        document.querySelectorAll('.alien').forEach(a => {
            if (checkCol(b, a)) {
                a.remove();
                b.remove();
                clearInterval(move);
                updateScore(100);
            }
        });

        if (pos > window.innerHeight) {
            b.remove();
            clearInterval(move);
        }
    }, 20);
}

// 2. ATUALIZAR PONTUAÇÃO E NÍVEL
function updateScore(pts) {
    score += pts;
    scoreEl.innerText = score;

    // Lógica para subir de nível (Ex: Ganha tiro duplo aos 2000 pontos)
    if (score >= 2000 && level === 1) {
        level = 2;
        showLevelUpMessage();
    }
}

function showLevelUpMessage() {
    const msg = document.createElement('div');
    msg.innerHTML = "<h2 style='color: #ffff00; position: absolute; top: 40%; left: 50%; transform: translate(-50%,-50%); z-index: 100;'>UPGRADE: TIRO DUPLO!</h2>";
    container.appendChild(msg);
    setTimeout(() => msg.remove(), 2000);
}

// 3. MOVIMENTAÇÃO
document.addEventListener('keydown', (e) => {
    if (!active) return;
    if (e.key === 'ArrowLeft' || e.key === 'a') playerX -= 30;
    if (e.key === 'ArrowRight' || e.key === 'd') playerX += 30;
    
    playerX = Math.max(25, Math.min(window.innerWidth - 25, playerX));
    player.style.left = playerX + 'px';
});

// 4. SPAWN DE INIMIGOS
function spawn() {
    if (!active) return;
    const a = document.createElement('div');
    a.className = 'alien';
    a.style.left = Math.random() * (window.innerWidth - 40) + 'px';
    a.style.top = '-40px';
    container.appendChild(a);

    let y = -40;
    const moveA = setInterval(() => {
        y += 4 + (level * 0.5); // Aliens ficam um pouco mais rápidos conforme o nível
        a.style.top = y + 'px';

        if (checkCol(a, player)) {
            lives--;
            lifeEl.innerText = lives;
            a.remove();
            clearInterval(moveA);
            if (lives <= 0) {
                active = false;
                document.getElementById('game-over').style.display = 'block';
            }
        }
        if (y > window.innerHeight) { a.remove(); clearInterval(moveA); }
    }, 30);
}

function checkCol(a, b) {
    const r1 = a.getBoundingClientRect(), r2 = b.getBoundingClientRect();
    return !(r1.top > r2.bottom || r1.bottom < r2.top || r1.right < r2.left || r1.left > r2.right);
}

// Iniciar Spawn e Estrelas
setInterval(spawn, 1000);

// Criar estrelas de fundo
for(let i=0; i<50; i++){
    const s = document.createElement('div');
    s.className = 'star';
    s.style.width = s.style.height = Math.random()*3+'px';
    s.style.left = Math.random()*100+'vw';
    s.style.top = Math.random()*100+'vh';
    s.style.animationDuration = (Math.random()*3+2)+'s';
    container.appendChild(s);
}
