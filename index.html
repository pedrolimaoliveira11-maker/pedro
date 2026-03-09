const container = document.getElementById('game-container');
const player = document.getElementById('player');
const lifeDisplay = document.getElementById('life-count');
const scoreBoard = document.getElementById('score-board');

let playerX = window.innerWidth / 2;
let score = 0;
let lives = 3;
let gameActive = true;
let bossActive = false;

// Controle de movimento
document.addEventListener('keydown', (e) => {
    if (!gameActive) return;
    if (e.key === 'ArrowLeft' || e.key === 'a') playerX -= 25;
    if (e.key === 'ArrowRight' || e.key === 'd') playerX += 25;
    if (e.key === ' ') fireBullet();
    
    playerX = Math.max(25, Math.min(window.innerWidth - 25, playerX));
    player.style.left = playerX + 'px';
});

function fireBullet() {
    const bullet = document.createElement('div');
    bullet.className = 'bullet';
    bullet.style.left = (playerX - 2) + 'px';
    bullet.style.bottom = '70px';
    container.appendChild(bullet);

    let bPos = 70;
    const moveB = setInterval(() => {
        bPos += 12;
        bullet.style.bottom = bPos + 'px';

        // Colisão com Aliens ou Boss
        const targets = document.querySelectorAll('.alien, .boss');
        targets.forEach(t => {
            if (isColliding(bullet, t)) {
                if (t.classList.contains('boss')) {
                    t.hp -= 1;
                    if (t.hp <= 0) destroyTarget(t, moveB, bullet, 5000);
                } else {
                    destroyTarget(t, moveB, bullet, 100);
                }
            }
        });

        if (bPos > window.innerHeight) { clearInterval(moveB); bullet.remove(); }
    }, 20);
}

function destroyTarget(target, interval, bullet, points) {
    const r = target.getBoundingClientRect();
    createExplosion(r.left + r.width/2, r.top + r.height/2);
    score += points;
    scoreBoard.innerText = `PONTOS: ${score}`;
    clearInterval(interval);
    target.remove();
    bullet.remove();
    if (target.classList.contains('boss')) bossActive = false;
}

function createAlien() {
    if (!gameActive || bossActive) return;
    
    // Chance de spawnar o BOSS
    if (score >= 2000 && !bossActive) {
        spawnBoss();
        return;
    }

    const alien = document.createElement('div');
    alien.className = 'alien';
    alien.style.left = Math.random() * (window.innerWidth - 60) + 30 + 'px';
    container.appendChild(alien);

    let y = -50;
    const moveA = setInterval(() => {
        y += 4;
        alien.style.top = y + 'px';

        // Colisão com Jogador
        if (isColliding(player, alien)) {
            takeDamage();
            alien.remove();
            clearInterval(moveA);
        }

        if (y > window.innerHeight) { alien.remove(); clearInterval(moveA); }
    }, 30);
}

function spawnBoss() {
    bossActive = true;
    const boss = document.createElement('div');
    boss.className = 'boss';
    boss.hp = 20; // Precisa de 20 tiros
    container.appendChild(boss);
    
    setTimeout(() => { boss.style.top = '50px'; }, 100);
}

function takeDamage() {
    lives--;
    lifeDisplay.innerText = lives;
    player.style.filter = "brightness(5)"; // Pisca branco
    setTimeout(() => player.style.filter = "none", 200);

    if (lives <= 0) {
        gameActive = false;
        document.getElementById('game-over').style.display = 'block';
    }
}

function isColliding(a, b) {
    const aR = a.getBoundingClientRect();
    const bR = b.getBoundingClientRect();
    return !(aR.top > bR.bottom || aR.bottom < bR.top || aR.right < bR.left || aR.left > bR.right);
}

function createExplosion(x, y) {
    for(let i=0; i<10; i++) {
        const p = document.createElement('div');
        p.className = 'particle';
        p.style.left = x+'px'; p.style.top = y+'px';
        container.appendChild(p);
        const ang = Math.random()*Math.PI*2;
        const vel = Math.random()*5+2;
        let px=x, py=y, op=1;
        const moveP = setInterval(() => {
            px += Math.cos(ang)*vel; py += Math.sin(ang)*vel; op -= 0.05;
            p.style.left = px+'px'; p.style.top = py+'px'; p.style.opacity = op;
            if(op<=0){ clearInterval(moveP); p.remove(); }
        }, 20);
    }
}

// Inicialização
setInterval(createAlien, 1000);
// (Incluir aqui a função createStars do código anterior)
