/* Chefão Estilizado */
.boss { 
    width: 160px; 
    height: 90px; 
    background: linear-gradient(180deg, #4b0082, #000); 
    position: absolute; 
    border-radius: 20px 20px 80px 80px; 
    box-shadow: 0 0 50px #ff00ff; 
    z-index: 5; 
    border: 2px solid #ff00ff;
}

/* Olhos do Chefão */
.boss::before, .boss::after {
    content: '';
    position: absolute;
    width: 25px;
    height: 8px;
    background: #ff0000;
    top: 35px;
    box-shadow: 0 0 15px #ff0000;
    border-radius: 50%;
}
.boss::before { left: 35px; transform: rotate(-10deg); }
.boss::after { right: 35px; transform: rotate(10deg); }
