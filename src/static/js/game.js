// Obtendo referência para o elemento canvas
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Objeto para guardar jogadores
let players = {}

// Conectando ao servidor web socket do jogo
const socket = io('http://127.0.0.1:5000')
socket.on('connect', () => {
  socket.emit('join', { room: room })
})

socket.on('position', (data) => {
  players[data.nickname] = {position: data.position, size: data.size, color: data.color, nickname: data.nickname}
})

// Definindo uma constante de atraso
const delay = 0.1;

// Definindo variável para armazenar o tamanho da bola
let ballSize = 20;

// Variáveis para armazenar a posição atual e anterior do mouse
let mouseX = 0;
let mouseY = 0;
let ballTargetX = canvas.width / 2;
let ballTargetY = canvas.height / 2;

// Função para atualizar a posição da bola com base no mouse, com atraso
function updateBallPosition(e) {
  const rect = canvas.getBoundingClientRect();
  mouseX = e.clientX - rect.left;
  mouseY = e.clientY - rect.top;
}

// Função para atualizar a posição da bola gradualmente em direção à posição atual do mouse
function updateBall() {
  const dx = mouseX - ballTargetX;
  const dy = mouseY - ballTargetY;
  ballTargetX += dx * delay;
  ballTargetY += dy * delay;
  socket.emit('position', {position: {x: ballTargetX, y: ballTargetY}, size: ballSize, room: room, nickname: nickname, color: color})
}

// Função para desenhar a bola na posição atualizada
function drawBall(x, y, size, color, nickname) {
  ctx.beginPath();
  ctx.arc(x, y, size, 0, Math.PI * 2);
  ctx.fillStyle = color;
  ctx.fill();
  ctx.closePath();
  ctx.fillStyle = '#000000'
  ctx.font = `${size - 8}px sans-serif`;
  ctx.textAlign = 'center'
  ctx.fillText(nickname, x, y)
}

// Função para limpar o canvas e desenhar novamente
function redrawCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (const player in players) {
      drawBall(players[player].position.x, players[player].position.y, players[player].size, players[player].color, players[player].nickname)
    }
  }
  

// Função principal para animar o jogo
function gameLoop() {
  updateBall();
  redrawCanvas();
  requestAnimationFrame(gameLoop);
}

// Adicionando evento para atualizar a posição do mouse
canvas.addEventListener('mousemove', updateBallPosition);

// Iniciando o loop do jogo
gameLoop();
