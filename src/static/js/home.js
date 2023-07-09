var profile = document.getElementById('profile_form')
var profileImage = document.getElementById('profile_image')
var submitButton = document.getElementById('submit')
var chatInput = document.getElementById('text')
var chatTable = document.getElementById('chat_table')
var chatContainer = document.getElementById('chat_container')
var colorInput = document.getElementById('color')
var currentUserNickname
var currentUserColor
const socket = io('http://127.0.0.1:5000')

async function setInfo() {
    const response = await fetch('http://127.0.0.1:5000/info', { method: 'GET' })
    const responseJson = await response.json();
    currentUserNickname = responseJson.nickname
    currentUserColor = responseJson.color
    nicknameInput.value = currentUserNickname
    initialNickname = currentUserNickname
    initialColor = currentUserColor
    colorInput.value = currentUserColor
    profileImage.style.backgroundColor = currentUserColor
}

setInfo()
var nicknameInput = document.getElementById('nickname');

function showSubmitButton() {
    submitButton.style.visibility = 'visible'
}

function hideSubmitButton() {
    submitButton.style.visibility = 'hidden'
}

function updateScroll(){
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function addMessageToChat(user, message) {
    chatTable.innerHTML += `<tr><td class="message"><b>${user}: </b>${message}</td><tr><tr><td class="divider"></td><tr>`
    updateScroll()
}

function sendMessage() {
    socket.emit('message', { user: currentUserNickname, message: chatInput.value })
    chatInput.value = ''
}

profile.addEventListener('input', () => {
    if (initialNickname != document.getElementById('nickname').value ||
        initialColor != document.getElementById('color').value) {
        showSubmitButton()
    } else {
        hideSubmitButton()
    }
})

chatInput.addEventListener('keypress', (event) => {
    if (event.key == 'Enter') {
        sendMessage()
    }
})

socket.on('connect', () => {
    console.log('connected');
})

socket.on('message', (data) => {
    addMessageToChat(data.user, data.message)
})

socket.on('error', (data) => {
    alert('Something went wrong with the chat!');
})