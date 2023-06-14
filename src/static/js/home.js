var profile = document.getElementById('profile_form')
var submitButton = document.getElementById('submit')
var chatInput = document.getElementById('text')
var chatTable = document.getElementById('chat_table')
var chatContainer = document.getElementById('chat_container')
var currentUserNickname

async function setNickname() {
    const response = await fetch('http://127.0.0.1:5000/nickname', { method: 'GET' })
    const responseJson = await response.json();
    currentUserNickname = responseJson.nickname
    nicknameInput.value = currentUserNickname
}

setNickname()
var nicknameInput = document.getElementById('nickname');
var initialNickname = nicknameInput.value

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


profile.addEventListener('input', () => {
    if (initialNickname != document.getElementById('nickname').value) {
        showSubmitButton()
    } else {
        hideSubmitButton()
    }
})

chatInput.addEventListener('keypress', (event) => {
    if (event.key == 'Enter') {
        addMessageToChat(currentUserNickname, chatInput.value)
        chatInput.value = ''
    }
})